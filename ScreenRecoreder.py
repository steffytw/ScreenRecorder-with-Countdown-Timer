#!/usr/bin/env python
import pyautogui
import time
from tkinter import *
import threading
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from tkinter import messagebox
import os

window=Tk()
window.geometry("650x500")
window.title("Screen Recorder")
window.configure(background="")

# Declaration of variables 
hour=StringVar() 
minute=StringVar() 
second=StringVar() 

# setting the default value as 0 
hour.set("00") 
minute.set("00") 
second.set("00") 



class Screenshot():

    def __init__(self,master):

        self.ctlabel=Label(master,text="Enter Timer input in Hr/Min/Sec ",font="times 10 bold", fg="Black",  bd=4, bg="White",)
        self.ctlabel.place(x=80,y=100)
        self.hourEntry= Entry(master, width=2,font=("Arial",18,""), 
                        textvariable=hour) 
        self.hourEntry.place(x=360,y=100) 

        self.minuteEntry= Entry(master, width=2,font=("Arial",18,""), 
                        textvariable=minute) 
        self.minuteEntry.place(x=410,y=100) 

        self.secondEntry= Entry(master, width=2,font=("Arial",18,""), 
                        textvariable=second) 
        self.secondEntry.place(x=460,y=100)

        self.lb1=Label(master,text="Enter Time interval in Seconds",font="times 10 bold", fg="Black",  bd=4, bg="White",)
        self.lb1.place(x=80,y=200)
        self.e1=Entry(master,width=30)
        self.e1.place(x=350,y=200)

        self.bt1=Button(master, text="Start",width=42, fg="Black", padx=5, pady=5,  bd=4, bg="Light green",command = self.threadFun)
        self.bt1.place(x=180,y=300)
        
    
    
    def takeScreenshot (self):
        self.s = self.e1.get()
        self.val=1*int(self.s)
        x=1
        while True:
            pyautogui.screenshot('/home/steffy/Desktop/ScreenRecorder/images/image'+str(x)+'.png')
            x+=1
            time.sleep(self.val)
            print(self.temp)
            if (self.temp == 0): 
                break
        
    def submit(self): 
        try: 
            # the input provided by the user is 
            # stored in here :temp 
            self.temp = int(hour.get())**3600 + int(minute.get())*60 + int(second.get()) 
        except: 
            print("Please input the right value") 
        while self.temp >-1: 
            
            # divmod(firstvalue = temp//60, secondvalue = temp%60) 
            self.mins,self.secs = divmod(self.temp,60) 

            # Converting the input entered in mins or secs to hours, 
            # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr : 
            # 50min: 0sec) 
            self.hours=0
            if self.mins >60: 
                
                # divmod(firstvalue = temp//60, secondvalue 
                # = temp%60) 
                self.hours, self.mins = divmod(self.mins, 60) 
            
            # using format () method to store the value up to 
            # two decimal places 
            hour.set("{0:2d}".format(self.hours)) 
            minute.set("{0:2d}".format(self.mins)) 
            second.set("{0:2d}".format(self.secs)) 

            # updating the GUI window after decrementing the 
            # temp value every time 
            window.update() 
            time.sleep(1) 

            # when temp value = 0; then a messagebox pop's up 
            # with a message:"Time's up" 
            if (self.temp == 0): 
                messagebox.showinfo("Time Countdown", "Time's up ") 
            
            # after every one sec the value of temp will be decremented 
            # by one
            self.temp -= 1
    def threadFun(self):
        self.thread1 = threading.Thread(target=self.submit)
        self.thread1.start()

        self.thread2 = threading.Thread(target=self.takeScreenshot)
        self.thread2.start()

    

shot =Screenshot(window)



window.mainloop()
