import tkinter as gold
from tkinter import StringVar, messagebox
import re
from calendar import calendar, month
from tkinter import ttk
from tkinter.constants import ANCHOR, BOTH, CENTER, INSERT, LEFT, RIGHT, TRUE

import API
from tkcalendar import DateEntry
window= gold.Tk()

window.title('Johnny Dang & Co.')
window.geometry('720x480')
window.iconbitmap('gold.ico')
frame1 = gold.Frame(window)
frame2 = gold.Frame(window)
frame3 = gold.Frame(window)


def checkLogin():
    account = []
   
    username_1 = username.get()
    password_1 = password.get()

    account.append(username_1)
    account.append(password_1)

    if(username_1 == "" or password_1 == "" ):
        messagebox.showinfo("Warning!", "Blank not allowed")
    elif (len(username_1) >= 30) or (len(password_1) >= 30):
        messagebox.showinfo("Warning!","Too much character" + "\n" + "The username or password must less than 30 character")
    elif not (re.match("^[a-zA-Z0-9]*$",username_1) and re.match("^[a-zA-Z0-9]*$",password_1)):
         messagebox.showinfo("Warning!","Error! Only letters a-z allowed!")
    else:
        infoPage()

def hide_frame():
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    
def registerCheck():
    account = []
   
    username_1 = usernameR.get()
    password_1 = passwordR.get()
    password_2 = repasswordR.get()

    account.append(username_1)
    if(password_1!=password_2):
        messagebox.showinfo("Warning!", "Passwords are not matched")
    elif(username_1 == "" or password_1 == "" ):
        messagebox.showinfo("Warning!", "Blank not allowed")
    elif (len(username_1) >= 30) or (len(password_1) >= 30):
        messagebox.showinfo("Warning!","Too much character" + "\n" + "The username or password must less than 30 character")
    elif not (re.match("^[a-zA-Z0-9]*$",username_1) and re.match("^[a-zA-Z0-9]*$",password_1)):
         messagebox.showinfo("Warning!","Error! Only letters a-z allowed!")
    else:
        account.append(password_1)
        infoPage()
        
def registerAccount():
    hide_frame()
    menu=gold.Label(frame3,text='Gold Price', font=('Times new roman',35),foreground='orange').place(x=260,y=20)
    frame3.pack(fill="both",expand=1)
    nametag=gold.Label(frame3,text='Username').place(x=195,y=100)
    passtag=gold.Label(frame3,text='Password').place(x=195,y=130)
    passtag=gold.Label(frame3,text='Confirm password').place(x=195,y=160)
    global usernameR
    global passwordR
    global repasswordR
    usernameR=StringVar()
    passwordR=StringVar()
    repasswordR=StringVar()
    usernameR=gold.Entry(frame3)
    usernameR.place(x=300,y=100)
    passwordR=gold.Entry(frame3)
    passwordR.place(x=300,y=130)
    passwordR.config(show='*')
    repasswordR=gold.Entry(frame3)
    repasswordR.place(x=300,y=160)
    repasswordR.config(show='*')
    button=gold.Button(frame3,text='Register',bg='orange',command=registerCheck).place(x=330,y=195)

def infoPage():
    hide_frame()

    label_title = gold.Label(frame2, text='Gold Price',
                           font=("Times new roman", 30, "bold"), foreground= "orange").place(x=260,y=3)
    logout_button = gold.Button(frame2, text='Logout',
                              width=10, command=lambda: login_page())

    global showInfo
    global goldType
    global my_date
    my_date = StringVar()

    showInfo = gold.Text(frame2, font=("Arial", 12), width=60, height=15)

    ok_button = gold.Button(frame2, text="OK", width=5,
                          bg="orange")
    quit_button = gold.Button(frame2, text='Quit', width=10, command=window.destroy)
    # combobox
    goldType =  ttk.Combobox(frame2, values=API.goldType)
    goldType.current(0)
    # date picker
    my_date = DateEntry(frame2, selectmode='day',year = 2021, month=12, day=19)

    frame2.pack(fill=BOTH, expand=1)
    
    my_date.place(x=550,y=53)
    logout_button.place(x=280, y= 400)
    showInfo.place(x=100, y=100)
    ok_button.place(x=660, y=50)
    quit_button.place(x=370, y=400)
    goldType.place(x=400, y=53)

def handleInfo():

    return

def login_page():
    hide_frame()
    menu=gold.Label(frame1,text='Gold Price', font=('Times new roman',35),foreground='orange').place(x=260,y=20)
    frame1.pack(fill="both",expand=1)
    nametag=gold.Label(frame1,text='Username').place(x=235,y=100)
    passtag=gold.Label(frame1,text='Password').place(x=235,y=130)
    global username
    global password
    username=StringVar()
    password=StringVar()
    username=gold.Entry(frame1)
    username.place(x=300,y=100)
    password=gold.Entry(frame1)
    password.config(show='*')
    password.place(x=300,y=130)
    button=gold.Button(frame1,text='Login',bg='orange',command=checkLogin).place(x=310,y=170)
    button=gold.Button(frame1,text='Register',bg='orange',command=registerAccount).place(x=370,y=170)
#login_page()
infoPage()
window.mainloop()