import telebot
import requests

# Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual bot token obtained from BotFather on Telegram.
bot = telebot.TeleBot('YOUR_TELEGRAM_BOT_TOKEN')

# Handler for receiving messages that contain text
@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_message(message):
    try:
        user_input = message.text

        if user_input == "/start":
            bot.send_message(message.chat.id, 'Hello Welcome in Movies Telegram Bot')
        else:
            # Replace the [name] placeholder in the URL with the user's input
            api_url = f"http://www.omdbapi.com/?t={user_input}&apikey=YOUR_OMDB_API_KEY"
            response = requests.get(api_url)
            data = response.json()

            if data.get('Response') == 'True':
                # Extract information from the API response
                title = data.get('Title', 'N/A')
                rating = data.get('imdbRating', 'N/A')
                description = data.get('Plot', 'N/A')
                image_url = data.get('Poster', '')

                api_url = f"https://api.mymemory.translated.net/get?q={description}&langpair=en|ar"

                # Make the GET request to the translation API
                response = requests.get(api_url)
                response_data = response.json()

                # Check if the translation was successful and retrieve the translated text
                if "responseData" in response_data and "translatedText" in response_data["responseData"]:
                    translated_text = response_data["responseData"]["translatedText"]
                    response_message = f"Title: {title}\nRating: {rating}\n{description}\n\n{translated_text}"
                else:
                    response_message = f"Title: {title}\nRating: {rating}\nDescription:{description}\n\n {translated_text}"

                # Send the image if available
                if image_url:
                    bot.send_photo(message.chat.id, image_url, caption=response_message)
                else:
                    bot.send_message(message.chat.id, response_message)
            else:
                bot.send_message(message.chat.id, "The movie does not exist")

    except Exception as e:
        bot.send_message(message.chat.id, "A problem occurred, please try again later")

# Start the bot
bot.polling(none_stop=True, interval=0)
