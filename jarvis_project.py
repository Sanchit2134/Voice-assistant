from sys import path
import pyttsx3 
import datetime
import speech_recognition as sr #  speech_recognition as sr it convert audio voice into string
import wikipedia
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')  # api - microsoft provide this property (which is in build ) 
voices = engine.getProperty('voices')   # In this line we get the voice 
engine.setProperty('voice',voices[0].id)  #In thisline we select the voice 

def speak(audio):
  engine.say(audio)
  engine.runAndWait()


def wishMe():
  hour = int(datetime.datetime.now().hour)
  if hour>=0 and hour<12:
    speak("Good Morning")
    speak("I am a jarvis how can I help you ")

  elif hour>=12 and 12<18:
    speak("Good afternoon")
    speak("I am a jarvis how can I help you ")

  else:
    speak("Good Evening")  
    speak("I am a jarvis how can I help you ")
  

def TakeCommand():
  #It takes microphone input from the user and returns string output

  r = sr.Recognizer() #Ye class hme help krte hai audio sunneme
  with sr.Microphone() as source:
    print("Listing...")
    r.pause_threshold = 1   #seconds of non-speaking audio before a phrase 
    audio = r.listen(source)

  try:   # try hmm tb likte hai jb hme lgta hai ki koi error aa skta hai
    print("Recognizing...")
    query = r.recognize_google(audio, language='en-in')
    print(f"user said: {query}\n")

  except Exception as e:
    print(e)
    print("Say that again please...")
    return "None"   #None string hai agr jarvis ko kuch pta nahi chla than wo None return kre ga
  return query

def sendEmail(to,content):
  server = smtplib.SMTP('smntp.gmail.com',587)
  server.starttls()
  server.login('youremail@gmail.com','yourpassword')
  server.sendmail('youremail@gmail.com',to,content)
  server.close()

if __name__ == "__main__":
  # speak("sale is going on")
  wishMe()
  # TakeCommand()

  while True:
    query = TakeCommand().lower()

  # logic for executing tasksbased on query
  if 'wikipedia' in query :
    speak('Searching Wikipedia...')
    query = query.replace('Wikipedia',"")
    result = wikipedia.summary(query,sentences=2)
    speak("According to wikipedia")
    print(result)
    speak(result)
  
  elif 'open Youtube' in query:
    webbrowser.open("youtube.com")

  elif 'open google' in query:
    webbrowser.open("google.com")

  elif 'open stackoverflow' in query:
    webbrowser.open("stackoverflow.com")

  elif 'open music' in query:
    music_dir = music
    song = os.listdir(music_dir)
    print(song)
    os.startfile(os.path.join(music_dir,songs[0]))

  elif 'the time' in query:
      strTime = datetime.datetime.now().strftime("%H:%M:%S")
      speak(f"Sir,the time is{strtime}")

  elif 'open code' in query:
    path = "C:\\Users\\jarvu\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(codepath)

  elif 'email to harry ' in query:
    try:
      speak("What should I say?")
      content = TakeCommand()
      to = "harryEmail@gmail.com"
      sentEmail(to,content)
      speak("Email has been sent!")
      
    except Exception as e:
      print(e)
      speak('Sorry not able to send this email')  