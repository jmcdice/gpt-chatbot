#!/usr/bin/env python3

import sys
import os
import re
import argparse
import yt_dlp
import openai
import json

# Get OpenAI API key from environment variable
openai.api_key = os.environ["OPENAI_API_KEY"]

# Define a function to create a slug from a string
def slugify(input_str):
    # Replace non-alphanumeric chars with hyphens
    output_str = re.sub(r'[^a-zA-Z0-9]+', '-', input_str)
    # Remove leading and trailing hyphens
    output_str = output_str.strip('-')
    # Convert to lower-case
    output_str = output_str.lower()
    return output_str

# Define a function to download the audio from the video
def download_youtube_audio(url, output_file):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': output_file,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def transcribe_audio(output_file):
    # Get OpenAI API key from environment variable
    openai.api_key = os.environ["OPENAI_API_KEY"]

    mp3_file = f"{output_file}.mp3"
    print("Output file: ", mp3_file)

    # Check if the file exists before trying to transcribe it
    if not os.path.isfile(mp3_file):
        raise Exception(f"File not found: {mp3_file}")

    # Open the file as a binary file
    with open(mp3_file, 'rb') as f:
        # Use the OpenAI API to transcribe the audio
        response = openai.Audio.transcribe("whisper-1", file=f)

    # Get the transcription from the response
    json_data = json.loads(str(response))
    transcription = json_data["text"]
    return transcription

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Download audio from a YouTube video")
    parser.add_argument("url", help="The URL of the YouTube video to download audio from")
    args = parser.parse_args()

    # Download the video and extract the title
    with yt_dlp.YoutubeDL() as ydl:
        info_dict = ydl.extract_info(args.url, download=False)
        title = info_dict.get('title', None)
        if title:
            # Create a slug from the video title for the output directory name
            slug = slugify(title)
            output_dir = f"{slug}"
            os.makedirs(output_dir, exist_ok=True)
            # Download the audio from the video
            print(f"Downloading {title}...")
            output_file = os.path.join(output_dir, f"{slug}.mp3")
            download_youtube_audio(args.url, output_file)
        else:
            sys.exit("Error: could not get video title.")

    print("Transcribing audio...")
    transcription = transcribe_audio(output_file)

    # Write the transcription to a file
    with open(os.path.join(output_dir, f"{slug}.txt"), "w") as f:
        f.write(transcription)

    print(f"Transcription written to {output_dir}/{slug}.txt")

if __name__ == '__main__':
    main()


