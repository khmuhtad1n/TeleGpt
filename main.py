import os
from dotenv.main import load_dotenv
import telebot
import openai

load_dotenv()
openai.api_key = os.getenv('api_openai')
bot = telebot.TeleBot(
    os.getenv('api_tele')
)
conversation_history = {}

#using GPT-3.5-turbo chat model
def generate_response(user_id, text):
    if user_id not in conversation_history:
        conversation_history[user_id] = []

    conversation_history[user_id].append({"role": "user", "content": text})

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", #using GPT-3.5-turbo chat model
        messages=conversation_history[user_id],
        max_tokens=200  # Adjust as needed
    )

    reply = response['choices'][0]['message']['content'].strip()
    conversation_history[user_id].append({"role": "assistant", "content": reply})

    return reply

# handle incoming messages
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_id = message.from_user.id
    user_input = message.text
    response = generate_response(user_id, user_input)
    bot.reply_to(message, response)

def main():
    bot.polling()

if __name__ == '__main__':
    main()
