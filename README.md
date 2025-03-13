# TG-sender

This repository contains a Telegram bot built using `aiogram`. The bot allows users to submit applications following a specific format.

## 📌 How to Create a Telegram Bot

1. Open Telegram and search for **BotFather**.
2. Start a chat and send the command:
   ```
   /newbot
   ```
3. Follow the instructions:
   - Choose a name for your bot.
   - Choose a unique username (must end in `bot`).
4. After completion, BotFather will provide a **token**. Save it securely.

## 📦 Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/RarchikCreation/TG-sender.git
   cd TG-sender
   ```

2. Create a virtual environment (optional but recommended):
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory and add your bot token:
   ```
   TOKEN=your-telegram-bot-token
   CHANNEL_ID=your-channel-id
   ```

## 📝 Project Description

This bot allows users to submit applications by sending structured messages. It validates user inputs and forwards submissions to a Telegram channel. Features include:

- **User Input Handling**: Users send structured applications following a predefined format.
- **Cooldown System**: Prevents spam by enforcing a cooldown period.
- **Inline Buttons**: Provides buttons for direct interaction with applicants.
- **Environment Configuration**: Uses `.env` for storing sensitive data securely.

## 🚀 Running the Bot

Start the bot using:
```sh
python main.py
```

## 🛠 Technologies Used
- Python
- Aiogram
- Asyncio
- Dotenv

