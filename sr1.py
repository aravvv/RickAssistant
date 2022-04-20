import speech_recognition as sr
import webbrowser
import pyttsx3
import datetime
import os
from datetime import time
from playsound import playsound

intro= ['introduce yourself','hello', 'tell me who are you', 'hey']
search_unit= ['search', 'browse' ]
current_time= ['what is the time', 'what time it is', 'time', 'time batao']

WAKE='hey rick'
if __name__ == '__main__':
    
    engine=pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 200)
    ghnta=int(datetime.datetime.now().hour)
    
    if ghnta<12:
        engine.say("Good Morning !")
        engine.runAndWait() 

    if ghnta==12 :
        engine.say("Good Noon !")
        engine.runAndWait()

    if ghnta>12 and ghnta<16:
        engine.say("Good Afternoon !")
        engine.runAndWait()

    if ghnta==16:
        engine.say("Good Evening !")
        engine.runAndWait()

    if ghnta>16:
        engine.say("Good Evening !")
        engine.runAndWait()
        

    engine.say("What can I do for you? Speak?")
    engine.runAndWait()
    print("I'm listening...")

    r=sr.Recognizer()


    r.energy_threshold=600

    
    with sr.Microphone(device_index=0) as source:
        audio=r.listen(source)
        text=r.recognize_google(audio)
        text.lower()
        
        try:
            
            if text in intro:
                engine.say("hey there, My name is Rick and I am programmed by Aarav Sir!")
                engine.runAndWait()
                print("Hi there, My name is Rick and I am programmed by Aarav Sir!")

            elif text in current_time:
                hour=int(datetime.datetime.now().hour)
                minute=int(datetime.datetime.now().minute)
                second=int(datetime.datetime.now().second)
                engine.say("Right now, the time is")
                engine.runAndWait()
                engine.say(hour + minute)
                engine.runAndWait()
                #engine.say(minute)
                #engine.runAndWait()
                if hour<12 and hour==24:
                    engine.say("A.M")
                    engine.runAndWait()
                if hour>12 and hour==12:
                    engine.say("P.M")
                    engine.runAndWait()
                
                
            elif text.count( "search") > 0:
                engine.say("Yes! what do you want me to search for?")
                engine.runAndWait()
                print("Yes! what do you want me to search for?")
                print("Speak! I'm all ears...")
                with sr.Microphone() as source:
                    audio=r.listen(source)

                    try:
                        
            
                        search_for=r.recognize_google(audio)

                        print("Okay! I will search for", search_for, "on Google")
                        engine.say("Okay! I will search for")
                        engine.runAndWait()
                        engine.say(search_for + "on google")
                        engine.runAndWait()
                        url='https://www.google.com/search?q='
                        search_url=url+search_for
                        webbrowser.open(search_url)

                    except:
                        
                        print("Can't recognise")
                        engine.say("Can't recognise")
                        engine.runAndWait()

            elif text in ['how are you', 'how you doing', 'how do you do']:
                engine.say("I am feeling very helpful !")
                engine.runAndWait()
                print("I am feeling very helpful !")
                engine.say("What about you, sir?")
                engine.runAndWait()
                with sr.Microphone() as source:
                    audio=r.listen(source)

                    try:
                        
            
                        reply_to_halchal=r.recognize_google(audio)

                        if reply_to_halchal in ['I am good', 'I am fine', 'I am awesome', 'I am okay', 'I am great', 'I am wonderful']:
                            engine.say("Wow! glad to hear that!")
                            engine.runAndWait()
                            print("Wow! glad to hear that!")

                        if reply_to_halchal in ['I am bad', 'I am not well', 'I am not fine', 'I am not okay', 'I dont know', 'I do not feel very good']:

                            engine.say("Oh ! I am sorry for that. Well,in that case, I think songs will be of help")
                            engine.runAndWait()
                            print("Oh ! I am sorry for that. I think songs will help!!")
                            playsound('Attention.mp3')
                            

                    except:
                        engine.say("Can't recognise")
                        engine.runAndWait()
                        print("Can't recognise")

            elif text in ['play a song', 'I want to hear a song']:
                engine.say("Ok! Playing a song")
                engine.runAndWait()
                print("Ok! Playing a song")
                playsound('Attention.mp3')

            elif text in ['khana bana lete ho', 'khana banao']:
                print("You just asked", text)
                engine.say("Yes! What do you want to eat? You must be hungry as hell!!")
                print("Yes! What do you want to eat? You must be hungry as hell!!")
                engine.runAndWait()
                with sr.Microphone() as source:
                    audio=r.listen(source)
                    print("I'm listening... \n .\n .\n .\n")

                    try:
                        
            
                        khana_item=r.recognize_google(audio)
                        if khana_item in ['shahi paneer','pizza']:
                            print("you said", khana_item,"\n .\n .\n .\n")
                            
                            engine.say("Sir, how can you be so foolish! I was just kidding! After all you have created me. so I just adapted some of your sense of humour, hehe!")
                            engine.runAndWait()
                            print("Sir, how can you be so foolish! I was just kidding! After all you have created me. so I just adapted some of your sense of humour, hehe!")

                    except:

                        engine.say("Can't recognise")
                        engine.runAndWait()
                        print("Can't recognise")
                

        except:
            print("Can't recognise")
            engine.say("Can't recognise")
            engine.runAndWait()

    
    
    
