import os
import sys
import argparse
from rapidfuzz import process
from pydub import AudioSegment

def parse_args():
    parser = argparse.ArgumentParser(
        description="TTS for the HL1 announcer using rapidfuzzing"
    )

    parser.add_argument(
        "library_dir",
        help="Directory containing the .wav files"
    )

    parser.add_argument(
        "output",
        help="Name of the file to be outputted"
    )

    parser.add_argument(
        "sentence",
        nargs="+",
        help="Sentence to generate an audio file from"
    )

    return parser.parse_args()


args = parse_args()
WORD_DIR = args.library_dir
output_name = args.output + ".wav"
sentence = " ".join(args.sentence)
print(output_name)

available_words = [
    os.path.splitext(f)[0]
    for f in os.listdir(WORD_DIR)
    if f.endswith(".wav")
]

def closest_match(word):
    if word in available_words:
        return word
    match, score, _ = process.extractOne(word, available_words)
    print("word had to be replaced, new word: " +  match)
    return match if score > 70 else None

def synthesize(text):
    output = AudioSegment.empty()

    for word in text.lower().split():
        matched = closest_match(word)
        if matched:
            output += AudioSegment.from_wav(f"{WORD_DIR}/{matched}.wav")
        else:
            print(f"No word found for: {word}")
            sys.exit(1)
        
    output.export(output_name, format="wav")

synthesize(sentence)