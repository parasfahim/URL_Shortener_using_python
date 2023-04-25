import pyperclip
import pyshorteners
from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("URL Shortener")
root.configure(bg="purple")
url = StringVar()
url_address = StringVar()

def urlshortener():
    urladdress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_short)

def copyurl():
    url_short = url_address.get()
    pyperclip.copy(url_short)

Label(root, text="URL SHORTENER", font=("poppins", 20, "bold"), bg="purple").place(x=80,y=35)
Entry(root, textvariable=url, width = 40).place(x=80,y=100)
Button(root, text="Generate Short URL", command=urlshortener, font=("poppins", 12, "bold")).place(x=118,y=130)
Entry(root, textvariable=url_address, width = 40).place(x=80,y=190)
Button(root, text="Copy URL", command=copyurl, font=("poppins", 12, "bold")).place(x=155,y=220)

root.mainloop()