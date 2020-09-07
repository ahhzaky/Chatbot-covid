import telebot
import time

bot_token = ''

bot = telebot.TeleBot(token=bot_token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Welcome to COVID-19 Information.\nWhat information you want to do: \n\n(/1) What is the COVID-19? \n(/2)What are the indication of Covid-19? \n(/3)How to protect yourself?  \n(/4) Information Indication Global (COVID-19). \n(/5)Information link (COVID-19). \n(/6) Contact the hospital. \n ')

@bot.message_handler(commands=['1'])
def send_welcome(message):
    bot.reply_to(message, 'Coronavirus is a large family of viruses that can attack humans and animals. Well, in humans, usually causes respiratory infections, ranging from the common cold to serious illnesses, such as MERS and SARS.')

@bot.message_handler(commands=['2'])
def send_welcome(message):
    bot.reply_to(message, 'Indication of Covid-19 generally include:  \n\nFever 38 ° C, Dry cough, blown. \n\nIf you have finished traveling and 14 days later changed your symptoms, immediately go to the referral hospital to check yourself more fully.')

@bot.message_handler(commands=['3'])
def send_welcome(message):
    bot.reply_to(message, 'Protect yourself before your death. \n\nWhat do you have to do? \n~Stay at home. Work, study and worship at home. \n~Keep a minimum distance of 1 meter from other people. \n~Do not contact directly with symptomatic people COVID-19. Communicate by telephone, chat or video call. \n~Avoid the crowd \n~Dont put your face as someone else face. \nAlways wash your hands with soap and running water! Before eating and preparing food, after going to the toilet, after handling animals and after traveling. \n~When coughing or sneezing, cover your mouth and nose with folded elbows or tissue. Dispose of directly into the trash after use. \n~Contact your health care provider if you have denied a conversation, have been in close contact with symptomatic people or traveled to areas affected by COVID-19. \n~If a health worker states that you must be self-isolated, then obey so that it is quickly resolved and not infect others. \n~Be open about your status with others around you. This is the first step to mutual care together.')

@bot.message_handler(commands=['4'])
def send_welcome(message):
    bot.reply_to(message, 'Corona virus situation (Covid-19) 1 April 2020. \n\nCountry / region : 179 \nCase Confirmed : 803.313 \nDead :39.014 \nTotal Recovered: 162.014 \n\nFor info on COVID-19 distribution map, you can click on the following link: https://www.bing.com/covid ')

@bot.message_handler(commands=['5'])
def send_welcome(message):
    bot.reply_to(message, 'Link Information (COVID-19)  \n\n1. https://www.who.int/emergencies/diseases/novel-coronavirus-2019/advice-for-public - Recommendations related to coronavirus outbreaks. \n2. https://www.who.int/news-room/q-a-detail/q-a-coronaviruses - Current situation in the world.')

@bot.message_handler(commands=['6'])
def send_welcome(message):
    bot.reply_to(message, 'Number Phone 199')




@bot.message_handler(commands=['help'])
def send_welcome(message):
    bot.reply_to(message, 'Klick /start')


bot.polling()
