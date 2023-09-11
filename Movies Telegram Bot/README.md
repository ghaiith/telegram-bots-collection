# Movies Telegram Bot


## Description

Movies Telegram Bot is a simple Telegram bot built using Python that allows users to get information about movies. The bot uses the OMDB API to fetch movie details and also provides the option to translate the movie description to Arabic using the MyMemory translation API.

## Features

- Get movie information (title, rating, description).
- Translate movie description to Arabic.
- Send movie posters along with the information.

## How to Use

1. Open Telegram and search for the Movies Telegram Bot (username: `@your_bot_username`).
2. Start a chat with the bot.
3. Send the name of the movie you want to get information about.
4. If the movie exists, the bot will reply with the movie's details, including title, rating, and description.
5. If available, the bot will also send the movie poster.

## Installation

To run this bot locally or deploy it on your server, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/ghaiith/movies-telegram-bot.git
cd movies-telegram-bot
```

2. Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

3. Replace `'YOUR_TELEGRAM_BOT_TOKEN'` with your actual Telegram bot token in the `main.py` file:

```python
# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual bot token obtained from BotFather on Telegram.
bot = telebot.TeleBot('YOUR_TELEGRAM_BOT_TOKEN')
```

4. Obtain an API key from the OMDB API by registering at https://www.omdbapi.com/ and replace `'YOUR_OMDB_API_KEY'` with your actual API key in the `main.py` file:

```python
# Replace 'YOUR_OMDB_API_KEY' with your actual API key obtained from the OMDB API.
api_url = f"http://www.omdbapi.com/?t={user_input}&apikey=YOUR_OMDB_API_KEY"
```

5. Obtain an API key from the MyMemory translation API by registering at https://mymemory.translated.net/doc/usagelimits.php and replace `'YOUR_MYMOMORY_API_KEY'` with your actual API key in the `main.py` file:

```python
# Replace 'YOUR_MYMOMORY_API_KEY' with your actual API key obtained from the MyMemory translation API.
api_url = f"https://api.mymemory.translated.net/get?q={description}&langpair=en|ar&key=YOUR_MYMOMORY_API_KEY"
```

6. Run the bot:

```bash
python main.py
```

7. The bot should be up and running, ready to respond to messages on Telegram.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- The bot uses the OMDB API (https://www.omdbapi.com/) to fetch movie details.
- The bot uses the MyMemory translation API (https://mymemory.translated.net/doc/usagelimits.php) to translate movie descriptions to Arabic.

## Disclaimer

This bot is created for educational purposes and should not be used for any commercial or malicious activities. The developers are not responsible for any misuse or damage caused by the bot.

