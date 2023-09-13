import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import random
import pytz 
from datetime import datetime
import time

#Title and others
window = tk.Tk()
window.geometry('800x400')
window.resizable(False, False)
window.attributes('-alpha', 0.9)
#window.attributes('-fullscreen', True)
window.configure(bg='#DFD8D8')
#Pictures
click_menu = PhotoImage(file='New game/menu.png')
menu_okay = Image.open("New game/menu.png",)
resized = menu_okay.resize((40,40))

click_x = PhotoImage(file='New game/x.png')
x_okay = Image.open("New game/x.png")
resized_x = x_okay.resize((40,40))
button_x = ImageTk.PhotoImage(resized_x)

darkmode_click = PhotoImage(file='New game/darkmode.png')
darkmode_image = Image.open('New game/darkmode.png')
resized_darkmode= darkmode_image.resize((200,100))
button_darkmode = ImageTk.PhotoImage(resized_darkmode)
switch_play = True
switch_value = True
#Functions
apply_click = PhotoImage(file='New game/checkmark.png')
apply_image = Image.open('New game/checkmark.png')
resized_apply = apply_image.resize((70,70))
button_apply = ImageTk.PhotoImage(resized_apply)
date = pytz.timezone('Asia/Manila')
dt = datetime.now(date)

def win_toggle():
    global open
    label1=tk.Label(bg='#DCDEE5', width=40, height=100,)
    label1.place(x=0,y=0)
    def dele():
        label1.destroy()
        switch.destroy()
        about.destroy()
    def toggle():
        window.destroy()

    def aboutme():
        label1.destroy()
        switch.destroy()
        about.destroy()
        
    

    switch = Button(window, text='Exit', 
                    bd=0, bg="white",
                    activebackground="white",  
                    width=20,height=3,
                    command=toggle or win_toggle)
    switch.place(x=20,y=300)
    
    about = Button(window, text='About'
                   ,width=20,height=3,
                   bd=0
                   ,command=aboutme)
    about.place(x=20,y=100)
    
    open = tk.Button(label1  ,image=button_x 
                     ,borderwidth=0,
                     command=dele, 
                     bg= '#DCDEE5')
    open.place(x=0,y=0)

def present():
    display_t = time.strftime('%I:%M:%S %p')
    digital_clock.config(text=display_t)
    digital_clock.after(200,present) 
        
digital_clock = Label(window, width= 10, height= 2, font=("Comic Sans MS", 12,), bg='#DFD8D8')
digital_clock.place(x=700,y=365)
present()
#Buttons
button_menu = ImageTk.PhotoImage(resized)

menu_button = tk.Button(window, command= win_toggle, image=button_menu ,border=0, activebackground= '#DFD8D8', bg = '#DFD8D8')
menu_button.place(x=0,y=0)


def scheduler():
    
    
    hours = StringVar()
    Entry(window, textvariable=hours, width=2,font="arial 30", bg="#DFD8D8" ,bd=0).place(x=30,y=155)
    hours.set("00")
    
    minutes = StringVar()
    Entry(window, textvariable=minutes, width=2, font="arial 30", bg="#DFD8D8" ,bd=0).place(x=150,y=155)
    minutes.set("00")
    
    seconds = StringVar()
    Entry(window, textvariable=seconds, width=2,font="arial 30", bg="#DFD8D8" ,bd=0).place(x=270,y=155)
    seconds.set("00")
    
    Label(window, text="Hours", font="arial 20", bg="#DFD8D8",).place(x=15,y=200)
    Label(window, text="Minutes", font="arial 20", bg="#DFD8D8").place(x=125,y=200)
    Label(window, text="Seconds", font="arial 20", bg="#DFD8D8").place(x=250,y=200)
    
    def Timer():
        global time
        times=int(hours.get())*3600 + int(minutes.get())*60+int(seconds.get())
        while times > -1:
            minute,second = (times//60, times %60)
            
            hour=0
            if minute>60:
                hour,minute=(minute//60,minute%60)
            
            seconds.set(second)
            minutes.set(minute)
            hours.set(hour)

            window.update()
            time.sleep(1)
            
            if (times==0):
                seconds.set("00")
                minutes.set("00")
                hours.set("00")
    
            times -= 1
            
            
    def study():
        hours.set("00")
        minutes.set("25")
        seconds.set("00")
            
    def rest():
        hours.set("00")
        minutes.set("25")
        seconds.set("00")
            
    def skincare():
        hours.set("00")
        minutes.set("15")
        seconds.set("00")

                
    start = tk.Button(window, text="start",bg= "#DFD8D8", border=0,command= Timer, )
    start.place(x=105,y=300)
    
    studybutton = tk.Button(window, text="Study", font=("Comic Sans MS", 12) ,bg= "white",command=study ,border=0, width=30, height=5)
    studybutton.place(x=500,y=300)
    
    restbutton = tk.Button(window, text="Rest" , font=("Comic Sans MS", 12),bg= "white", command= rest ,border=0, width=30, height=5)
    restbutton.place(x=500,y=100)
    
    skincarebutton = tk.Button(window, text="Skincare" , font=("Comic Sans MS", 12),bg= "white", command=skincare, border=0, width=30, height=5)
    skincarebutton.place(x=500,y=200)
    
    window.mainloop()
    def rest():
        window = tk.Tk()
        window.geometry('800x400')
        window.resizable(False, False)
        window.attributes('-alpha', 0.9)
        #window.attributes('-fullscreen', True)
        window.configure(bg='#DFD8D8')
        
    def skincare():
        window = tk.Tk()
        window.geometry('800x400')
        window.resizable(False, False)
        window.attributes('-alpha', 0.9)
        #window.attributes('-fullscreen', True)
        window.configure(bg='#DFD8D8')
        
    studybutton = tk.Button(window, text="Study", font=("Comic Sans MS", 12) ,bg= "white",command=study ,border=0, width=30, height=5)
    studybutton.place(x=500,y=300)
    
    restbutton = tk.Button(window, text="Rest" , font=("Comic Sans MS", 12),bg= "white", command= rest ,border=0, width=30, height=5)
    restbutton.place(x=500,y=100)
    
    skincarebutton = tk.Button(window, text="Skincare" , font=("Comic Sans MS", 12),bg= "white", command=skincare, border=0, width=30, height=5)
    skincarebutton.place(x=500,y=200)
                        
scheduler_button = tk.Button(window, text="Scheduler",command=scheduler, border=0, activebackground="white",bg = 'white') 
scheduler_button.place(x=100,y=200)


window.mainloop()

#Nicko <3