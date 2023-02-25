# gpt-chatbot: A Conversational AI Chatbot

This is a Bash script that uses OpenAI's GPT-3 language model to create a conversational AI chatbot. The script prompts the user for input, sends it to the GPT-3 API for processing, and displays the AI's response.

## Prerequisites

Before you can use this script, you need to have an OpenAI API key. If you don't already have one, you can sign up for a free account at the [OpenAI website](https://beta.openai.com/signup/).

## Usage

To use the chatbot, simply run the `chatbot.sh` script in your terminal. The script will prompt you for input, and you can type in anything you like. The AI will respond with a generated text that continues the conversation.

You can exit the chatbot by typing 'exit' at any time.

## Configuration

The script checks for the presence of an environment variable named `OPENAI_API_KEY` in order to authenticate with the OpenAI API. If this variable is not set, the script will exit with an error message.

To set the `OPENAI_API_KEY` variable, export it in your terminal before running the script:

```bash
export OPENAI_API_KEY=your_api_key_here
```

## Disclaimer

Please note that this script is provided for educational purposes only. Use of the OpenAI API is subject to their terms of service, and you should review those terms before using this script.




