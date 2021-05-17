# Simple Weather-Station

![](https://cdn.discordapp.com/attachments/825669056719355908/843570629260214332/39416535-4d358eca-4c6b-11e8-981b-733298f1d643.png)

This program is a Simple Weather-Station written in Python.
It can measure the humidity and temperature from outside (via OpenWeatherMap)
and it can measure the humidity and temperature from a DHT11 Sensor (on Raspberry Pi)

## Features

- Measure Temperature & Humidity from Outside (via OpenWeatherMap) (Outdoor Mode)
- Measure Temperature & Humidity from Inside (DHT11 with RPi) (Indoor Mode)
- Show a fitting icon to the weather from outside (Sunny Weather --> Sun Icon ; Rainy Weather --> Rain Icon)
- Fullscreen Mode (after you press the "Exit Fullscreen" Button you wont be able to open the fullscreen again until you restarted the script)
- Exit Button for closing the program 
- Error Handling (No Internet connection = Error Box)
- An easy to use GUI with Tkinter
- Live Clock

## Installation & Usage:

### Windows
- Disclaimer: You wont be able to use the Indoor mode in Windows.
1. Download and Install the newest version of Python3
2. Open the command prompt and type:  `python -m pip install Pillow` 
3. Then type(If not installed): `python -m pip install requests`
4. ^ : `python -m pip install json`
5. Then, you need to register on the [OpenWeatherMap Website](https://openweathermap.org/ "OpenWeatherMap Website")
6. Then, go to "Profile > API Keys and copy the long API key. (it contains random numbers and letters)
7. Open the Script in any text editor and paste the copied API Key into the `token` variable
8. In the script, edit the variable `city` for any city you want to get the data from
9. Run the script
10. Press the `Show data` button to show the data

### Linux
- Disclaimer: You wont be able to use the Indoor mode in Linux Computers EXCEPT the Raspberry Pi with a DHT11.
1. Open the terminal and type: `sudo apt-get update -y && sudo apt-get upgrade -y`
2. Download and Install the newest version of Python3: `sudo apt-get install python3`
3. Open the command prompt and type:  `sudo pip3 install Pillow` OR  `sudo python -m pip install Pillow`
4. Then type(If not installed): `sudo pip3 install requests` OR  `sudo python -m pip install requests`
5. ^ : `sudo pip3 install json` OR  `sudo python -m pip install json`
6. Then, you need to register on the [OpenWeatherMap Website](https://openweathermap.org/ "OpenWeatherMap Website")
7. Then, go to "Profile > API Keys and copy the long API key. (it contains random numbers and letters)
8. Open the Script in any text editor and paste the copied API Key into the `token` variable
9. In the script, edit the variable `city` for any city you want to get the data from
10. Run the script
11. Press the `Show data` button to show the data 
12. FOR RASPBERRY PI ONLY: For Indoor Data, click on the options menu and choose `Indoor`


## try:
... to run the script and get correct data

## except errors:
- 