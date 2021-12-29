import tkinter as gold
from tkinter import  StringVar, messagebox
from tkinter import ttk
import re
from tkinter.constants import END
import socket


#Đóng gói hàm lại, không gọi hàm ở ngoài như thế này
window = gold.Tk()

window.title("Johny Dang & Co. Server")

window.geometry("720x480")
window.resizable(width=False, height=False)
window.iconbitmap('gold.ico')


frame2 = gold.Frame(window)

HOST = socket.gethostbyname(socket.gethostname())
PORT = 3702
# Thoát chương trình
def close_App():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()

# trang chính
def homePage():

    frame2.pack(fill="both", expand=1)
    page_name = gold.Label(frame2, text="SERVER", font=("Times new roman",20, "bold"), foreground="orange")
    page_name.place(x=270)
    
    quit_button = gold.Button(frame2, text='Quit',width=10, command=lambda:close_App())
    quit_button.place(x=600,y = 10)
    
    user_info = gold.Label(frame2, text=("Server: " + str(HOST) + "  -  " + str(PORT)))
    user_info.place(x=240, y=55)
    refresh_button = gold.Button(frame2,text = 'REFRESH', bg='orange',width=15)
    refresh_button.place(x = 280, y=430)
    
    global txt
    txt = gold.Listbox(frame2,font = ("Times new roman",15), width=45, height=12)
    scrollbar  = gold.Scrollbar(frame2, orient="vertical", command=txt.yview)
    txt['yscroll'] = scrollbar.set
    scrollbar.place(in_=txt, relx=1.0, relheight=1.0, bordermode="outside")
    txt.place(x=100, y=80)

homePage()

window.mainloop()