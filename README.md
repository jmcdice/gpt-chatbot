# OpenAI Endpoint Learnings

gpt-chatbot: A conversational AI chatbot
transcribe-yt-audio.py: Transcribe audio from YouTube videos


## gpt-chatbot
This is a Bash script that uses OpenAI's GPT-3 language model to create a conversational AI chatbot. The script prompts the user for input, sends it to the GPT-3 API for processing, and displays the AI's response.

## Prerequisites

Before you can use this script, you need to have an OpenAI API key. If you don't already have one, you can sign up for a free account at the [OpenAI website](https://beta.openai.com/signup/).

You need [jq](https://stedolan.github.io/jq/) installed on the system. The installation process depends on the operating system you are using.

For example, if you are using Ubuntu or Debian, you can install jq by running the following command:

```console
sudo apt-get install jq
```

If you are using CentOS or Fedora, you can install jq by running the following command:

```console
sudo yum install jq
```

If you are using macOS, you can install jq using Homebrew by running the following command:

```console
brew install jq
```

## Usage

To use the chatbot, simply run the `chatbot.sh` script in your terminal. The script will prompt you for input, and you can type in anything you like. The AI will respond with a generated text that continues the conversation.

You can exit the chatbot by typing 'exit' at any time.

You can also clear the screen, by typing 'clear' at any time.

## Configuration

The script checks for the presence of an environment variable named `OPENAI_API_KEY` in order to authenticate with the OpenAI API. If this variable is not set, the script will exit with an error message.

To set the `OPENAI_API_KEY` variable, export it in your terminal before running the script:

```bash
export OPENAI_API_KEY=your_api_key_here
```

## transcribe-yt-audio.py

### Introduction
yt-audio-transcriber-chatbot is a Python-based project that enables you to download and transcribe audio from YouTube videos. In addition, it includes a conversational chatbot that uses the OpenAI API to generate human-like responses to user input.

Installation
To use yt-audio-transcriber-chatbot, you'll need to have Python 3.x installed on your machine. Additionally, you'll need to install the yt-dlp and openai Python modules. You can install these modules using the following commands:

```console
  pip install yt-dlp
  pip install openai
```

## Usage
### Downloading and Transcribing Audio from YouTube Videos

To download and transcribe audio from a YouTube video, you can run the transcribe-ytaudio.py script from the command line:

```console
  ./transcribe-yt-audio.py <video_url>
```

This will download the audio from the YouTube video and save it as an mp3 file in a directory with a name generated from the video's title. The script will also transcribe the audio using the OpenAI API and save the transcript as a text file in the same directory.



