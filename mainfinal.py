import speech_recognition as sr
import webbrowser
import pyttsx3
import datetime
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
from datetime import time
import playsound
from pygame import mixer
import pywhatkit as kit
import warnings
warnings.filterwarnings("ignore")
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import subprocess
import wikipedia
from pynput.keyboard import Key, Controller
import smtplib
import numpy as np
import cv2
PATH = "/Users/mac/Desktop/sr1final auto/chromedriver"

intro= ['introduce yourself','hello', 'tell me who are you', 'hey']
search_unit= ['search', 'browse' ]
current_time= ['what is the time', 'what time it is', 'time', 'time batao']

mixer.init()
engine=pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[7].id)
engine.setProperty('rate', 170)

r=sr.Recognizer()
r.energy_threshold=4000

mixer.music.load('/Users/mac/Desktop/sr1final auto/intro.mp3')
mixer.music.play()
'''def img():
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    cap = cv2.VideoCapture(0)
    cap.set(3,640) # set Width
    cap.set(4,480) # set Height
    while True:
        ret, img = cap.read()
        img = cv2.flip(img, 1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,     
            scaleFactor=1.2,
            minNeighbors=1,     
            minSize=(70, 70)
        )
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]  
        cv2.imshow('video',img)
        k = cv2.waitKey(30) & 0xff
        
        if k == 27: # press 'ESC' to quit
            break
    cap.release()
    cv2.destroyAllWindows()
'''
def switch():
    keyboard = Controller()
    with keyboard.pressed(Key.cmd):
        keyboard.press(Key.tab)
        keyboard.release(Key.tab)
def email():
    se= 'devanshgupta2604@gmail.com'
    pyttsx3.speak("Okay! To whom should I email? Please type the email addrress")
    print("Rick : 'Okay! To whom should I email ?'")
    persone= str(input("Please type the e-mail address : "))
    #re = 'aviagarwal011@gmail.com'
    password = '26aprilkishu'
    pyttsx3.speak("What's the subject sir ?")
    print("Rick : 'What's the subject, sir ?'")
    #message = "this email is ric-generated"
    try:
        with sr.Microphone(device_index=0) as source:
        
            audio_su=r.listen(source)
            r.adjust_for_ambient_noise(source)
            r.dynamic_energy_threshold = True
            subject=r.recognize_google(audio_su)
            subject.lower()
            print("SUBJECT : " + subject)
    except:
        subject = ' '

    pyttsx3.speak("What's the message sir ?")
    print("Rick : 'What's the message, sir ?'")

    try:
        with sr.Microphone(device_index=0) as source:
        
            audio_me=r.listen(source)
            r.adjust_for_ambient_noise(source)
            r.dynamic_energy_threshold = True
            body=r.recognize_google(audio_me)
            body.lower()
            print("MESSAGE : " + body)
    except:
        body = ' '
    msg = f'Subject: {subject}\n\n{body}'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(se, password)
    print("Login succesfful !")
    
    server.sendmail(se, persone, msg)
    print("Email sent !")
    pyttsx3.speak("Email Sent !")

   ## pyttsx3.speak("Sorry couldn't get that !")
   ## print("Rick : 'Sorry, couldn't get that'")
def pause():
    
    '''
    with sr.Microphone(device_index=0) as source:
        
        audio_yt=r.listen(source)
        r.adjust_for_ambient_noise(source)
        r.dynamic_energy_threshold = True
        text_yt=r.recognize_google(audio_yt)
        text_yt.lower()
        
        if text_yt.count("stop")>0:'''
            
    keyboard = Controller()

    
    with keyboard.pressed(Key.cmd):
        keyboard.press('w')
        keyboard.release('w')
def wish():
    hour=int(datetime.datetime.now().hour)
    
    if hour<12:
        print("Good Morning !")
        pyttsx3.speak("Good Morning !")
        

    if hour==12 :
        print("Good Noon !")
        pyttsx3.speak("Good Noon !")
        

    if hour>12 and hour<16:
        print("Good Afternoon !")
        pyttsx3.speak("Good Afternoon !")
        

    if hour==16:
        print("Good Evening !")
        pyttsx3.speak("Good Evening !")
        

    if hour>16:
        print("Good Evening !")
        pyttsx3.speak("Good Evening !")
        

        #print(text)
        
def main():
    if __name__ == '__main__':
        try:
        
            while True:
                
                with sr.Microphone(device_index=0) as source:
                    audio=r.listen(source)
                    r.adjust_for_ambient_noise(source)
                    r.dynamic_energy_threshold = True
                    text=r.recognize_google(audio)
                    text.lower()
                    print(text)

                    queries=['who is', 'tell me about', 'wikipedia', 'tell me something about']
                    
                    try:
                        if text.count("hay rake") > 0:
                            print("You said : 'Hey Rick !'")
                            print("Rick : 'Yes, Sir !'")
                            pyttsx3.speak("yes, sir !")
                            
                            text=r.recognize_google(audio)
                            text.lower()

                        elif text.count("hay Rick") > 0:
                            print("You said : 'Hey Rick !'")
                            print("Rick : 'Yes, Sir !'")
                            pyttsx3.speak("yes, sir !")
                            
                            text=r.recognize_google(audio)
                            text.lower()

                        elif text in ['firak' , 'new bike' , 'yaar ek' , 'Vivek' , 'hirak' , 'hair' , 'hello Rick' , 'Nell,e 1' , 'hello re' , 'hay rate' , 'Hay re' , 'shareit'] :
                            
                            print("You said : 'Hello Rick !'")
                            print("Rick : 'Yes, Sir !'")
                            pyttsx3.speak("yes, sir !")
                            
                            text=r.recognize_google(audio)
                            text.lower()

                        elif text in ['Hello re', 'hello Drake', 'hello Rekha', 'hello rec', 'break', 'error 1', 'hello rape', 'helo rate', 'hey wreck', 'hello wreck']:
                            print("You said : 'Hello Rick !'")
                            print("Rick : 'Yes, Sir !'")
                            pyttsx3.speak("yes, sir !")
                            
                            text=r.recognize_google(audio)
                            text.lower()


                        elif text.count("you") > 0 and text.count("there") > 0:
                            mixer.music.load('intro.mp3')
                            mixer.music.play()
                            print("You said :" + "  " + "'" + text + "'")
                            pyttsx3.speak("Yes I'm here")
                            
                            print("Rick : 'Yes I'm here'")

                        elif text in ['introduce yourself', 'who are you']:
                            print("You said :" + "  " + "'" + text + "'")
                            print("Rick : 'Hey there, My name is Rick and I am programmed by Aarav Sir!'")
                            pyttsx3.speak("hey there, My name is Rick and I am programmed by Aarav Sir!")
                            
                            

                        elif text in ['okay got it', 'okay', 'got it', 'great']:
                            print("You said :" + "  " + "'" + text + "'")
                            pyttsx3.speak("Yeah !")
                            
                            print("Rick : 'Yeah !'")


                        elif text.count("how") > 0 and text.count("you"):
                            print("You said :" + "  " + "'" + text + "'")
                            pyttsx3.speak("I am feeling very helpful !")
                            
                            print("Rick : 'I am feeling very helpful !'")
                            print("Rick : 'What about you, Sir ?'")
                            pyttsx3.speak("What about you, sir?")
                            
                        

                        elif text in ['I am good' , 'I am fine' , 'I am awesome' , 'I am okay' , 'I am great' , 'I am wonderful']:
                            print("You said :" + "  " + "'" + text + "'")
                            pyttsx3.speak("Wow! glad to hear that!")
                            
                            print("Rick : 'Wow! glad to hear that!'")

                        elif text in ['I am bad', 'I am not well', 'I am not fine', 'I am not okay', 'I dont know', 'I do not feel very good']:
                            print("You said :" + "  " + "'" + text + "'")
                            pyttsx3.speak("Oh ! I am sorry for that. Well,in that case, I think songs will be of help")
                            
                            print("Rick : 'Oh ! I am sorry for that. I think songs will help!!'")
                            mixer.music.load('Attention.mp3')
                            mixer.music.play()

                        elif text.count('you can sleep')>0:
                            print("You said :" + "  " + "'" + text + "'")
                            print("Rick : 'Okay! Bye-Bye!'")
                            pyttsx3.speak("Okay! bye-bye !")
                            
                            quit()

                        elif text in ['where are you']:
                            print("You said :" + "  " + "'" + text + "'")
                            pyttsx3.speak("always with you, sir")
                            
                            print("Rick : 'Always with you, Sir!'")

                        elif text in ['hello', 'good morning', 'good afternoon', 'good evening', 'hey']:
                            print("You said :" + "  " + "'" + text + "'")
                            pyttsx3.speak("Hola ! How may I help you ?")
                            
                            print("Rick : 'Hola ! How may I help you ?'")
                            
                        
                        elif text.count( "search") > 0:
                            #search
                            print("You said :" + "  " + "'" + text + "'")
                            pyttsx3.speak("Okay ! These are the results !")
                            
                            print("Rick : 'Okay ! These are the results !'")
                            mixer.music.load('search_music.mp3')
                            mixer.music.play()
                            if "for" in text:
                                search_unit=(text.split("search for")[1])
                                url = 'https://www.google.com/search?q='
                                websearch=url+search_unit
                                webbrowser.open(websearch)
                            elif "for" not in text:
                                search_unit=(text.split("search")[1])
                                url = 'https://www.google.com/search?q='
                                websearch=url+search_unit
                                webbrowser.open(websearch)

                        elif text.count("bye") > 0 or text.count("i am going") > 0 or text.count("go away") > 0:
                            print("You said :" + "  " + "'" + text + "'")
                            pyttsx3.speak("Bye-Bye !")
                            
                            print("Rick : 'Bye-Bye !'")
                            quit()

                        elif text.count("what") > 0 and text.count("doing"):
                            pyttsx3.speak("I'm trying to be the best version of myself ")
                            
                            print("You said :" + "  " + "'" + text + "'")
                            print("Rick : 'I'm trying to be the best version of myself ! :)'")
                       
                        elif text.count("Beatbox") > 0:
                            print("You said :" + "  " + "'" + text + "'")
                            pyttsx3.speak("I've been waiting for you to ask!")
                            print("BEATBOXING...")
                            
                            print("Rick : 'I've been waiting for you to ask ! ;)'")
                            mixer.music.load('beatbox_rick.mp3')
                            mixer.music.play()

                        elif text.count("thanks") > 0 or text.count("thank you")> 0 or text.count("thank")>0:
                            print("You said :'Thanks !'")
                            pyttsx3.speak("always here for your service !")
                            
                            print("Rick : 'Always here for your service ! :)'")


                        elif text.count("play") > 0:
                            song=(text.split("play")[1])
                            print("You said :" + "  " + "'" + text + "'")
                            pyttsx3.speak("playing" + song)
                            
                            print("Rick : 'Playing"+ song + "'")
                            mixer.music.load('search_music.mp3')
                            mixer.music.play()
                            #pause()
                            kit.playonyt(song)

                        
                            #addition
                        elif text.count("+") > 0:
                            
                            #print("calculating..")
                            a=((int(text.split("+")[0])) + (int(text.split("+")[1])))
                            b=str(a)
                            print("You said :" + "  " + "'" + text + "'")
                            print("Rick : 'The answer is " + b +"'")
                            pyttsx3.speak("The answer is " + b)

                        elif text.count("take a note") > 0:
                            time = datetime.datetime.now()
                            ab=str(time)

                            save_path = '/Users/mac/Desktop/sr1final auto/notes'
                            print("You said :" + "  " + "'" + text + "'")
                            pyttsx3.speak("okay, what do you want me to note ?")
                            print("Rick : 'Okay what do you want me to note ?'")
                            print("Noting...")
                            with sr.Microphone(device_index=0) as source:
                                
                                audio1=r.listen(source)
                                r.adjust_for_ambient_noise(source)
                                r.dynamic_energy_threshold = True
                                text1=r.recognize_google(audio1)
                                text1.lower()
                                print("N O T E ----  " + "-->" + text1)
                                
                                completeName = os.path.join(save_path, ab + ".txt")
                                file = open(completeName, "w")
                                file.write(text1)
                                file.close()
                                mixer.music.load('noted.mp3')
                                mixer.music.play()
                                pyttsx3.speak("Note taken !")
                                print("Rick: 'Note taken !'")

                        elif text.count("note") > 0 and text.count("that") > 0:
                            
                            time = datetime.datetime.now()
                            ab=str(time)
                            text_to_save=(text.split("note that")[1])
                            save_path = '/Users/mac/Desktop/sr1final auto/notes'
                            print("You said :" + "  " + "'" + text + "'")
                            completeName = os.path.join(save_path, ab + ".txt")
                            file = open(completeName, "w")
                            file.write(text_to_save)
                            file.close()
                            mixer.music.load('noted.mp3')
                            mixer.music.play()
                            pyttsx3.speak("Note taken !")
                            print("Rick: 'Note taken !'")
                            
                        elif text.count("weather") > 0 or text.count("whether") > 0 or text.count("temperature")>0:
                            print("You said :" + "  " + "'" + text + "'")
                            driver = webdriver.Chrome(PATH)
                            driver.get("https://www.google.com/search?q=what+is+the+weather+right+now&rlz=1C5CHFA_enIN948IN948&sxsrf=ALeKk03-i0yFK_flEEOcGyHPJT0XfslUXA%3A1618518251578&ei=66B4YM7sIpuv9QO3v4ywCg&oq=what+is+the+weather+right+now&gs_lcp=Cgdnd3Mtd2l6EAMyBwgjELADECcyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAEEcQsAMyBwgAELADEENQAFgAYJcUaAFwAngAgAGhAogBoQKSAQMyLTGYAQCqAQdnd3Mtd2l6yAEKwAEB&sclient=gws-wiz&ved=0ahUKEwiOjsqrioHwAhWbV30KHbcfA6YQ4dUDCA4&uact=5")
                            weather_info= driver.find_element(By.ID, 'wob_tm')
                            temp= weather_info.text
                            mixer.music.load('search_music.mp3')
                            mixer.music.play()
                            pyttsx3.speak("The weather in your location right now is" + temp + "degrees celsius")
                            print("Rick : 'The weather in your location right now is " + temp + " degrees celsius")

                        elif text.count("close the window")>0 or text.count("okay close it")>0:
                            pause()

                        elif text in ['shut down', 'shurdown', 'shut down the system', 'shutdown the system']:
                            print("You said :" + "  " + "'" + text + "'")
                            print("Rick : 'Are you sure?'")
                            pyttsx3.speak("Are you sure?")
                            print("say YES or NO...")
                            with sr.Microphone(device_index=0) as source:
                                
                                audio1=r.listen(source)
                                r.adjust_for_ambient_noise(source)
                                r.dynamic_energy_threshold = True
                                text1=r.recognize_google(audio1)
                                text1.lower()

                                if text1.count("yes") > 0:
                                    print("You said : '" + text1 + "'")
                                    pyttsx3.speak("The system is shutting down !")
                                    print("Rick : 'The system is shutting down.'")
                                    
                                    subprocess.call(['osascript', '-e',
                                    'tell app "System Events" to shut down'])
                                    
                                elif text1.count("no") > 0:
                                    print("Okay, not shutting down the system")
                                    pyttsx3.speak("Okay, not shutting down the system")
                                else:
                                    print("Okay, not shutting down the system")
                                    pyttsx3.speak("Okay, not shutting down the system")

                        elif text.count("open") > 0:
                            try:
                                
                                open_app = (text.split("open")[1])
                                keyboard = Controller()
                                with keyboard.pressed(Key.cmd):
                                    
                                    keyboard.press(Key.space)
                                    keyboard.release(Key.space)
                                time.sleep(3)
                                keyboard.type(open_app)
                                time.sleep(2)
                                keyboard.press(Key.enter)
                                keyboard.release(Key.enter)
                                time.sleep(13)
                            except:
                                pyttsx3.speak("Sorry couldn't find an app with this name")

                        elif 'time' in text:
                            time=datetime.datetime.now().strftime('%I:%M %p')
                            print("You said : '" + text + "'")
                            print("Rick : The time right now is " + time)
                            pyttsx3.speak("The time right now is " + time)

                        
                        elif text.count("email") > 0:
                             email()
                                    
                        elif text.count("who")>0 and text.count("is")>0:
                            question=(text.split("is")[1])
                            print("You said : '" + text + "'")

                            try:
                            
                                info = wikipedia.summary(question, 2)
                                print("Rick : " + info)
                                pyttsx3.speak(info)
                                '''
                                driver = webdriver.Chrome(PATH)
                                linkwiki=('https://en.wikipedia.org/wiki/'+question)
                                driver.get(linkwiki)
                                
                                inputbox= driver.find_element(By.ID, 'searchInput').send_keys(question)
                                btns= driver.find_element(By.CLASS_NAME, 'suggestion-title')
                                btns.click()'''

                            except wikipedia.exceptions.PageError as e:
                                if "does not match any pages" in str(e):
                                    print("Rick : 'Sorry, I didn't get that! Can you please be more specific?")
                                    pyttsx3.speak("Sorry, I didn't get that! Can you please be more specific?")

                        elif text.count("tell me something about")>0:
                            question=(text.split("about")[1])
                            print("You said : '" + text + "'")

                            try:
                            
                                info = wikipedia.summary(question, 2)
                                print("Rick : " + info)
                                pyttsx3.speak(info)
                                '''
                                driver = webdriver.Chrome(PATH)
                                linkwiki=('https://en.wikipedia.org/wiki/'+question)
                                driver.get(linkwiki)
                                
                                inputbox= driver.find_element(By.ID, 'searchInput').send_keys(question)
                                btns= driver.find_element(By.CLASS_NAME, 'suggestion-title')
                                btns.click()'''

                            except wikipedia.exceptions.PageError as e:
                                if "does not match any pages" in str(e):
                                    print("Rick : 'Sorry, I didn't get that! Can you please be more specific?")
                                    pyttsx3.speak("Sorry, I didn't get that! Can you please be more specific?")

                        elif text.count("call")>0:
                            
                            personc= (text.split("call")[1])
                            keyboard = Controller()
                            with keyboard.pressed(Key.cmd):
                                keyboard.press(Key.space)
                                keyboard.release(Key.space)
                            time.sleep(3)
                            keyboard.type("Whatsapp")
                            time.sleep(2)
                            keyboard.press(Key.enter)
                            keyboard.release(Key.enter)
                            time.sleep(13)
                            
                            with keyboard.pressed(Key.cmd):
                                keyboard.press('f')
                                keyboard.release('f')
                            time.sleep(3)
                            keyboard.type(personc)
                            keyboard.press(Key.enter)
                            time.sleep(2)
                            keyboard.press(Key.tab)
                            keyboard.press(Key.tab)
                            keyboard.press(Key.tab)
                            keyboard.press(Key.enter)

                        elif text.count("bombing protocol")>0:
                            
                            print("You said : 'Start bombing protocol'")
                            pyttsx3.speak("Starting bombing protocol, sir!")
                            mixer.music.load('search_music.mp3')
                            mixer.music.play()
                            print("Rick : 'Starting bombing protocol, sir!'")
                            import bombing

                        elif text.count("switch")> 0 and text.count("window")>0:
                            switch()
                        
                        elif text.count("Alexa")>0 or text.count("Google")>0 or text.count("Siri")>0 or text.count("Cortana")>0 or text.count("bixby")>0:
                            pyttsx3.speak("Yes she's always been my good friend !")
                            print("Rick : 'Yes. She's always been my good friend !' ")

                        elif text.count("say")>0 and text.count("hi")>0:
                            pyttsx3.speak("Hello there! My name is Rick and I am a personal assisstant!")
                            print("Hello there! My name is Rick and I am a personal assisstant!")

                        elif text.count("lyrics")>0:
                            songsplit= (text.split("of")[1])
                            songna= ("lyrics of" + songsplit)
                            url = 'https://www.google.com/search?q='
                            print("You said : 'what are the lyrics of " + songsplit + "'")
                            print("Rick : 'these are the lyrics of " + songsplit + "'")
                            pyttsx3.speak("these are the lyrics of " + songsplit)
                            mixer.music.load('search_music.mp3')
                            mixer.music.play()
                            
                            websearch=url+songna
                            webbrowser.open(websearch)
                            
                            
                    except sr.UnknownValueError:
                        print("~")
                        
        except sr.UnknownValueError:
                        print("~")
                        main()


                       
wish()
main()
                        

                    

           
