import telebot
from deepface import DeepFace
import configparser
import random
import math

config = configparser.ConfigParser()                   #  api key parseng
config.read("settings.ini")  

api_key = config["TopSecret"]["API_KEY"]

bot = telebot.TeleBot(api_key) 

@bot.message_handler(content_types=['photo'])             # handler for photos    
def face_analyze(message):
    try:
        fileID = message.photo[-1].file_id                                     # get new photo (1 time)
        file_info = bot.get_file(fileID)
        downloaded_file = bot.download_file(file_info.file_path)
        with open("image.jpg", 'wb') as new_file:
            new_file.write(downloaded_file)
        
        result_dict = DeepFace.analyze(img_path="image.jpg", actions=['age', 'gender', 'race', 'emotion'])       # main method
        age_level = result_dict[0]['age']
        dom_gn = result_dict[0]['dominant_gender']
        dom_gn_level = result_dict[0]['gender'][dom_gn]
        dom_rc = result_dict[0]['dominant_race']                        # rzecz pospolitaia (раздел)
        dom_rc_level = result_dict[0]['race'][dom_rc]
        dom_em = result_dict[0]['dominant_emotion']
        dom_em_level = result_dict[0]['emotion'][dom_em]
        real_age = int(age_level) - random.randint(14, 25)                                           # "real age"
        GETREAL_age = math.fabs(real_age)  # fix "-1 age"
        bot.send_message(message.chat.id, f"👶 Предположительный возраст: {GETREAL_age}-{age_level}")
        bot.send_message(message.chat.id, f"👥 Предположительный пол: {dom_gn}")
        bot.send_message(message.chat.id, f"👩🏻👦🏾Предположительная paca: {dom_rc}")
        bot.send_message(message.chat.id, f"🤯 Предположительная эмоция: {dom_em}")
        if (dom_em == 'neutral'):
            bot.send_message(message.chat.id, "🤓 Ответственный")
        else:
            bot.send_message(message.chat.id, "🤡 Безответственный")
    except ValueError:
        bot.send_message(message.chat.id, "😖 Лицо не распознано")
    except:
        bot.send_message(message.chat.id, "☠️ Неизвестная Ошибка (420)")
         
    
@bot.message_handler(content_types = ['text'])              # handler for any text message  
def bot_message(message):
    if message.chat.type == 'private':
        bot.send_message(message.chat.id, "Дайте нам лицо")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

    

bot.infinity_polling()