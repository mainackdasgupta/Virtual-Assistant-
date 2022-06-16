import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import shutil
import smtplib
import webbrowser
import winshell
import requests
import json
from bs4 import BeautifulSoup
import ctypes
from pprint import pprint
import os
import subprocess
import wolframalpha
from ecapture import ecapture as ec

listener = sr.Recognizer()
engine = pyttsx3.init()  # initialization
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening.....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)


    except:

        pass
    return command


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        talk("Good Morning Sir !")

    elif hour >= 12 and hour < 18:
        talk("Good Afternoon Sir !")

    else:
        talk("Good Evening Sir !")

    assname = ("crypto 1 point o point 5")
    talk("I am your Assistant")
    talk(assname)

def username():
    talk("What should i call you sir")
    uname = take_command()
    talk("Welcome Mister")
    talk(uname)
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))

    talk("How can i Help you, Sir")

def mail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login('your email id', 'your email password')
    server.sendmail('your email id', to, content)
    server.close()




if __name__ == '__main__':
    clear = lambda: os.system('cls')
    clear()
    wishMe()
    username()
    while True:
        command = take_command()
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%H:%M')
            print(time)
            talk('current time is ' + time)
        elif 'who is' in command:
            person = command.replace('who is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
        elif 'open youtube' in command:
            talk("Here you go to Youtube\n")
            webbrowser.register('chrome', None,webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open("youtube.com")
        elif 'open google' in command:
            talk("Here you go to Google\n")
            webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open("google.com")
        elif 'open iemcrp' in command:
            talk("Here you go to iemcrp\n")
            webbrowser.register('chrome', None,webbrowser.BackgroundBrowser("C://Program Files//Google//Chrome//Application//chrome.exe"))
            webbrowser.get('chrome').open("iemcrp.com")
        elif 'chrome' in command:
            dir = "C://Program Files//Google//Chrome//Application//chrome.exe"
            os.startfile(dir)
            os.system(dir)
        elif 'ms word' in command:
            dir = "C://ProgramData//Microsoft//Windows//Start Menu//Programs//Microsoft Office 2013//Word 2013.lnk"
            os.startfile(dir)
            os.system(dir)
        elif 'ms excel' in command:
            dir = "C://ProgramData//Microsoft//Windows//Start Menu//Programs//Microsoft Office 2013//Excel 2013.lnk"
            os.startfile(dir)
            os.system(dir)
        elif 'open stackoverflow' in command:
            talk("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        elif 'search in google' in command:
            talk("what to search")
            query = take_command()
            talk("here we go")
            pywhatkit.search(query)
        elif 'news' in command:
            url = 'https://www.bbc.com/news'
            response = requests.get(url)

            soup = BeautifulSoup(response.text, 'html.parser')
            headlines = soup.find('body').find_all('h3')
            unwanted = ['BBC World News TV', 'BBC World Service Radio',
                        'News daily newsletter', 'Mobile app', 'Get in touch']

            for x in list(dict.fromkeys(headlines)):
                if x.text.strip() not in unwanted:
                    print(x.text.strip())
                    talk(x.text.strip())
        elif 'send a mail' in command:
            try:
                talk("What should I say?")
                content = take_command()
                talk("whom should i send")
                to = input()
                mail(to, content)
                talk("Email has been sent !")
            except Exception as e:
                print(e)
                talk("I am not able to send this email")

        elif 'how are you' in command:
            talk("I am fine, Thank you")
            talk("How are you, Sir")

        elif "don't call me sir" in command:
            talk("okay i wont")

        elif 'fine' in command or "good" in command:
            talk("It's good to know that your fine")
        elif "who made you" in command or "who created you" in command:
            talk("I have been created by Subhradeep")
        elif 'you are best crypto' in command:
            talk("Ha Ha Ha obviously I am")
        elif "who i am" in command:
            talk("If you talk then definitely your human.")
        elif "change my name to" in command:
            command = command.replace("change my name to", "")
            assname = command
        elif "change name" in command:
            talk("What would you like to call me, Sir ")
            assname = take_command()
            talk("Thanks for naming me")
        elif "what's your name" in command or "What is your name" in command:
            talk("My friends call me")
            talk(assname)
            print("My friends call me", assname)
        elif "where is" in command:
            query = command.replace("where is", "")
            location = query
            talk("User asked to Locate")
            talk(location)
            webbrowser.open('https://www.google.com/maps/place/' + location + "")
        elif 'empty recycle bin' in command:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=True)
            talk("Recycle Bin Recycled")
        elif "weather" in command:
            api_key = "Your_API_Key"
            base_url = "http://api.openweathermap.org/data/2.5/weather?"
            talk(" City name ")
            print("City name : ")
            city_name = take_command()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()

            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " +
                      str(current_temperature) +
                      "\n atmospheric pressure (in hPa unit) = " +
                      str(current_pressure) +
                      "\n humidity (in percentage) = " +
                      str(current_humidity) +
                      "\n description = " +
                      str(weather_description))

            else:
                talk(" City Not Found ")
        elif 'lock window' in command:
            talk("locking the device")
            ctypes.windll.user32.LockWorkStation()
        elif "restart" in command:
            talk("Restarting system")
            subprocess.call(["shutdown", "/r"])
        elif 'shutdown system' in command:
            talk("Shutting down")
            subprocess.call('shutdown / p /f')
        elif "camera" in command or "take a photo" in command:
            ec.capture(0, "crypto Camera ", "img.jpg")
        elif 'crypto sleep' or 'bye' in command:
            talk("Thanks for giving me your time")
            exit()
        else:
            talk('please say it again')







