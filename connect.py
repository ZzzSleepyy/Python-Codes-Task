import customtkinter as ctk
import time

window = ctk.CTk()
window.geometry("1000x600")
window.title("Knowdify")
window._set_appearance_mode("dark")


font = ctk.CTkFont(family="Comic Sans MS"
                   , size=20)

button1_enabled = False 

def switchButtonState():
    global button1_enabled
    button1_enabled = not button1_enabled
    
    if button1_enabled:
        state1 = ctk.NORMAL
        state2 = ctk.DISABLED
        bottom_label.place(x=250,y=550)
        input_text.place(x=250,y=550)
        dashboard_label.place(x=250,y=0)
        
    else:
        state1 = ctk.DISABLED
        state2 = ctk.NORMAL
        bottom_label.place_forget()
        input_text.place_forget()
        dashboard_label.place_forget()
        
    dashboard.configure(state=state1)
    chatbot.configure(state=state2)



def widgets():
    if input_text.get() == "hi" or input_text.get() == "hello":
             widget_texts.append("Bot: Hello there!")
    if input_text.get() == "how are you" or input_text.get() == "how r u":
             label.configure("Bot: I'm doing well actually.")
    for i, text in enumerate(widget_texts):
        i = i + 2
        widget = ctk.CTkLabel(dashboard_label, text=text, font=font, text_color="#e83f3f")
        widget.grid(row=i, column=0, padx=10, pady=10)

        label = ctk.CTkLabel(dashboard_label, text="...", font=font, text_color="#e83f3f", width=40)
        label.grid(row=i, column=0, padx=10, pady=10)
        label.after(1000, lambda l=label: l.destroy())

    dashboard_label.update()
    


bottom_label = ctk.CTkFrame(window
                            , width=750
                            , height=50
                            , border_color="#ab9335"
                            , border_width=2)
bottom_label._set_appearance_mode("dark")

design_board = ctk.CTkFrame(window
                            , width=250
                            , height=600
                            , border_color="#ab9335"
                            , border_width=2)
design_board.place(x=0,y=0)
design_board._set_appearance_mode("dark")

dashboard = ctk.CTkButton(window, text="Dashboard"
                          , state=ctk.DISABLED
                          , command=switchButtonState
                          , font=font, border_width=1
                          , text_color="#ab9335"
                          , hover_color="#6b685c"
                          , border_color="#ab9335")
dashboard._set_appearance_mode("dark")
dashboard.place(x=50,y=100)

chatbot = ctk.CTkButton(window
                        , text="Chatbot"
                        , state=ctk.NORMAL
                        , command=switchButtonState
                        , font=font
                        , border_width=1
                        , border_color="#ab9335"
                        , text_color="#ab9335"
                        , hover_color="#6b685c")
chatbot._set_appearance_mode("dark")
chatbot.place(x=50,y=200)

input_text = ctk.CTkEntry(window
                          , height=50
                          , width=750
                          , font=font
                          , placeholder_text= "Ask a question.")


dashboard_label = ctk.CTkScrollableFrame(window
                                        , corner_radius=0
                                        , scrollbar_button_color="#e83f3f"
                                        , fg_color="#211e1e"
                                        , width=735
                                        , height=550)
dashboard_label._set_appearance_mode("dark")

f = ctk.CTkButton(window, text="Enter"
                          , state=ctk.NORMAL
                          , command=widgets
                          , font=font, border_width=1
                          , text_color="#ab9335"
                          , hover_color="#6b685c"
                          , border_color="#ab9335")
f._set_appearance_mode("dark")
f.place(x=300,y=200)

widget_texts = []
widgetstart = ctk.CTkLabel(dashboard_label, text="Bot: Feel free to ask question you like.", font=font, text_color="#e83f3f")
widgetstart.grid(row=0, column=0, padx=10, pady=10)


input_text._set_appearance_mode("dark")
window.mainloop()
################################################################################################################


import customtkinter as ctk
import time
from PIL import Image
import math
from tkinter .messagebox import showerror, showinfo, showwarning

window = ctk.CTk()
window.resizable(False, False)
window._set_appearance_mode("dark")
window.config(bg="#18191A")

window.geometry("1000x600")
window.title("Knowdify")

font = ctk.CTkFont(family="Verdana"
                   , size=13)

font_profile = ctk.CTkFont(family="Verdana"
                   , size=20, weight='bold')

button1_enabled = False

def switch_calculator():
    if switch_var.get() == "Calculator On":
        command_texts.append("Calculator On")
        logcommand()
    elif switch_var.get() == "Calculator Off":
        command_texts.append("Calculator Off")
        logcommand()

def switchButtonState():
    global button1_enabled
    button1_enabled = not button1_enabled
    
    if button1_enabled:
        state1 = ctk.NORMAL
        state2 = ctk.DISABLED
        profile.place_forget()
        bottom_label.place(x=250,y=550)
        dashboard_label.place(x=250,y=0)
        input_text.place_forget()
        button_enter.place_forget()
        dashboard_design.place_forget()
        dashboard_inside.place_forget()
        dashboard_logs.place_forget()
    else:
        state1 = ctk.DISABLED
        state2 = ctk.NORMAL
        dashboard_design.place(x=150,y=0)
        profile.place(x=160,y=15)
        bottom_label.place_forget()
        input_text.place(x=170,y=550)
        dashboard_label.place_forget()
        button_enter.place(x=600,y=550)
        dashboard_inside.place(x=160,y=120)
        dashboard_logs.place(x=180,y=200)
    dashboard.configure(state=state1)
    chatbot.configure(state=state2)




widget_texts = []

command_texts = []


def logcommand():
    for i, command_text in enumerate(command_texts):
        i = i + 1
        widget = ctk.CTkLabel(dashboard_logs, text=f"Added command: {command_text}", font=font, text_color="#08a8ff", wraplength=200, anchor="w")
        widget.grid(row=i, column=0, padx=10, pady=10, sticky="w")
        widget._set_appearance_mode("dark")
    dashboard_logs.update()

def widgets():
    global widget
    if input_text.get() == "":
        command_texts.append("No input.")
        logcommand()
        showwarning(
            title="Warning",
            message="Enter the right value."
        )
    elif len(widget_texts) == 10:
        showerror(
            title="Oops!",
            message="You can only add 10 tasks."
        )
    else:
        progress_task.step()    
        command_texts.append(input_text.get())
        logcommand()
        widget_texts.append(input_text.get())
        for l, formatted_text in enumerate(widget_texts):
            l = l + 1
            widget = ctk.CTkLabel(dashboard_label, text=f"{l}. {formatted_text}", font=font, text_color="#e83f3f", wraplength=200, anchor="w")
            widget.grid(row=l, column=0, padx=10, pady=10, sticky="w")
            widget._set_appearance_mode("dark")
        dashboard_label.update()

profile_pic_image = ctk.CTkImage(dark_image=Image.open("Reviewer app/pictures/icons8-male-user-24.png"), size=(35,35))


logo_image = ctk.CTkImage(dark_image=Image.open("Reviewer app/pictures/logo.png"), size=(40,40))


bottom_label = ctk.CTkFrame(window
                            , width=750
                            , height=50
                            , border_color="#ab9335")
bottom_label._set_appearance_mode("dark")

design_board = ctk.CTkFrame(window
                            , width=150
                            , height=600)
design_board.place(x=0,y=0)
design_board._set_appearance_mode("dark")



dashboard = ctk.CTkButton(window, text="Dashboard"
                          , state=ctk.DISABLED
                          , command=switchButtonState
                          , font=font
                          , text_color="#000000")
dashboard.place(x=5,y=100)
dashboard._set_appearance_mode("dark")


settings = ctk.CTkButton(window, text="Switch"
                          , state=ctk.NORMAL
                          , command=switchButtonState
                          , font=font
                          , text_color="#000000")
settings.place(x=5,y=200)
settings._set_appearance_mode("dark")

dashboard_inside = ctk.CTkFrame(window, width=830, height=400, border_width=0.5)
dashboard_inside.place(x=160,y=120)
dashboard_inside._set_appearance_mode("dark")

chatbot = ctk.CTkButton(window
                        , text="Tasks"
                        , state=ctk.NORMAL
                        , command=switchButtonState
                        , font=font
                        , border_color="#FFFFFF"
                        , text_color="#000000")
chatbot.place(x=5,y=150)
chatbot._set_appearance_mode("dark")

input_text = ctk.CTkEntry(window
                          , height=30
                          , width=400
                          , font=font
                          , placeholder_text= "Add a task. | Ex: 1. Study"
                          , border_width=0.5)
input_text._set_appearance_mode("dark")
input_text.place(x=170,y=550)


dashboard_label = ctk.CTkScrollableFrame(window
                                        , corner_radius=0
                                        , width=200
                                        , height=400)
dashboard_label._set_appearance_mode("dark")

button_enter = ctk.CTkButton(window, text="Enter"
                          , state=ctk.NORMAL
                          , command=widgets
                          , font=font
                          , text_color="#ab9335"
                          , bg_color="#18191A"
                          , hover_color="#6b685c"
                          , border_color="#ab9335")
dashboard_label._set_appearance_mode("dark")
button_enter.place(x=600,y=550)\

dashboard_design = ctk.CTkFrame(window
                                , fg_color="#3a3b3c"
                                , bg_color="#3a3b3c"
                                , width=850
                                , height=60)
dashboard_design.place(x=150,y=0)
dashboard_design._set_appearance_mode("dark")

dashboard_logs = ctk.CTkScrollableFrame(window
                                        , border_width=1
                                        , width=200
                                        , height=200
                                        , bg_color="#2b2b2b"
                                        , fg_color="#2b2b2b"
                                        , border_color="#464d4f")
dashboard_logs._set_appearance_mode("dark")
dashboard_logs.place(x=180,y=200)

profile = ctk.CTkLabel(window
                       , text="Knowdify"
                       , font=font_profile
                       , bg_color="#3a3b3c"
                       , fg_color="#3a3b3c"
                       , text_color="#00a8f3")
profile.place(x=160,y=19)

version = ctk.CTkLabel(window
                       , text="V1.0"
                       , font=font_profile
                       , bg_color="#2b2b2b"
                       , fg_color="#2b2b2b"
                       , text_color="#00a8f3")
version.place(x=45,y=19)

switch_d_l = ctk.CTkSwitch(window
                           , text="Darkmode"
                           , bg_color="#2b2b2b"
                           , text_color="#FFFFFF")
switch_d_l.place(x=20,y=510)

switch_var = ctk.StringVar()
calculator = ctk.CTkSwitch(window
                           , text="Calculator"
                           , bg_color="#2b2b2b"
                           , text_color="#FFFFFF"
                           , variable=switch_var
                           , onvalue="Calculator On"
                           , offvalue="Calculator Off"
                           , command = switch_calculator)
calculator.place(x=20,y=550)

progress_task = ctk.CTkProgressBar(window
                                   , orientation="vertical"
                                   , width=20
                                   , height=200
                                   , bg_color="#2b2b2b"
                                   , determinate_speed=5
                                   , corner_radius=5)
progress_task.place(x=450,y=210)


progress_task.set(0)

def test(selected_value):
    if widget_texts and selected_value == "Number 1":
        widget_texts.remove(widget_texts[0])
        widget.destroy()
        remove_combobox.update()
    if widget_texts and selected_value == "Number 2":
        widget_texts.remove(widget_texts[1])
        
        widget.destroy()
        remove_combobox.update()
    print(widget_texts)

remove_combobox = ctk.CTkComboBox(window, values=["Number 1", "Number 2","Number 3","Number 4", "Number 5","Number 6","Number 7", "Number 8","Number 9","Number 10"], command=test, corner_radius=20)
remove_combobox.pack()

def timestft():
    format = time.strftime("%A")
    label_time.configure(text=format)
    label_time.after(1000, timestft)
    if format == "Saturday":
        label_time.configure(text_color= "#5ca19e")    
    elif format == "Sunday":
        label_time.configure(text_color= "#FF7F7F")  
    elif format == "Monday":
        label_time.configure(text_color= "#cdd61a")  
    elif format == "Tuesday":
        label_time.configure(text_color= "#2c735b")  
    elif format == "Wednesday":
        label_time.configure(text_color= "#290e20") 
    elif format == "Thursday":
        label_time.configure(text_color= "#3d0c0c")  
    elif format == "Friday":
        label_time.configure(text_color= "#4f230d")   
        
label_time = ctk.CTkLabel(window
                          , font=font_profile
                          , bg_color="#2b2b2b"
                          , fg_color="#2b2b2b")
label_time.place(x=20,y=450)


timestft()



window.mainloop()
