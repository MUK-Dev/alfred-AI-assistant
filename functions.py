from asyncore import read
import os
from random import random
from tkinter import E
import pyttsx3
import datetime
import speech_recognition as sr
import smtplib
from secrets import senderemail, epwd
from email.message import EmailMessage
import pyautogui as pg
import webbrowser as wb
from time import sleep
import wikipedia
import pywhatkit
import clipboard
import pyjokes
import time as tt
import random

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-30)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def sendEmail(reciever, subject, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(senderemail, epwd)
    email = EmailMessage()
    email['From'] = senderemail
    email['To'] = reciever
    email['Subject'] = subject
    email.set_content(content)
    server.send_message(email)
    server.close()


def time():
    Time = datetime.datetime.now().strftime('%I:%M')
    speak('current time is')
    speak(Time)


def get_month(i):
    return ['january', 'feburary', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'octuber', 'november', 'december'][i-1]


def date():
    year = int(datetime.datetime.now().year)
    month = get_month(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak('today is')
    speak(str(date)+str(month)+str(year))


def greeting():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak('good morning, how are you')
    elif hour >= 12 and hour < 18:
        speak('good afternoon sir, how are you')
    elif hour >= 18 and hour < 24:
        speak('good evening sir, how are you')
    else:
        speak('hello sir, how are you')


def wishme():
    speak('hello this is alfred')
    greeting()
    time()
    date()
    speak('i am available if you need help')


def takeCommandCMD():
    query = input('> ')
    return query


def takeCommandMic():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-PK')
        print(query)
    except Exception as e:
        print(e)
        return "None"
    return query


def shouldSendObject(reply):
    if 'no' in reply:
        speak('please say again then')
        return False
    elif 'type' in reply:
        return 'type'
    elif 'yes' in reply:
        speak('splendid sir, i will send it as soon as possible')
        return True
    else:
        speak('please say the content of the message again')


def email():
    try:
        speak(
            'To whom do you want to send the mail, please type the email adress?')
        reciever = takeCommandCMD()
        speak('what will be the subject of this email')
        subject = takeCommandMic()
        speak('what should i say?')
        shouldSend = False
        while shouldSend != True:
            content = takeCommandMic()
            speak('is this ok? or do you want to type')
            reply = takeCommandMic().lower()
            shouldSend = shouldSendObject(reply)
            if shouldSend == 'type':
                speak('ok sir you can type in the command prompt')
                content = takeCommandCMD()
                break
        sendEmail(reciever, subject, content)
        speak('email has been sent')
    except Exception as e:
        print(e)
        speak('i was not able to send the email')


def sendWhatsappMessage(phone_no, message):
    Message = message
    wb.open('https://web.whatsapp.com/send?phone='+phone_no+'&text='+Message)
    sleep(20)
    pg.click()
    pg.press('enter')
    sleep(5)
    pg.hotkey('ctrl', 'w')


def whatsapp():
    user_name = {
        'alpha': '+923366202013',
        'beta': '+923111619466'
    }
    try:
        speak(
            'To whom do you want to send the whats app message?')
        name = takeCommandMic().lower()
        try:
            phone_no = user_name[name]
        except Exception as e:
            print(e)
            speak(
                'I don\'t know anyone by that name, you can type the phone number in the command prompt')
            phone_no = takeCommandCMD()
        speak('what is the message')
        shouldSend = False
        while shouldSend != True:
            message = takeCommandMic()
            speak('is this ok? or do you want to type')
            reply = takeCommandMic().lower()
            shouldSend = shouldSendObject(reply)
            if shouldSend == 'type':
                speak('ok sir you can type in the command prompt')
                message = takeCommandCMD()
                break
        sendWhatsappMessage(phone_no, message)
        speak('task completed')
    except Exception as e:
        print(e)
        speak('i was not able to send the message')


def openWhatsapp():
    speak('ok sir')
    wb.open('https://web.whatsapp.com')


def wikipediaSearch():
    speak('what do you want to search?')
    query = takeCommandMic().lower()
    speak('searching...')
    result = wikipedia.summary(query, sentences=2)
    print(result)
    speak(result)


def googleSearch():
    speak('what should i search on google')
    search = takeCommandMic().lower()
    wb.open(f'https://www.google.com/search?q={search}')


def youtubeSearch():
    speak('what should i search on youtube')
    topic = takeCommandMic().lower()
    pywhatkit.playonyt(topic)


def text2Speech():
    text = clipboard.paste()
    print(text)
    speak(text)


def openvscode():
    vscodepath = 'C:\\Users\\Aqib\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
    os.startfile(vscodepath)


def openFileExplorer(query):
    os.system('explorer C://{}'.format(query.replace('open', '')))


def tellJoke():
    joke = pyjokes.get_joke()
    print(joke)
    speak(joke)


def screenShot():
    name_img = tt.time()
    name_img = f'C:\\Users\\Aqib\\Desktop\\ScreenShots\\{name_img}.png'
    img = pg.screenshot(name_img)
    speak('screenshot saved in the screenshots folder on desktop')
    img.show()


def remember():
    speak('what should i remember?')
    data = takeCommandMic()
    speak('you told me to remember '+data)
    if len(open('data.txt', 'r').read()) > 1:
        data = open('data.txt', 'r').read() + ' and ' + data
    memory = open('data.txt', 'w')
    memory.write(data)
    memory.close()


def remembered():
    print(len(open('data.txt', 'r').read()))
    if len(open('data.txt', 'r').read()) == 0:
        speak('i don\'t remember anything')
    else:
        speak('you told me to remember '+open('data.txt', 'r').read())


def flip():
    speak('okay sir, flipping a coin')
    coin = ['heads', 'tails']
    toss = []
    toss.extend(coin)
    random.shuffle(toss)
    toss = (''.join(toss[0]))
    speak('you got '+toss)
