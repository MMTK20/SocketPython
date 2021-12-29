import tkinter as gold
from tkinter import StringVar, messagebox
import re
from calendar import calendar, month
from tkinter import ttk
from tkinter.constants import BOTH
import client as c
import API
from tkcalendar import DateEntry
window = gold.Tk()

window.title('Johnny Dang & Co. Client')
window.geometry('720x480')
window.iconbitmap('gold.ico')
frame1 = gold.Frame(window)
frame2 = gold.Frame(window)
frame3 = gold.Frame(window)


def checkLogin(client):
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
        temp = c.sendMessage(client,"login",account)
        if(temp=="okee"):
            infoPage(client)
        else:
            messagebox.showinfo("Warning!","Account or password was wrong.")
            

def hide_frame():
    frame1.pack_forget()
    frame2.pack_forget()
    frame3.pack_forget()
    
def registerCheck(client):
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
        temp = c.sendMessage(client,"register",account)
        if(temp=="okee"):
            infoPage(client)
        else:
            messagebox.showinfo("Warning!","Register failed!")

        
def registerAccount(client):
    hide_frame()

    menu=gold.Label(frame3,text='Gold Price', font=('Times new roman',35),foreground='orange')
    menu.place(x=260,y=20)

    frame3.pack(fill="both",expand=1)

    nametag=gold.Label(frame3,text='Username')
    nametag.place(x=195,y=100)
    passtag=gold.Label(frame3,text='Password')
    passtag.place(x=195,y=130)
    passtag2=gold.Label(frame3,text='Confirm password')
    passtag2.place(x=195,y=160)

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
    button=gold.Button(frame3,text='Register',bg='orange',command=lambda:registerCheck(client)).place(x=330,y=195)

def infoPage(client):
    hide_frame()

    label_title = gold.Label(frame2, text='Gold Price',font=("Times new roman", 30, "bold"), foreground= "orange")
    label_title.place(x=260,y=3)

    logout_button = gold.Button(frame2, text='Logout',width=10,bg="red", command= login_page)
    logout_button.place(x=245, y= 435)

    global showInfo
    global goldType
    global date

    date = StringVar()

    showInfo = gold.Text(frame2, font=("Times new roman", 15), width=69, height=14)
    showInfo.place(x=10, y=100)

    search_button = gold.Button(frame2, text="Search", width=5,bg="orange", command=lambda:handleInfo(client))
    search_button.place(x=660, y=62)

    exit_button = gold.Button(frame2, text="Exit", width=10,bg="red", command=lambda:closeWindow(client))
    exit_button.place(x=375, y=435)

    # choose type of Gold
    goldType =  ttk.Combobox(frame2, values=API.goldType)
    goldType.current(0)

    # choose day month year
    date = DateEntry(frame2, selectmode= 'day',year = 2021, month=12, day=19)
    date.place(x=550,y=65)

    frame2.pack(fill=BOTH, expand=1)
    
    goldType.place(x=400, y=65)

def handleInfo(client):
    TypeAndTime=[]
    type=goldType.get()
    time=date.get_date()
    time2=time.strftime(r"%Y%m%d")
    
    TypeAndTime.append(type)
    TypeAndTime.append(time2)

    print(TypeAndTime)
    c.sendMessage(client,"info",TypeAndTime)
    return

def closeWindow(client):
    if messagebox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()
        c.closeConnection(client)

def login_page():

    hide_frame()

    client=c.startConnect()

    menu=gold.Label(frame1,text='Gold Price', font=('Times new roman',35),foreground='orange')
    menu.place(x=260,y=20)

    frame1.pack(fill="both",expand=1)

    nametag=gold.Label(frame1,text='Username')
    nametag.place(x=235,y=100)

    passtag=gold.Label(frame1,text='Password')
    passtag.place(x=235,y=130)

    global username
    global password
    username=StringVar()
    password=StringVar()

    username=gold.Entry(frame1)
    username.place(x=300,y=100)

    password=gold.Entry(frame1)
    password.config(show='*')
    password.place(x=300,y=130)

    buttonLogin=gold.Button(frame1,text='Login',bg='orange',command=lambda:checkLogin(client))
    buttonLogin.place(x=310,y=170)

    buttonRegister=gold.Button(frame1,text='Register',bg='orange',command=lambda:registerAccount(client))
    buttonRegister.place(x=370,y=170)

#login_page(client)
login_page()
window.mainloop()