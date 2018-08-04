# -*- coding: utf-8 -*-
import random
#import io
import sys
if int(sys.version[0]) < 3:
    from proxy2 import *
else:
    from proxy3 import *

set_logging(True)
init()


cities = []
citiesAlreadySaid = []
lastLetter = None
nextCity = None 
check_give_up = False
cityUser = None


log("LOADING 1")
try:
    with open("cities.db", encoding = "utf-8", mode = "r") as file:
        for line in file:
            cities.append(line.strip())
except IOError as e:
    sendMessage("DeskChan:request-say", "Прости, база данных \"cities.db\" не найдена")
    log(e)
    end_init()


def getCharacter(sender, data):
    log("got experience: " + data["experience"])
    return data["experience"]



sendMessage("core:add-command", {"tag": "cities:play", "info": "плагин-игра городки"})


def get_last_char(city):
    i = -1
    while city[i] in ["ъ", "ь", "ы"]:
        i -= 1
    
    return city[i].upper()

def get_city(letter):
    copyCity = []
    for city in cities:
        if city[0] == letter and city not in citiesAlreadySaid:
            copyCity.append(city)
    return copyCity[random.randint(0, len(copyCity) - 1)]


def game_iteration(sender, data):
    log_warn("got inside function")


    try:
        global check_give_up
        global lastLetter
        global nextCity
        global cityUser

        experience = sendMessage("talk:get-preset", None, getCharacter)

        if check_give_up:
            check_give_up = False
            if "не" in data["value"].lower():
                sendMessage("DeskChan:say", {"text": "Тогда говори город. Я говорила " + nextCity + ", помнишь?", "skippable": False})
            elif "да" in data["value"].lower():
                sendMessage("gui:set-image", "happy")
                sendMessage("DeskChan:say", {"text": "Урааа! Я выигралаа!", "skippable": False})
                lastLetter = None
                return
            else:
                sendMessage('DeskChan:say', "Ну... я так понимаю - играем. Хорошо, давай по " + "\"" + cityUser + "\"" + " продолжим.")
                
            sendMessage("DeskChan:request-user-speech", None, game_iteration)
            return
            
        
        if lastLetter is None:
            nextCity = cities[random.randint(0, len(cities) - 1)]
            citiesAlreadySaid.append(nextCity)
            lastLetter = get_last_char(nextCity)
            sendMessage("DeskChan:say", {"text": "Я начинаю и говорю... " + nextCity + ". Твоя очередь. Тебе на " + lastLetter, "skippable": False})
        else:
            cityUser = data["value"]

            
            if cityUser in cities:
                check_give_up = False
 
                if cityUser[0] == lastLetter and cityUser not in citiesAlreadySaid:
                    citiesAlreadySaid.append(cityUser)
                    lastLetter = get_last_char(cityUser)
                    sendMessage("DeskChan:say", {"text": "Молодец, правильно. Мне на " + lastLetter, "skippable": False})

                    nextCity = get_city(lastLetter)
                    lastLetter = get_last_char(nextCity)
                    citiesAlreadySaid.append(nextCity)
                    sendMessage("gui:set-image", "thoughtful")
                    sendMessage('DeskChan:say', "Я говорю... " + nextCity + ". Твоя очередь. Тебе на " + lastLetter)

                elif cityUser[0] != lastLetter:
                    sendMessage("DeskChan:say", {"text": "Ты назвал мне город не на ту букву! Я же сказала " + nextCity + " !", "skippable": False})
                elif cityUser[0] == lastLetter and cityUser in citiesAlreadySaid:
                    sendMessage("gui:set-image", "sceptic")
                    sendMessage("DeskChan:say", {"text": "Ну что ты не следишь, " + cityUser + " уже называли! Подумай хорошенько ещё раз.", "skippable": False})


            elif cityUser not in cities:
                sendMessage("gui:set-image", "serious")
                sendMessage("DeskChan:say", {"text": "Что-то ты вообще не то задал. Или уже даёшься? (да/нет)", "skippable": False})
                check_give_up = True


        sendMessage("DeskChan:request-user-speech",None, game_iteration)
    except Exception as e:
        log(e)



addMessageListener("cities:play", game_iteration)

#здесь мы связываем команду и событие    
sendMessage("core:set-event-link", {"eventName": "speech:get", "commandName": "cities:play", "rule": "игра городки"})




# plugin informations
setConfigField("dependencies", "python3")
setConfigField("author", "DeskChan Project <support@deskchan.info> (http://deskchan.info)")
setConfigField("short-description", {
                   "ru": "ДескЧан плагин: Игра в 'Города'",
                   "en": "DeskChan plagin: game 'cities'"
               })
setConfigField("name", {
                   "ru": "Игра в 'Города'",
                   "en": "Game 'cities'"
               })
setConfigField("link", "https://forum.deskchan.info/topic/130/python-ygra-v-goroda")
setConfigField("version", "0.8")

end_init()
