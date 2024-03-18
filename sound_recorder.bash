#!/bin/bash

# File name to save the recorded audio
OUTPUT_FILE="output.wav"

# Record audio for 5 seconds and save to the output file
arecord -f cd -D plughw:1,0 -d 5 -r 44100 -c 2 "$OUTPUT_FILE"

echo "Audio saved to: $OUTPUT_FILE"
