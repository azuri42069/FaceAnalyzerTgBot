import telebot
from deepface import DeepFace
import configparser

config = configparser.ConfigParser() 
config.read("settings.ini")  

api_key = config["TopSecret"]["API_KEY"]

bot = telebot.TeleBot(api_key) 

@bot.message_handler(content_types=['photo'])   
def face_analyze(message):
    try:
        fileID = message.photo[-1].file_id   
        file_info = bot.get_file(fileID)
        downloaded_file = bot.download_file(file_info.file_path)
        with open("user_media/image.jpg", 'wb') as new_file:
            new_file.write(downloaded_file)
        
        result_dict = DeepFace.analyze(img_path="user_media/image.jpg", actions=['age', 'gender', 'race', 'emotion'])
        # age_level = result_dict[0]['age'][1]
        dom_em = result_dict[0]['dominant_emotion']
        dom_em_level = result_dict[0]['emotion'][dom_em]
        # msg1 = f"% Возможный возраст: {age_level}"
        msg2 = f"% Доминантной эмоции: {dom_em_level}"
        print(result_dict)
        # bot.send_message(message.chat.id, msg1)
        bot.send_message(message.chat.id, msg2)
    except ValueError:
        bot.send_message(message.chat.id, "Лицо не распознано")
    except:
        bot.send_message(message.chat.id, "Неизвестная Ошибка (420)")
         
    
@bot.message_handler(content_types = ['text'])
def bot_message(message):
    if message.chat.type == 'private':
        bot.send_message(message.chat.id, "Дайте нам лицо")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

    

bot.infinity_polling()