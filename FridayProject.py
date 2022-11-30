#Female Replacement Intelligent Digital Assistant Youth - FRIDAY
#fac108dabb984594a55bb5d0539b1059
import pyttsx3 
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
from pytube import YouTube
import time
import re
import subprocess
import pyjokes
import json
from urllib.request import urlopen
import requests
import time

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty("rate",175)

def Speak(audio):
    engine.say(audio)
    engine.runAndWait()

def date():
    hour = int(datetime.datetime.now().hour)
    if(hour <= 6 and hour < 12):
        Speak("Good moring sir")
    elif(hour >=12 and hour < 18):
        Speak("Good afternoon sir")
    elif (hour >18 and hour<6):
        Speak("Good night sir")
    Speak("its friday sir, how may i help you")
    

def inputCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Taking your command....")
        r.pause_threshold = 1
        r.energy_threshold = 800
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"You Said: {query}\n")
    except Exception as e:
        Speak("Sorry please say that again")
        print("Sorry please say that again")
        return "None"
    return query

if __name__ == "__main__":
    date()
    for i in range(3):
        query = inputCommand().lower()

        if 'wikipedia' in query:
            Speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            Speak("according to wikipedia")
            print(results)
            Speak(results)
        elif 'who are you' in query:
            print("i am Artificial Intelligence bot named friday made by saurav, sonali and yuvraj")
            Speak("i am Artificial Intelligence bot named friday made by saurav and sonali, and yuvraj")


        elif 'open chrome' in query:
            subprocess.Popen('"C:\Program Files\Google\Chrome\Application\chrome.exe"')
            Speak("Openning chrome")
            
        elif 'open youtube' in query:
            Speak("openning youtube")
            webbrowser.open("youtube.com")

        #function to ask
        elif 'how are you' in query:
            Speak("i am good sir what about you")

        #function to ask for owner
        elif 'who is sourav' in query:
            Speak("Saurav is one of my co-founder")

        #function to open google
        elif 'open google' in query:
            Speak("Openning Google")
            webbrowser.open("google.com") 

        #function to open instagram
        elif 'open instagram' in query:
            Speak("Openning Instagram")
            webbrowser.open("instagram.com")

        #open camera
        elif 'camera' in query:
            Speak("Openning camera")
            os.system("start microsoft.windows.camera:")

        #function to play music
        elif 'play music' in query:
            music_dir = 'D:\music'
            songs = os.listdir(music_dir)
            sn = random.randint(0,4)
            os.startfile(os.path.join(music_dir,songs[sn]))

        #function to download youtube video
        elif 'download youtube video' in query:
            print("press ctrl + shift + v to paste video url! \n")
            Speak("Please paste your youtube video url")
            link = input("Enter link: ")
            youtubeObject = YouTube(link)
            youtubeObject = youtubeObject.streams.get_highest_resolution()
            try:
                youtubeObject.download()
            except:
                print("Error occured")
            print("Downloaded :) anything else! ")

        #function for time
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            Speak(f"current time is, {strTime}")
            print(f"Current time is {strTime}")

        #function for stopwatch 
        elif 'stopwatch' in query:
            def time_convert(sec):
                mins = sec // 60
                sec = sec % 60
                hours = mins // 60
                mins = mins % 60
                print("Time lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))
            input("Press Enter to Start")
            start_time = time.time()
            input("Press Enter to stop")
            end_time = time.time()
            time_lapsed = end_time - start_time
            time_convert(time_lapsed)
        
        #function for calculater
        elif 'calculator' in query:
            Speak("What operation you want me to do")
            op = input("Enter operation as(+,-,x,/): ")
            n1 = int(input("Enter first number: "))
            n2 = int(input("Enter second number: "))
            if op == '+' :
                sm1 = n1 + n2
                print(sm1)
                Speak(f"sum is {sm1}")
            elif op == '-':
                sm2 = n1 - n2
                print(sm2)
                Speak(f"substractio is {sm2}")
            elif op == 'x':
                sm3 = n1*n2
                print(sm3)
                Speak(f"product is {sm3}")
            elif op == '/':
                sm4 = n1/n2
                print(sm4)
                Speak(f"divident is {sm4}")
        #dice game
        elif 'dice game' in query:
            Speak("playing dice game for you sir! ")
            num1=random.randint(1,6)
            num2=random.randint(1,6)
            print("You got: \n",num1)
            print("Friday got: \n",num2)
            if num1 > num2:
                print("You won \n")
                Speak("shiitt, you won")
            elif num1 == num2:
                print("Draw \n")
                Speak("its a draw")
            else :
                print("friday won \n")  
                Speak("yess i won")  

        #function to play rock,paper scissors
        elif 'rock paper scissor' in query:
            os.system('cls' if os.name=='nt' else 'clear')
            Speak("Number of rounds you want sir")
            n = int(input("Enter no. of rounds: "))
            i = 0
            while(i<n):
                print("\n")
                print("Rock,Paper,Scissors - shoot!")
                userChoice = input("Choose your weapon \n[R]ock \n[P]aper \n[S]cissors \n:")
                if not re.match("[SsRrPp]",userChoice):
                    print("Please choose a letter: ")
                    print("[R], [S], [P]")
                    continue
                print("you choose: "+userChoice)
                choices = ['R','P','S']
                opponenetChoice = random.choice(choices)
                if opponenetChoice == str.upper(userChoice):
                    print("Tie!")
                    Speak("Its a tie breaker")
                elif opponenetChoice == 'R' and userChoice.upper() == 'S':
                    print ("Scissors beats rock, I win! ")
                    Speak("Scissors beats rock, I win! ")
                    continue
                elif opponenetChoice == 'S' and userChoice.upper() == 'P':
                    print("Scissors beats paper! I win! ")
                    Speak("Scissors beats paper! I win! ")
                    continue
                elif opponenetChoice == 'P' and userChoice.upper() == 'R':
                    print("Paper beat rock, I win!")
                    Speak("Paper beat rock, I win!")
                    continue
                elif opponenetChoice == 'e' or 'E' and userChoice.upper() == 'E':
                    break
                else:
                    print("You won")
                    Speak("You won")
                i = i + 1
        elif 'i love you' in query:
            Speak("i feel sorry for you but, I am loyal to my founders")
        elif 'joke' in query:
            s = pyjokes.get_joke()
            print(s)
            Speak(s)

        #function for news
        elif 'news' in query or 'samachar' in query:
            if 'news' in query:
                Speak("Top articles")
            if 'samachar' in query:
                Speak("aaj ke samachar")
            def NewsFromGoogle():
                main_url = " http://newsapi.org/v2/top-headlines?sources=google-news-in&apiKey=fac108dabb984594a55bb5d0539b1059"
                open_bbc_page = requests.get(main_url).json()
                article = open_bbc_page["articles"]
                results = []

                for ar in article:
                    results.append(ar["title"])
                for i in range(5):
                    time.sleep(1)
                    print(i + 1,results[i])
                    Speak(results[i])
            NewsFromGoogle()
        elif 'end' or 'exit' in query:
            Speak("Thanks for having me in use")
            break
        time.sleep(3)
        Speak("Anything else sir")


