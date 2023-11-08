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
