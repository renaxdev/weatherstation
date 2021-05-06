from tkinter import *
from tkinter import Tk, messagebox, simpledialog
import requests
import json

fenster = Tk()
fenster.geometry("350x250")

fenster.title("Show Weather")

def callback(selection):
    global choice
    choice = selection

def request_call():
    city = textfeld.get()
    token = "6942eb75679c8b5081e70754e8d73dba"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}appid={token}&units=metric"
    resp = requests.get(url)
    re = resp.json()
    temp = re['main']['temp']
    hum = re["main"]["humidity"]
    if choice == "Temperature":
        messagebox.showinfo("Temperature", f"Die Temperatur in {city} beträgt {temp} C°")

    elif choice == "Humidity":
        messagebox.showinfo("Humidity", f"DIe Feuchtigkeit in {city} beträgt {hum}%")

  
label1 = Label(fenster, text="Hallo Welt")
label1.pack()

options = StringVar()
menu = OptionMenu(fenster, options, 'Temperature', 'Humidity', command=callback)
menu.pack()
options.set('Temperature')

textfeld = Entry(fenster)
textfeld.pack()

buttonreq = Button(fenster,text="Send Request", command=request_call)
buttonreq.pack()


fenster.mainloop()