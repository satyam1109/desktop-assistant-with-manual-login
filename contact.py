from googletrans import Translator
from tkinter import*
from tkinter.ttk import *
from tkinter import messagebox
import mysql.connector
import sys
import pyttsx3
import datetime
from datetime import date
from datetime import time
import pywhatkit
import geocoder
from geopy.geocoders import Nominatim
import wikipedia
import webbrowser
import subprocess
import speech_recognition as sr
import sys
import pyautogui
import os
from ecapture import ecapture as ec
import screen_brightness_control as sbc
import requests


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)  # voices[0] is used for male voice


root = Tk()
root.title("Contact Information")
root.maxsize(1150,650)


def speak(audio):
    engine.say(audio)  # This function will convert the text to speech ("audio" is the input from the user)
    engine.runAndWait()  # This function will make the speech audible in the system, if you don't write this command then the speech will not be audible to you.
    print(audio)
 
     
def gif():
    import tkinter as tk
    from PIL import Image, ImageTk

    class GIFPlayer(tk.Label):
        def __init__(self, master=None, filename='robo3.gif'):
            super().__init__(master)
            self.master = master
            self.filename = 'robo3.gif'
            self.load_gif()
    
        def load_gif(self):
             # Load GIF file
            self.gif = Image.open(self.filename)
            self.frames = []
            try:
                while True:
                    self.frames.append(self.gif.copy())
                    self.gif.seek(len(self.frames))
            except EOFError:
                pass
        
           # Set initial frame
            self.current_frame = 0
            self.set_frame()
    
        def set_frame(self):
            # Update label with current frame
            frame_image = self.frames[self.current_frame]
            self.image = ImageTk.PhotoImage(frame_image)
            self.configure(image=self.image)
        
           # Move to next frame
            self.current_frame += 1
            if self.current_frame == len(self.frames):
                self.current_frame = 0
        
        # Call this method again after a delay to update the GIF
            self.after(50, self.set_frame)

    # Create root window and GIFPlayer widget
    mroot = tk.Tk()
    gif_player = GIFPlayer(master=root, filename="robo3.gif")

    # Start GUI main loop
    gif_player.pack()
    gif_player.mainloop()  


def takeCommand():  # take input from the user microphone and converts the audio into "string"


    r = sr.Recognizer()  # the recogniser class will help us to recognise the audio
    with sr.Microphone() as source:
        print("Listening....")
        #gif()
        r.pause_threshold = 1  # we have kept the pause_threshold or be "1" so that
        # whie speaking if i am taking the pause for 1 sec. the program should not end taking the voice input
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        query = query.lower()
        print("you said ", query)

    except Exception as e:

        speak("Say that again, please....")
        return "None"
    
    return query




def time():
    hour = int(datetime.datetime.now().hour)
    min = int(datetime.datetime.now().minute)

    if hour > 0 and hour <= 12:
        speak(hour)
        speak(min)
    
    elif hour >12:
        
        speak(hour - 12)
        speak(min)

def opengoogle():

    speak("what you want me to search for you")
    query = takeCommand()
    speak("searching on google")
    query = query.replace("search", "")
    query=query.replace("who is","")
    query=query.replace("what is","")
    query=query.replace("how to","")
    query=query.replace("who is","")
    query=query.replace("what do you mean by","")

    pywhatkit.search(query)
    try:
        result = wikipedia.summary(query, sentences=2)
        speak(result)
    except:
        speak("sorry, please try again")

def youtube():
    
    speak("what you want to see on youtube")
    query=takeCommand()
    speak("i found this on youtube")
    pywhatkit.playonyt(query)

def movies():

    speak("which movie you want me to play for you")
    query = takeCommand()

    try:
        if 'abc' in query:
            pw = r"C:\Users\satya\Desktop\movies\intresteler.mp4"
            os.startfile(pw)
    except:
        speak("movie not found, please try again")

def music():

    speak("which song you want me to play for you")
    query = takeCommand()

    try:
        if 'old songs' in query:
            pw = r"C:\Users\satya\Desktop\movies\music\old.mp3"
            os.startfile(pw)
    except:
        speak("song not found, ple4ase try again")

def weather():
    g = geocoder.ip('me')
    latitude, longitude = g.latlng
    lat=str(latitude)
    lon=str(longitude)

    api_key = "8886683047d53510ea0cead388ee87db"

    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "lat=" + lat + "&lon=" + lon + "&appid=" + api_key

    response = requests.get(complete_url)
    # Convert the response to JSON format
    weather_data = response.json()

    # Extract relevant weather information from the JSON data
    temp = str(round(weather_data["main"]["temp"] - 273.15, 2))
    desc =str(weather_data["weather"][0]["description"].title())
    humidity = str(weather_data["main"]["humidity"])
    wind_speed = str(weather_data["wind"]["speed"])

    speak("todays temperature is "+temp+" degree selsius")
    speak("with , "+desc)
    speak("and , Humidity"+humidity+" percent")
    speak(" and , wind speed"+wind_speed+"meter per second")

def files():
    f=open('new2.txt','w')
    f.write("satyam")
    speak("file is creayed")

def translation():
    speak("Ok sir, What do you want to translate")
    msg=takeCommand()
    speak("In which language you want to translate")
    lang=takeCommand()
    translator=Translator()

    speak("translation is  , ")

    if 'german' in lang:
        txt=translator.translate(msg,dest='de') 
        speak(txt.text)
        print(txt.text)

    elif 'french' in lang:
        txt=translator.translate(msg,dest='fr') 
        speak(txt.text)
        print(txt.text)
    
    elif 'spanish' in lang:
        txt=translator.translate(msg,dest='es') 
        speak(txt.text)
        print(txt.text)
    
    elif 'portugese' in lang:
        txt=translator.translate(msg,dest='pt') 
        speak(txt.text)
        print(txt.text)

    elif 'italian' in lang:
        txt=translator.translate(msg,dest='it') 
        speak(txt.text)
        print(txt.text)
    
    elif 'sutch' in lang:
        txt=translator.translate(msg,dest='nl') 
        speak(txt.text)
        print(txt.text)
    
    elif 'swedish' in lang:
        txt=translator.translate(msg,dest='sw') 
        speak(txt.text)
        print(txt.text)
    
    elif 'indonesian' in lang:
        txt=translator.translate(msg,dest='id') 
        speak(txt.text)
        print(txt.text)
    
    elif 'icelandic' in lang:
        txt=translator.translate(msg,dest='is') 
        speak(txt.text)
        print(txt.text)
    
    elif 'english' in lang:
        txt=translator.translate(msg,dest='en') 
        speak(txt.text)
        print(txt.text)  


def tasks():
    while True:
        query = takeCommand()
        if 'sam' in query:
            speak("yes sir")

        if 'tell me about you' in query:
            speak(" My name is sam, I am a virtual assistance, developed by Satyam")

        if 'how are you' in query:
            speak("I am good sir,  what about you")
        
        if 'wikipedia' in query:

            try:
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                speak("According to wikipedia,")
                speak(result)
                print(result)
            except:
                speak("sorry did not get this , please speak again")

        if 'open youtube' in query:
            youtube()
  
        if 'open google' in query:
            opengoogle()

        if 'open instagram' in query:

            webbrowser.open("https://www.instagram.com")
            speak("opening instagram")
        
        if 'open flipkart' in query:

            webbrowser.open("https://www.flipkart.com")
            speak("opening flipkart")

        

        if 'time' in query:
            time()
        
        if 'date' in query:
            today = date.today()
            day = today.day
            month = today.month
            year = today.year
            speak("today date is ")
            speak(day)
            speak(month)
            speak(year)

        if 'open downloads file' in query:
            os.startfile('C:\\Users\\satya\\Downloads')
            speak("on your screen sir")
        
        if 'open desktop file' in query:
            os.startfile('C:\\Users\\satya\\Desktop')
            speak("on your screen sir")

        
        
        if 'open dev c++' in query:
            
            subprocess.call(r"C:\Program Files (x86)\Dev-Cpp\devcpp.exe")
            speak("on your screen sir")
        
        if 'open vscode' in query:
            subprocess.call(r"C:\Users\satya\AppData\Local\Programs\Microsoft VS Code\Code.exe")
            speak("on your screen sir")
        
        if 'open powerpoint' in query:
            pw = r"C:\Users\satya\PycharmProjects\jarvis\Presentation2.pptx"
            os.startfile(pw)
            speak("on your screen sir")
        
        if 'open notepad' in query:
            pw = r"C:\Users\satya\PycharmProjects\jarvis\note.txt"
            os.startfile(pw)
        


        if 'play movies' in query:

            movies()


        if 'increase the volume' in query:
            pyautogui.press("volumeup")
            speak("volume increased")

        if 'decrease the volume' in query:
            pyautogui.press("volumedown")
            speak("volume decreased")

        if 'mute the volume' in query:
            pyautogui.press("volumemute")
            speak("volume muted")


        if 'the brightness' in query:
            try:
                query=query.replace("change the brightness to","")
                query=query.replace("set the brightness to","")
                sbc.fade_brightness(query)
            except:
                speak("sorry please give the measurement again")
        
        if 'my current location' in query or 'where am i' in query:
            g = geocoder.ip('me')
            latitude, longitude = g.latlng


            geolocator = Nominatim(user_agent="my_application") 
            location = geolocator.reverse(str(latitude) + ", " + str(longitude))


            a=(location.raw['address']['state_district'])
            b=(location.raw['address']['state'])
            speak("sir, your current location is ")
            speak(a)
            speak(b)
            speak("with latitude")
            speak(latitude)
            speak("and longitude")
            speak(longitude)


        if 'weather today' in query:
             weather()
            


        
        if 'cerate a note' in query or 'make a notepad file' in query or 'create a notepad file' in query:

            files()
        
        if 'play songs' in query or 'play music' in query:
             music()
        
        if 'click a photo' in query or 'camera' in query:
             ec.capture(0, "Camera ", "image.jpg")
        
        if 'open translator' in query or 'open language translator' in query:
             translation()
                 





#function to close login window
def logclose():
	log.destroy()

#function to check login details in database
def login_check():
	if num.get()=="" or passwd.get()=="":
		messagebox.showwarning("Warning","Please enter the details")
	else:
		mycon = mysql.connector.connect(host="localhost",user="root",passwd="Devil1@!",database="practise2")
		crsr=mycon.cursor()
		sql = "select * from member where mobile = %s and passwd=%s"
		crsr.execute(sql,[(num.get()),(passwd.get())])
		results = crsr.fetchall()
                
		if results:
                     
                     speak("Welcome sir , i am jarvis your desktop assistant , Please tell me how can i help you ")
                     tasks()

        


                     


#function for login page

def login():
	global log
	log = Tk()
	log.title("Login")
	log.maxsize(1150,650)
	#global variable to store values from entry box
	global num
	global passwd

	passwd = StringVar()
	num = IntVar()

	#label for heading
	L1 = Label(log, text=" Login Page",font=("Helvetica 35 bold"))
	L1.place(x= 290,y=190)

	#labels for number and password
	L2 = Label(log, text="Number :",font=("25")).place(x=300,y=300)
	L3 = Label(log, text="Password :" ,font=("25")).place(x=300,y=350)

	#entry box to write information by user 
	Entry(log, textvariable=num).place(x=420,y=303)
	Entry(log, textvariable=passwd).place(x=420,y=353)

	#buttons to login and cancel the page
	Button(log, text="Cancel" , command=logclose).place(x=330,y=420)
	Button(log, text="Login" ,command=login_check).place(x=430,y=420)
	log.mainloop()

#function to close root window
def quit():
        root.destroy()

#function to store data in our database
def storedata():
	if  fname.get() == "" or lname.get() == "" or radio.get() == "" or email.get() == "" or number.get() == "" or passwd.get() == "" or address.get() =="":
		messagebox.showinfo("Info", "Please fill all the fields first.")
	elif len(str(number.get())) >10: 
		messagebox.showwarning("Warning","Please enter valid number")
	elif len(str(number.get())) <10 :
		messagebox.showwarning("Warning","Please enter valid number")

	else:
		mycon = mysql.connector.connect(host="localhost",user="root",password="Devil1@!",database="practise2")
		crsr=mycon.cursor()
		sql = "select * from member where mobile = %s"
		crsr.execute(sql,[(number.get())])
		results = crsr.fetchall()
		if results:
			messagebox.showinfo("Information","This number already registered")
		else:
			crsr.execute(" insert into member values('%s','%s','%s','%s','%s','%s','%s')" %(fname.get(),lname.get(),radio.get(),email.get(),number.get(),passwd.get(),address.get()))
			crsr.close()
			mycon.commit()
			mycon.close()
			messagebox.showinfo("Information","Data saved")
			close()
    

#register window
def register():
	#mycon = mysql.connector.connect(host="localhost",user="root",password="@ryaN2101",database="data")
	#crsr=mycon.cursor()
	#crsr.execute(''' CREATE TABLE if not exists members (Fname text, Lname text,Gender integer(2),Email varchar(255), Mobile bigint(225),password varchar(255),Address varchar(255))''')
	#crsr.close()
	#mycon.commit()
	#mycon.close()
	global top
	top = Tk()
	top.title("Register")
	top.maxsize(1150,650)

	#variables to store values of entry
	global fname
	global lname
	global radio
	global email
	global number
	global passwd
	global address

	fname =StringVar()
	lname =StringVar()
	radio =IntVar()
	email =StringVar()
	number =IntVar()
	passwd =StringVar()
	address =StringVar()

	#label for heading
	Label(top,text="Sign Up Page",font="Helvetica 35 bold").place(x=350,y=50)
	#labels nd entry for details
	Label(top, text="Firstname :",font="Helvetica 18").place(x=100,y=150)
	Entry(top,textvariable=fname).place(x=250,y=155)

	Label(top, text="Lastname :",font="Helvetica 18").place(x=100,y=200)
	Entry(top,textvariable=lname).place(x=250,y=205)

	Label(top, text="Gender :",font="Helvetica 18").place(x=100,y=250)
	
	#radio button for gender
	Radiobutton(top, text = "Male", variable = radio,value = 1).place(x=250,y=255)
	Radiobutton(top, text = "Female", variable = radio,value = 2).place(x=310,y=255)

	Label(top, text="Email :",font="Helvetica 18").place(x=100,y=300)
	Entry(top,textvariable=email).place(x=250,y=305)

	Label(top, text="Mobile No. :",font="Helvetica 18").place(x=100,y=350)
	Entry(top,textvariable=number).place(x=250,y=355)

	Label(top, text="Password :",font="Helvetica 18").place(x=100,y=400)
	Entry(top,textvariable=passwd,show="*").place(x=250,y=405)

	Label(top, text="Address :",font="Helvetica 18").place(x=100,y=450)
	Entry(top,textvariable=address).place(x=250,y=455)

	#button for cancel and submit the details
	Button(top, text="Close", command=close).place(x=140,y=520)
	Button(top, text="Submit",command=storedata).place(x=240,y=520)

	


	top.mainloop()
#function to close top window means register window
def close():
	top.destroy()
        

   
#label for heading          
L1 = Label(root, text=" Welcome To Interface",font=("Helvetica 35 bold"))
L1.place(x= 290,y=190)
#label for image


#label for text below the image
L3= Label(root,text="Management System", font=("Helvetica 16")).place(x=450,y=340)

#button to add new data
btn1 = Button(root, text= "Register", command=lambda:[quit(),register()])
btn1.place(x=400,y=400)

#button to cancel or end the root window
btn2 = Button(root, text="Close", command=quit)
btn2.place(x=500,y=400)
#button to login for already registered members
btn3 = Button(root, text="Login",command=lambda:[quit(),login()]).place(x=600,y=400)
root.mainloop()