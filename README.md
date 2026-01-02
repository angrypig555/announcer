## announcer
Announcer is a python program that converts a string that was given into an audio file.
It only supports .wav files as it was made to be a TTS for the half life 1 announcer.

### Dependencies
Required: rapidfuzz, pydub, audioop-lts

### Usage

The audio directory must contain only .wav files and no other files or directories.
The output name can be anything as long as you don't put a file type at the end.
The sentence to be translated to the announcer voice doesn't need quotes around it.
`python main.py audio_directory output_name sentence to be translated`

If you want to use the half life 1 announcer as voice, you have to own a copy of half life 1. You can provide other .wav files as well but make sure to name them according to what word is said.