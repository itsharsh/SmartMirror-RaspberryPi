import cv2
import csv
import os
import sys
import time
import json
import locale
import requests
import threading
import traceback
import matplotlib
import speech_recognition as sr
import subprocess
import Main


from subprocess import call
from tkinter import *
from io import BytesIO
from PIL import Image, ImageTk
from contextlib import contextmanager
from matplotlib import style
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from time import strftime
from gtts import gTTS
from pygame import mixer
from subprocess import call
from Main import *

dbpath = "data/db.csv"
loginpath = "data/loginstatus.csv"


class FullscreenWindow:
    
    def __init__(self):
        self.tk = Tk()
        self.tk.configure(background='black')
        self.tk.attributes("-fullscreen", True)
        self.Frame = Frame(self.tk, background = 'black')
        self.Frame.pack(anchor='center')

        self.state = False
        self.tk.bind("<Return>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)
        
        self.screensaver = ScreenSaver(self.Frame)
        self.screensaver.pack(anchor = 'center')

    def toggle_fullscreen(self, event=None):
        self.state = not self.state  #Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"

class VoiceAssistant:
    
    def __init__(self):
        pass    
        
    def talkToMe(self, audio):
        self.filename='audio.mp3'
        print(audio)
        self.tts = gTTS(text=audio, lang='en')
        self.tts.save(self.filename)
        mixer.init()
        mixer.music.load(self.filename)
        mixer.music.play()

    def myCommand(self):
        self.r=sr.Recognizer()
        with sr.Microphone() as source:
            print('Listening ')
            self.r.pause_threshold = 1
            self.r.adjust_for_ambient_noise(source, duration = 1)
            self.audio = self.r.listen(source)
            
        try:
            self.command = self.r.recognize_google(self.audio)        
              
        except sr.UnknownValueError:
            self.assistant(self.myCommand())
            
        except Exception as e:
            print(e)
            self.talkToMe('Got Error' + e)
            
        else:
            print('You said: '+ self.command + '\n')
            return self.command



                
class ScreenSaver(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent, bg='black')
        self.string = ''
        self.lbl = Label(self, font=('Helvetica', 40), fg="white", bg="black")
        self.lbl.pack()
        self.msg = Label(self, font=('Helvetica', 20), fg="white", bg="black")
        self.msg.pack()
        self.time()
        self.after(100,self.recognize)
        self.after(5000,self.kill)
        
    def time(self):
        self.string=strftime('%H:%M:%S')
        self.lbl.config(text=self.string)
        self.lbl.after(1000,self.time)

    def recognize(self):
        faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        video_capture = cv2.VideoCapture(0)	

        rec = cv2.face.LBPHFaceRecognizer_create()
        rec.read("recognizer/trainingData.yml")
        id=0
        
        loopcheck=True
        
        while loopcheck:
            ret, frame = video_capture.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30, 30),flags=cv2.CASCADE_SCALE_IMAGE)

            for (x, y, w, h) in faces:
                id,conf=rec.predict(gray[y:y+h,x:x+w])

                with open(dbpath,'r') as f:
                    reader=csv.reader(f, delimiter=',')

                    for ids in reader:
                        face_id=ids[0]    
                        if (face_id == str(id)):
                            email = ids[1]
                            name = ids[2]

                            with open (loginpath,'w') as f2:
                                writer = csv.writer(f2)
                                writer.writerow([id,email,name])
                                f2.close()

                if(conf<60):
                    
                    print ("Face Matched "+str(id))
                    loopcheck=False
                    self.talkToMe(text='Welcome to your SmartMirror '+str(name)+" ("+str(email)+")")
                    Main.main()
                    

    def kill(self):
        exit()
        


if __name__ == '__main__':
    FullscreenWindow().tk.mainloop
    
    
