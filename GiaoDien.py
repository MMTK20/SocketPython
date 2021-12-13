import tkinter as gold
from tkinter import StringVar, messagebox
import re
window= gold.Tk()

window.title('Johnny Dang & Co.')
window.geometry('720x480')
window.iconbitmap('gold.ico')


def check_login():
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
        messagebox.showinfo('test','Login successful!')

def main():
    menu=gold.Label(window,text='Gold Price', font=('Times new roman',35),foreground='orange').place(x=260,y=20)

    nametag=gold.Label(window,text='Username').place(x=235,y=100)
    passtag=gold.Label(window,text='Password').place(x=235,y=130)
    global username
    global password
    username=StringVar()
    password=StringVar()
    username=gold.Entry(window)
    username.place(x=300,y=100)
    password=gold.Entry(window)
    password.config(show='*')
    password.place(x=300,y=130)
    button=gold.Button(window,text='Login',bg='orange',command=check_login).place(x=330,y=170)
main()
window.mainloop()