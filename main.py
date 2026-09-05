import telebot, random, time
from telebot import apihelper

PROXY_URL = "http://PROXY_URL"
apihelper.proxy = {'http': PROXY_URL, 'https': PROXY_URL}

api = telebot.TeleBot("TELEGRAM_TOKEN_BOT")

@api.message_handler()
def message(message):
    try:
        t = message.text.split(' ')
        if t[0] == "/start":
            api.send_video(message.chat.id, 'https://nn1kk00.ru/niko.mp4')
        if message.text.count("Нико") == 1 or message.text.count("нико") == 1 or message.text.count("НИКО") == 1 or message.text.count("Niko") == 1 or message.text.count("niko") == 1 or message.text.count("NIKO") == 1:
            api.send_video(message.chat.id, 'https://nn1kk00.ru/niko.mp4')
        elif message.text.count("Ноик") == 1 or message.text.count("ноик") == 1 or message.text.count("НОИК") == 1 or message.text.count("Noik") == 1 or message.text.count("noik") == 1 or message.text.count("NOIK") == 1:
            api.send_photo(message.chat.id, 'https://nn1kk00.ru/share/niko.png')
        else:
            a, b = random.randint(1, 25), random.randint(1, 25)
            if a == b: 
                if random.randint(1, 2) == 1: api.send_video(message.chat.id, 'https://nn1kk00.ru/niko.mp4')
                else: api.send_photo(message.chat.id, 'https://nn1kk00.ru/share/niko.png')
    except Exception as e:
        api.send_message(message.from_user.id, e)

while(1):
    try: api.polling(non_stop=True, interval=0)
    except:
        print("ERROR: Time OUT")
        time.sleep(0.5)
        print("Connecting...")
