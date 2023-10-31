
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
#DAY 2 ----------------------------------------------------------------------------------------------------------------------------------------
from customtkinter import *

import customtkinter as ctk

window = ctk.CTk()
window._set_appearance_mode("light")
window.geometry("335x350")
window.title("Calculator Day #1")

characters = ""

def num(press):
    global characters
    characters = characters + str(press)
    eq.set(characters)

def equal():
    try:
        global characters
        total = str(eval(characters))
        eq.set(total)
        
    except:
        eq.set("Error")
        characters = ""
def clear():
    global characters
    characters = ""
    eq.set("")

eq = StringVar()

buttoninsert = ctk.CTkEntry(window, textvariable=eq, width=240, height=50)
buttoninsert.place(x=50,y=20)
buttoninsert._set_appearance_mode("dark")

button1 = ctk.CTkButton(window
                        ,text="1"
                        ,width=40
                        ,height=40
                        ,command=lambda: num(1))
button1.place(x=50, y=80)
button1._set_appearance_mode("dark")

button2 = ctk.CTkButton(window
                        ,text="2"
                        ,width=40
                        ,height=40
                        ,command=lambda: num(2))
button2.place(x=100, y=80)
button2._set_appearance_mode("dark")

button3 = ctk.CTkButton(window
                        ,text="3"
                        ,width=40
                        ,height=40
                        ,command=lambda: num(3))
button3.place(x=150, y=80)
button3._set_appearance_mode("dark")

button4 = ctk.CTkButton(window
                        ,text="4"
                        ,width=40
                        ,height=40
                        ,command=lambda: num(4))
button4.place(x=200, y=80)
button4._set_appearance_mode("dark")
#
button5 = ctk.CTkButton(window
                        ,text="5"
                        ,width=40
                        ,height=40
                        ,command=lambda: num(5))
button5.place(x=50, y=140)
button5._set_appearance_mode("dark")

button6 = ctk.CTkButton(window
                        ,text="6"
                        ,width=40
                        ,height=40
                        ,command=lambda: num(6))
button6.place(x=100, y=140)
button6._set_appearance_mode("dark")

button7 = ctk.CTkButton(window
                        ,text="7"
                        ,width=40
                        ,height=40
                        ,command=lambda: num(7))
button7.place(x=150, y=140)
button7._set_appearance_mode("dark")

button8 = ctk.CTkButton(window
                        ,text="8"
                        ,width=40
                        ,height=40
                        ,command=lambda: num(8))
button8.place(x=200, y=140)


button9 = ctk.CTkButton(window
                        ,text="9"
                        ,width=40
                        ,height=40
                        ,command=lambda: num(9))

button9.place(x=200, y=200)

button10 = ctk.CTkButton(window
                        ,text="Clear"
                        ,width=40
                        ,height=40
                        ,command=lambda: clear())
button10.place(x=50, y=200)

button11 = ctk.CTkButton(window
                        ,text="x"
                        ,width=40
                        ,height=40
                        ,command=lambda: num("*"))
button11.place(x=250, y=80)

button12 = ctk.CTkButton(window
                        ,text="÷"
                        ,width=40
                        ,height=40
                        ,command=lambda: num("/"))
button12.place(x=250, y=140)


button13 = ctk.CTkButton(window
                        ,text="0"
                        ,width=40
                        ,height=40
                        ,command=lambda: num(0))

button13.place(x=150, y=200)

button14 = ctk.CTkButton(window
                        ,text="+"
                        ,width=40
                        ,height=40
                        ,command=lambda: num("+"))
button14.place(x=250, y=200)

button15 = ctk.CTkButton(window
                        ,text="-"
                        ,width=40
                        ,height=40
                        ,command=lambda: num("-"))
button15.place(x=250, y=200)


enter = ctk.CTkButton(window
                        ,text="Enter"
                        ,width=40
                        ,height=40
                        ,command=equal)

enter.place(x=100, y=200)

window._set_appearance_mode("dark")
enter._set_appearance_mode("dark")
button15._set_appearance_mode("dark")
button14._set_appearance_mode("dark")
button13._set_appearance_mode("dark")
button12._set_appearance_mode("dark")
button11._set_appearance_mode("dark")
button10._set_appearance_mode("dark")
button9._set_appearance_mode("dark")
button8._set_appearance_mode("dark")
button7._set_appearance_mode("dark")
button6._set_appearance_mode("dark")
button5._set_appearance_mode("dark")
button4._set_appearance_mode("dark")
button3._set_appearance_mode("dark")
button2._set_appearance_mode("dark")
button1._set_appearance_mode("dark")


def switch():
    if var.get() == "Darkmode":
        window._set_appearance_mode("dark")
        enter._set_appearance_mode("dark")
        button15._set_appearance_mode("dark")
        button14._set_appearance_mode("dark")
        button13._set_appearance_mode("dark")
        button12._set_appearance_mode("dark")
        button11._set_appearance_mode("dark")
        button10._set_appearance_mode("dark")
        button9._set_appearance_mode("dark")
        button8._set_appearance_mode("dark")
        button7._set_appearance_mode("dark")
        button6._set_appearance_mode("dark")
        button5._set_appearance_mode("dark")
        button4._set_appearance_mode("dark")
        button3._set_appearance_mode("dark")
        button2._set_appearance_mode("dark")
        button1._set_appearance_mode("dark")
        buttoninsert._set_appearance_mode("dark")
        switch_lightmode_darkmode._set_appearance_mode("dark")
        
    elif var.get() == "Lightmode":
        window._set_appearance_mode("light")
        enter._set_appearance_mode("light")
        button15._set_appearance_mode("light")
        button14._set_appearance_mode("light")
        button13._set_appearance_mode("light")
        button12._set_appearance_mode("light")
        button11._set_appearance_mode("light")
        button10._set_appearance_mode("light")
        button9._set_appearance_mode("light")
        button8._set_appearance_mode("light")
        button7._set_appearance_mode("light")
        button6._set_appearance_mode("light")
        button5._set_appearance_mode("light")
        button4._set_appearance_mode("light")
        button3._set_appearance_mode("light")
        button2._set_appearance_mode("light")
        button1._set_appearance_mode("light")
        buttoninsert._set_appearance_mode("light")
        switch_lightmode_darkmode._set_appearance_mode("light")
var = ctk.StringVar()
switch_lightmode_darkmode = ctk.CTkSwitch(window
                                          ,command=switch
                                          ,variable=var
                                          ,text="D/L"
                                          ,onvalue="Lightmode"
                                          ,offvalue="Darkmode")
switch_lightmode_darkmode.place(x=100,y=320)
switch_lightmode_darkmode._set_appearance_mode("dark")

window.mainloop()
