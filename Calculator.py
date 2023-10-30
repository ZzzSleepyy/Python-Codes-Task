
from customtkinter import *

import customtkinter as ctk

window = ctk.CTk()
window._set_appearance_mode("dark")
window.geometry("300x350")
window.title("Calculator Day #1")

characters = ""

def num(press):
    
    global characters
    
    characters = characters + str(press)
    
    eq.set(characters)

def equal():
    pass

def clear():
    
    global characters
    characters = ""
    eq.set("")

eq = StringVar()

buttoninsert = ctk.CTkEntry(window, textvariable=eq)
buttoninsert.place(x=80,y=20)

button1 = ctk.CTkButton(window, text="1", width=40, height=40, command=lambda: num(1))
button1.place(x=50, y=80)
button1._set_appearance_mode("dark")

button2 = ctk.CTkButton(window, text="2", width=40, height=40, command=lambda: num(2))
button2.place(x=100, y=80)
button2._set_appearance_mode("dark")

button3 = ctk.CTkButton(window, text="3", width=40, height=40, command=lambda: num(3))
button3.place(x=150, y=80)
button3._set_appearance_mode("dark")

button4 = ctk.CTkButton(window, text="4", width=40, height=40, command=lambda: num(4))
button4.place(x=200, y=80)
button4._set_appearance_mode("dark")
#
button5 = ctk.CTkButton(window, text="5", width=40, height=40, command=lambda: num(5))
button5.place(x=50, y=160)
button5._set_appearance_mode("dark")

button6 = ctk.CTkButton(window, text="6", width=40, height=40, command=lambda: num(6))
button6.place(x=100, y=160)
button6._set_appearance_mode("dark")

button7 = ctk.CTkButton(window, text="7", width=40, height=40, command=lambda: num(7))
button7.place(x=150, y=160)
button7._set_appearance_mode("dark")

button8 = ctk.CTkButton(window, text="8", width=40, height=40, command=lambda: num(8))
button8.place(x=200, y=160)
button8._set_appearance_mode("dark")

button9 = ctk.CTkButton(window, text="9", width=40, height=40, command=lambda: num(9))
button9._set_appearance_mode("dark")
button9.place(x=200, y=240)

button9 = ctk.CTkButton(window, text="Clear", width=40, height=40, command=lambda: clear())
button9._set_appearance_mode("dark")
button9.place(x=50, y=240)

window.mainloop()
