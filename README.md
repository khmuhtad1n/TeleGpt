
# Telegram Bot with OpenAI GPT-3.5-Turbo

This repository contains a Python script that implements a Telegram bot using the OpenAI GPT-3.5-Turbo model. The bot can respond to user messages with generated responses from the GPT-3.5-Turbo model.

## Features

- Uses the OpenAI GPT-3.5-Turbo model for generating responses.
- Maintains conversation history for each user.
- Responds to incoming messages on Telegram.

## Requirements

- Python
- `python-telegram-bot`
- `openai`
- `python-dotenv`

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/khmuhtad1n/TeleGpt.git
cd TeleGpt
```

### 2. Install Dependencies

Make sure you have Python 3.6 or higher installed. Install the required Python packages:

```bash
pip install -r requirements.txt
```

### 3. Create a `.env` File

Create a `.env` file in the root directory of your project and add your OpenAI API key and Telegram bot token:

```env
api_openai=your_openai_api_key
api_tele=your_telegram_bot_token
```

### 4. Running the Bot

Run the bot using the following command:

```bash
python main.py
```

## Contributing

Feel free to submit issues or pull requests if you have any suggestions or improvements.

## License

This project is licensed under the MIT License.
