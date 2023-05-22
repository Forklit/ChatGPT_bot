import openai
import telebot

API_TOKEN = '6055272465:AAGAY7be6esOyfnltFqsUQOcGWmM6HZfK4E'
openai.api_key = "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"

bot = telebot.TeleBot(API_TOKEN)


# Men xato qilgan joy
def get_response(msg):
    completion = openai.Completion.create(
        engine="text-davinci-003",
        prompt=msg,
        max_tokens=4000,
        n=2,
        stop=None,
        temperature=0,
    )
    return completion.choices[0].text


def get_code(msg):
    response = openai.Completion.create(
        model="code-davinci-002",
        prompt=msg,
        temperature=0,
        max_tokens=256,
    )
    return response.choices[0].text


# Command yoziladigan joy
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # bot.send_message(message.chat.id,message.text)
    bot.send_message(message.chat.id, """\
Assalomu alaykum. Men To'lqin O'rinbayev tomonidan Telegramm ga integratsiya qilingan ChatGPT3 bo'laman. Istalgan savolingizni bering ! 
Savol berish uchun /ask  buyrug'ini ishlating! Stable Diffusion yordamida rasm chizmoqchi bo'lsangiz https://t.me/txt2image_exhuman_bot ga o'ting \
""")


# Men xato qilgan joy2
@bot.message_handler(commands=['ask'])
def first_process(message):
    bot.send_message(message.chat.id, "Savolingzni bering!")
    bot.register_next_step_handler(message, second_process)


def again_send(message):
    bot.register_next_step_handler(message, second_process)


def second_process(message):
    bot.send_message(message.chat.id, get_response(message.text))
    again_send(message)


bot.infinity_polling()

# api_requestor.py da TIMEOUT_SECS = 36000 qilib o'zgartirganman, agar muommo bo'sa o'sha joydan to'g'irlash kerak
