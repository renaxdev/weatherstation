from tkinter import *
from tkinter import Tk, messagebox
import requests
import json
from PIL import ImageTk, Image
import os

token = "6942eb75679c8b5081e70754e8d73dba"
url = f"https://api.openweathermap.org/data/2.5/weather?q=Wolfsburg&appid={token}&units=metric"

snow = [600, 601, 602, 611, 612, 613, 615, 616, 620, 621, 622]
rain = [500, 501, 502, 503, 504, 511, 520, 521, 522, 531]
sun = [800, 801]
clouds = [802, 803, 804]
storm = [200, 201, 202, 210, 211, 212, 221, 230, 231, 232]

fenster = Tk()
fenster.geometry("400x350")
fenster.title("Wetter Station")

def request():
    auswahl = control_variable.get()
    print(auswahl)
    if auswahl == "Indoor":
        print("Indoor")

    if auswahl == "Outdoor":
        resp = requests.get(url)
        re = resp.json()
        status = re["cod"]       
        temp = re["main"]["temp"]
        hum = re["main"]["humidity"]
        weather_id = re["weather"][0]["id"]
        labelframe_widget = LabelFrame(fenster, text="Werte")
        label_widget = Label(labelframe_widget,text=f"Temperatur: {temp} C° \n Feuchte: {hum}%")
        labelframe_widget.pack(padx=10, pady=10)
        label_widget.pack()
        if weather_id in rain:
            panel = Label(fenster, image = img_rain)
            panel.pack(side = "bottom", fill = "both", expand = "yes")
        
        if weather_id in clouds:
            panel = Label(fenster, image = img_clouds)
            panel.pack(side = "bottom", fill = "both", expand = "yes")

        if weather_id in storm:
            panel = Label(fenster, image = img_storm)
            panel.pack(side = "bottom", fill = "both", expand = "yes")

        if weather_id in sun:
            panel = Label(fenster, image = img_sun)
            panel.pack(side = "bottom", fill = "both", expand = "yes")
        
        if weather_id in snow:
            panel = Label(fenster, image = img_snow)
            panel.pack(side = "bottom", fill = "both", expand = "yes")





img_rain = ImageTk.PhotoImage(Image.open("rain.jpg"))
img_sun = ImageTk.PhotoImage(Image.open("sun.jpg"))
img_storm = ImageTk.PhotoImage(Image.open("storm.jpg"))
img_snow = ImageTk.PhotoImage(Image.open("snow.jpg"))
img_clouds = ImageTk.PhotoImage(Image.open("clouds.jpg"))

title_label = Label(fenster, text="-----WETTERSTATION-----", font="Impact")
title_label.pack(side=TOP)

control_variable = StringVar(fenster)
OPTION_TUPLE = ("Indoor", "Outdoor") 
optionmenu_widget = OptionMenu(fenster, control_variable, *OPTION_TUPLE)
control_variable.set("Indoor")
optionmenu_widget.pack()


button = Button(fenster, text="Show Data", command=request)
button.pack()

fenster.mainloop()