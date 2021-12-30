import tkinter as gold
from tkinter import  StringVar, messagebox
from tkinter import ttk
import re
from tkinter.constants import END
import server as s

window = gold.Tk()

window.title("Johny Dang & Co. Server")
window.geometry("720x480")
window.resizable(width=False, height=False)
window.iconbitmap('gold.ico')


frame2 = gold.Frame(window)

def close_App(server):
    if messagebox.askokcancel("Exit", "Do you want to exit?"):
        s.closeServer(server)
        window.destroy()

def homePage():
    sThread = s.threading.Thread(target=s.Start)
    sThread.daemon = True 
    sThread.start() 

    def seeConnection():
        board.delete(0, len(s.client_online))
        for i in range(len(s.client_online)):
            board.insert(i, s.client_online[i])

    frame2.pack(fill="both", expand=1)
    page_name = gold.Label(frame2, text="Gold Price (server)", font=("Times new roman",23, "bold"), foreground="orange")
    page_name.place(x=234, y=11)
    
    quit_button = gold.Button(frame2, text='Exit', bg='red', width=10, command=lambda:close_App(s.s))
    quit_button.place(x=617,y = 430)
    
    user_info = gold.Label(frame2, text=("Server IP: " + str(s.HOST) + "   Port: " + str(s.PORT)))
    user_info.place(x=10, y=450)

    refresh_button = gold.Button(frame2,text = "Reload", bg='orange',width=8,command=seeConnection)
    refresh_button.place(x = 632, y=51) 
    
    clients = gold.Label(frame2, text="Clients online:", font=("Arial",12))
    clients.place(x=5, y=68)

    global board
    board = gold.Listbox(frame2,font = ("Times new roman",15), width=69, height=14)
    scrollbar  = gold.Scrollbar(frame2, orient="vertical", command=board.yview)
    board['yscroll'] = scrollbar.set
    scrollbar.place(in_=board, relx=1.0, relheight=1.0, bordermode="outside")
    board.place(x=5, y=88)

homePage()

window.mainloop()