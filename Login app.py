from customtkinter import *

window = CTk()
window.geometry("350x350")
window._set_appearance_mode("dark")
window.title("AD1E")

login_names = ["adie123","test"]
login_pass = ["123","test"]

def button_login():
    username = login_entry.get()
    password = login_password.get()
    
    for widget in window.winfo_children():
        if isinstance(widget, CTkLabel) and widget.cget("text") != "Username" and widget.cget("text") != "Password" and widget.cget("text") != "AD1E":
            widget.destroy()
    
    if username in login_names[0] and password == login_pass[0] and [login_names[0].index(username)]:
        window.destroy()
            
        loginwindow = CTk()
        loginwindow.geometry("400x500")
        loginwindow._set_appearance_mode("dark")
        loginwindow.title("Admin panel")
        
        label_title = CTkLabel(loginwindow, text=f"Welcome, {username}", font=("Comic Sans MS",25))
        label_title._set_appearance_mode("dark")
        label_title.place(x=20,y=20)
        
        show_console = CTkButton(loginwindow, text="Show console", bg_color="#36454F" ,border_width=1 ,command=None, font=("Comic Sans MS",20))
        show_console.place(x=50,y=200)
        
        show_banned = CTkButton(loginwindow, text="Show banned", bg_color="#36454F" ,border_width=1 ,command=None, font=("Comic Sans MS",20))
        show_banned.place(x=50,y=100)
        
        ban_user = CTkButton(loginwindow, text="Ban User", bg_color="#36454F" ,border_width=1 ,command=None, font=("Comic Sans MS",20))
        ban_user.place(x=200,y=100)
        
        warn_user = CTkButton(loginwindow, text="Ban User", bg_color="#36454F" ,border_width=1 ,command=None, font=("Comic Sans MS",20))
        warn_user.place(x=200,y=200)
        
        role = CTkLabel(loginwindow, text="You are the Owner!", font=("Comic Sans MS",46))
        role._set_appearance_mode("dark")
        role.place(y=300)
        
        loginwindow.mainloop()
        
            
    elif username not in login_names and username not in login_pass:
        label_incorrect = CTkLabel(window, text="Incorrect Password and Username.", font=("Comic Sans MS",15))
        label_incorrect._set_appearance_mode("dark")
        label_incorrect.place(x=60,y=280)

    
    else:
        label_wrong = CTkLabel(window, text="The password does not match the username.", font=("Comic Sans MS",15))
        label_wrong._set_appearance_mode("dark")
        label_wrong.place(x=35,y=280)
    


label_name = CTkLabel(window, text="Username", font=("Comic Sans MS",20)) # USERNAME LABEL
label_name._set_appearance_mode("dark")
label_name.place(x=110,y=70)


label_password = CTkLabel(window, text="Password", font=("Comic Sans MS",20)) # LABEL PASSWORD
label_password._set_appearance_mode("dark")
label_password.place(x=110,y=140)

label_title = CTkLabel(window, text="AD1E", font=("Comic Sans MS",25)) # LABEL TITLE
label_title._set_appearance_mode("dark")
label_title.place(x=20,y=20)


login_entry = CTkEntry(window ,bg_color="#36454F", height=35) # LOGIN ENTRY
login_entry.place(x=110,y=100)

login_password = CTkEntry(window, bg_color="#36454F", height=35, show="*") # LOGIN ENTRY PASSWORD
login_password.place(x=110,y=170)

login_button = CTkButton(window, text="Login", bg_color="#36454F" ,border_width=1 ,command=button_login, font=("Comic Sans MS",20)) # LOGIN BUTTON
login_button.place(x=110,y=230)

 

window.mainloop()



#UPDATE



from customtkinter import *

window = CTk()
window.geometry("350x350")
window._set_appearance_mode("dark")
window.title("AD1E")
admin = ["adie123"]
login_names = ["adie123","test".lower()]
login_pass = ["123","test"]

def button_login():
    username = login_entry.get()
    password = login_password.get()
    
    for widget in window.winfo_children():
        if isinstance(widget, CTkLabel) and widget.cget("text") != "Username" and widget.cget("text") != "Password" and widget.cget("text") != "AD1E":
            widget.destroy()
    
    if username in login_names[0] and password == login_pass[0] and [login_names[0].index(username)] or username in login_names[1] and password == login_pass[1] and [login_names[1].index(username)]:
        window.destroy()
            
        loginwindow = CTk()
        loginwindow.geometry("400x500")
        loginwindow._set_appearance_mode("dark")
        loginwindow.title("Admin panel")
        
        
        label_title = CTkLabel(loginwindow, text=f"Welcome, {username}", font=("Comic Sans MS",25))
        label_title._set_appearance_mode("dark")
        label_title.place(x=20,y=20)
        def ban_command():
            user_ban = ban_username.get()
            if user_ban in login_names:
                commands = CTkLabel(loginwindow, text=f"User {user_ban} has been banned.", font=("Comic Sans MS",25))
                commands.place(x=100,y=50)
                login_names.remove(user_ban)
                
        show_console = CTkButton(loginwindow, text="Show console", bg_color="#36454F" ,border_width=1 ,command=None, font=("Comic Sans MS",20))
        show_console.place(x=50,y=100)
        
        show_banned = CTkButton(loginwindow, text="Show banned", bg_color="#36454F" ,border_width=1 ,command=None, font=("Comic Sans MS",20))
        show_banned.place(x=200,y=200)
        
        warn_user = CTkButton(loginwindow, text="Warn User", bg_color="#36454F" ,border_width=1 ,command=None, font=("Comic Sans MS",20))
        warn_user.place(x=50,y=200)
        
        role = CTkLabel(loginwindow, text="You are the Owner!", font=("Comic Sans MS",46))
        role._set_appearance_mode("dark")
        role.place(y=300)
        
        ban_username = CTkEntry(loginwindow, bg_color="#36454F" ,border_width=1, font=("Comic Sans MS",20))
        ban_username.place(x=130,y=400)
        ban_username._set_appearance_mode("dark")
        
        ban_user = CTkButton(loginwindow, text="Ban User", bg_color="#36454F" ,border_width=1 ,command=ban_command, font=("Comic Sans MS",20))
        ban_user.place(x=200,y=100)
        
        loginwindow.mainloop()
        
            
    elif username not in login_names and username not in login_pass:
        label_incorrect = CTkLabel(window, text="Incorrect Password and Username.", font=("Comic Sans MS",15))
        label_incorrect._set_appearance_mode("dark")
        label_incorrect.place(x=60,y=280)

    
    else:
        label_wrong = CTkLabel(window, text="The password does not match the username.", font=("Comic Sans MS",15))
        label_wrong._set_appearance_mode("dark")
        label_wrong.place(x=35,y=280)
    


label_name = CTkLabel(window, text="Username", font=("Comic Sans MS",20)) # USERNAME LABEL
label_name._set_appearance_mode("dark")
label_name.place(x=110,y=70)


label_password = CTkLabel(window, text="Password", font=("Comic Sans MS",20)) # LABEL PASSWORD
label_password._set_appearance_mode("dark")
label_password.place(x=110,y=140)

label_title = CTkLabel(window, text="AD1E", font=("Comic Sans MS",25)) # LABEL TITLE
label_title._set_appearance_mode("dark")
label_title.place(x=20,y=20)


login_entry = CTkEntry(window ,bg_color="#36454F", height=35) # LOGIN ENTRY
login_entry.place(x=110,y=100)

login_password = CTkEntry(window, bg_color="#36454F", height=35, show="*") # LOGIN ENTRY PASSWORD
login_password.place(x=110,y=170)

login_button = CTkButton(window, text="Login", bg_color="#36454F" ,border_width=1 ,command=button_login, font=("Comic Sans MS",20)) # LOGIN BUTTON
login_button.place(x=110,y=230)

 

window.mainloop()
