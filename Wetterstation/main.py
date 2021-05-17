from tkinter import *
from tkinter import Tk, messagebox, simpledialog
import requests
import json
from PIL import ImageTk, Image
import os
import time

token = "6942eb75679c8b5081e70754e8d73dba" #API key from openweathermap.org --> Profile > API Keys
city = "Wolfsburg" #City 
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&units=metric"

snow = [600, 601, 602, 611, 612, 613, 615, 616, 620, 621, 622]
rain = [500, 501, 502, 503, 504, 511, 520, 521, 522, 531]
sun = [800, 801]
clouds = [802, 803, 804]
storm = [200, 201, 202, 210, 211, 212, 221, 230, 231, 232]

fenster = Tk()
fenster.geometry("500x500")
fenster.attributes("-fullscreen", True)
fenster.configure(bg="#b3d0ff")
fenster.title("Wetter Station")

def close():
    fenster.destroy()

def exit_fs():
    fenster.attributes("-fullscreen", False)

def request():
    auswahl = control_variable.get()
    if auswahl == "Indoor":
        print("Indoor")

    if auswahl == "Outdoor":
        try:
            resp = requests.get(url)
            re = resp.json()
            status = re["cod"]       
            temp = re["main"]["temp"]
            hum = re["main"]["humidity"]
            weather_id = re["weather"][0]["id"]
            labelframe_widget = LabelFrame(fenster, text="Werte", bg="#b3d0ff")
            labelframe_widget.config(font=("Arial", 25))
            label_widget = Label(labelframe_widget,text=f"🌡 - Temperatur: {temp} C°", fg="blue", bg="#b3d0ff")
            label_widget2 = Label(labelframe_widget,text=f"💧 - Feuchte: {hum}%", fg="red", bg="#b3d0ff")
            label_widget.config(font=("Arial", 30))
            label_widget2.config(font=("Arial", 30))
            labelframe_widget.pack(padx=10, pady=10)
            label_widget.pack()
            label_widget2.pack()

            if weather_id in rain:
                panel = Label(fenster, text="🌧", bg="#b3d0ff")
                panel.config(font=("Courier", 70))
                panel.pack()
        
            if weather_id in clouds:
                panel = Label(fenster, text="☁", bg="#b3d0ff")
                panel.config(font=("Courier", 70))
                panel.pack()

            if weather_id in storm:
                panel = Label(fenster, text="⛈", bg="#b3d0ff")
                panel.config(font=("Courier", 70))
                panel.pack()

            if weather_id in sun:
                panel = Label(fenster, text="☀", bg="#b3d0ff")
                panel.config(font=("Courier", 70))
                panel.pack()
        
            if weather_id in snow:
                panel = Label(fenster, text="🌨", bg="#b3d0ff")
                panel.config(font=("Courier", 70))
                panel.pack()

        except requests.exceptions.ConnectionError:
            messagebox.showerror("Connection Error", "Fehler bei der Verbindung zum Server")           


title_label = Label(fenster, text="-----WETTERSTATION-----", bg="#b3d0ff")
title_label.config(font=("Courier", 44))
title_label.pack(side=TOP)

zeit = ''
def tick(  ):
    global zeit
    neuezeit = time.strftime('%H:%M:%S')
    if neuezeit != zeit:
        zeit = neuezeit
        uhr.config(text = zeit) 
        fenster.title(f"Wetter Station | {zeit}")
    uhr.after(200, tick) 

uhr = Label(fenster, bg="#b3d0ff")
uhr.pack()
 

control_variable = StringVar(fenster)
OPTION_TUPLE = ("Indoor", "Outdoor") 
optionmenu_widget = OptionMenu(fenster, control_variable, *OPTION_TUPLE)
control_variable.set("Indoor")
optionmenu_widget.pack()

button = Button(fenster, text="Show Data", command=request)
button.pack()

exit_button = Button(fenster, text="Close", bg="Red", command=close)
exit_button.pack(side=BOTTOM)

exit_fullscreen = Button(fenster, text="Exit Fullscreen", bg="Red", command=exit_fs)
exit_fullscreen.pack(side=BOTTOM)

tick()
fenster.mainloop()