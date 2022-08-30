# from cgitb import text
# from re import search
from tkinter import *
import tkinter as tk
# from turtle import color
from geopy.geocoders import Nominatim
# from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk


# for user interface
root = Tk()
root.title("Weather Check")
root.geometry("890x470+300+200")
root.configure(bg="aqua")
root.resizable(False, False)


# setting tkinter window size
# width = root.winfo_screenwidth()
# height = root.winfo_screenheight()
# root.geometry("%dx%d" % (width, height))

# function


def getWeather():
    city = text_field.get()

    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(city)
    obj = TimezoneFinder()

    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    timezone.config(text=result)
    long_lat.config(
        text=f"{round(location.latitude,4)}°N,{round(location.longitude,4)}°E")

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text=current_time)

    # weather-api-for-weather-data
    api = "https://api.openweathermap.org/data/2.5/onecall?lat="+str(location.latitude)+"&lon="+str(
        location.longitude)+"&units=metric&exclude=hourly&appid=646824f2b7b86caffec1d0b16ea77f79"
    json_data = requests.get(api).json()

    # current
    temp = json_data["current"]["temp"]
    humidity = json_data["current"]["humidity"]
    pressure = json_data["current"]["pressure"]
    wind = json_data["current"]["wind_speed"]
    description = json_data["current"]["weather"][0]["description"]
    # print(temp)
    # print(humidity)
    # print(pressure)
    # print(wind)
    # print(description)

    t.config(text=(temp, "°C"))
    h.config(text=(humidity, "%"))
    p.config(text=(pressure, "hPa"))
    w.config(text=(wind, "m/s"))
    d.config(text=description)

    # first-cell
    firstDayImage = json_data['daily'][0]['weather'][0]['icon']
    # print(firstDayImage)
    photo1 = ImageTk.PhotoImage(file=f"icon/{firstDayImage}@2x.png")
    firstImage.config(image=photo1)
    firstImage.image = photo1

    temp_day1 = json_data['daily'][0]['temp']['day']
    temp_night1 = json_data['daily'][0]['temp']['night']

    day1_temp.config(text=f"Day:{temp_day1}\n Night:{temp_night1}")

    # second-cell
    secondDayImage = json_data['daily'][1]['weather'][0]['icon']
    print(secondDayImage)
    img = (Image.open(f"icon/{secondDayImage}@2x.png"))
    resized_image = img.resize((50, 50))
    photo2 = ImageTk.PhotoImage(resized_image)
    secondImage.config(image=photo2)
    secondImage.image = photo2

    temp_day2 = json_data['daily'][1]['temp']['day']
    temp_night2 = json_data['daily'][1]['temp']['night']

    day2_temp.config(text=f"Day:{temp_day2}\n Night:{temp_night2}")

    # third-cell
    thirdDayImage = json_data['daily'][2]['weather'][0]['icon']
    print(thirdDayImage)
    img = (Image.open(f"icon/{thirdDayImage}@2x.png"))
    resized_image = img.resize((50, 50))
    photo3 = ImageTk.PhotoImage(resized_image)
    thirdImage.config(image=photo3)
    thirdImage.image = photo3

    temp_day3 = json_data['daily'][2]['temp']['day']
    temp_night3 = json_data['daily'][2]['temp']['night']

    day3_temp.config(text=f"Day:{temp_day3}\n Night:{temp_night3}")

    # fourth-cell
    fourthDayImage = json_data['daily'][3]['weather'][0]['icon']
    print(fourthDayImage)
    img = (Image.open(f"icon/{fourthDayImage}@2x.png"))
    resized_image = img.resize((50, 50))
    photo4 = ImageTk.PhotoImage(resized_image)
    fourthImage.config(image=photo4)
    fourthImage.image = photo4

    temp_day4 = json_data['daily'][3]['temp']['day']
    temp_night4 = json_data['daily'][3]['temp']['night']

    day4_temp.config(text=f"Day:{temp_day4}\n Night:{temp_night4}")

    # fifth-cell
    fifthDayImage = json_data['daily'][4]['weather'][0]['icon']
    print(fifthDayImage)
    img = (Image.open(f"icon/{fifthDayImage}@2x.png"))
    resized_image = img.resize((50, 50))
    photo5 = ImageTk.PhotoImage(resized_image)
    fifthImage.config(image=photo5)
    fifthImage.image = photo5

    temp_day5 = json_data['daily'][4]['temp']['day']
    temp_night5 = json_data['daily'][4]['temp']['night']

    day5_temp.config(text=f"Day:{temp_day5}\n Night:{temp_night5}")

    # sixth-cell
    sixthDayImage = json_data['daily'][5]['weather'][0]['icon']
    print(sixthDayImage)
    img = (Image.open(f"icon/{sixthDayImage }@2x.png"))
    resized_image = img.resize((50, 50))
    photo6 = ImageTk.PhotoImage(resized_image)
    sixthImage.config(image=photo6)
    sixthImage.image = photo6

    temp_day6 = json_data['daily'][5]['temp']['day']
    temp_night6 = json_data['daily'][5]['temp']['night']

    day6_temp.config(text=f"Day:{temp_day6}\n Night:{temp_night6}")

    # seventh-cell
    seventhDayImage = json_data['daily'][6]['weather'][0]['icon']
    print(seventhDayImage)
    img = (Image.open(f"icon/{seventhDayImage}@2x.png"))
    resized_image = img.resize((50, 50))
    photo7 = ImageTk.PhotoImage(resized_image)
    seventhImage.config(image=photo7)
    seventhImage.image = photo7

    temp_day7 = json_data['daily'][6]['temp']['day']
    temp_night7 = json_data['daily'][6]['temp']['night']

    day7_temp.config(text=f"Day:{temp_day7}\n Night:{temp_night7}")

    # days
    # a=datetime.now()
    # day1.config()
    first = datetime.now()
    day1.config(text=first.strftime("%A"))

    second = first+timedelta(days=1)
    day2.config(text=second.strftime("%A"))

    third = first+timedelta(days=2)
    day3.config(text=third.strftime("%A"))

    fourth = first+timedelta(days=3)
    day4.config(text=fourth.strftime("%A"))

    fifth = first+timedelta(days=4)
    day5.config(text=fifth.strftime("%A"))

    sixth = first+timedelta(days=5)
    day6.config(text=sixth.strftime("%A"))

    seventh = first+timedelta(days=6)
    day7.config(text=seventh.strftime("%A"))


# icon
image_icon = PhotoImage(file="images/weather-app.png")
root.iconphoto(False, image_icon)

# round-box1
round_box = PhotoImage(file="images/bottom-box1.png")
Label(root, image=round_box, bg="aqua").place(x=10, y=100.5)

# label1
label1 = Label(root, text="Temperature:", font=(
    'cascadia code semibold', 9), fg="white", bg="black")
label1.place(x=24, y=120)

# label2
label2 = Label(root, text="Humidity :", font=(
    'cascadia code semibold', 9), fg="white", bg="black")
label2.place(x=24, y=140)

# label3
label3 = Label(root, text="Pressure :", font=(
    'cascadia code semibold', 9), fg="white", bg="black")
label3.place(x=24, y=160)

# label4
label4 = Label(root, text="Wind Speed :", font=(
    'cascadia code semibold', 9), fg="white", bg="black")
label4.place(x=24, y=180)

# label5
label5 = Label(root, text="Description :", font=(
    'cascadia code semibold', 9), fg="white", bg="black")
label5.place(x=24, y=200)


# search-box
search_image = PhotoImage(file="images/search-box.png")
my_image = Label(image=search_image, bg="aqua")
my_image.place(x=270, y=120)

weather_image = PhotoImage(file="images/weather-image.png")
weatherImage = Label(root, image=weather_image, bg="#203243")
weatherImage.place(x=290, y=127)

text_field = tk.Entry(root, justify='center', width=15, font=(
    'poppins', 25, 'bold'), bg="#203243", border=0, fg="white")
text_field.place(x=370, y=130)
text_field.focus()

search_icon = PhotoImage(file="images/search-icon.png")
searchIcon = Button(image=search_icon, borderwidth=0,
                    cursor="hand2", bg="#203243", command=getWeather)
searchIcon.place(x=645, y=125)

# bottom-box
frame = Frame(root, width=900, height=180, bg="#212120")
frame.pack(side=BOTTOM)

# bottom-inner-boxes
firstBox = PhotoImage(file="images/bottom-box11.png")
secondBox = PhotoImage(file="images/bottom-box2.png")

Label(frame, image=firstBox, bg="#212120").place(x=30, y=20)
Label(frame, image=secondBox, bg="#212120").place(x=300, y=30)
Label(frame, image=secondBox, bg="#212120").place(x=400, y=30)
Label(frame, image=secondBox, bg="#212120").place(x=500, y=30)
Label(frame, image=secondBox, bg="#212120").place(x=600, y=30)
Label(frame, image=secondBox, bg="#212120").place(x=700, y=30)
Label(frame, image=secondBox, bg="#212120").place(x=800, y=30)


# clock
clock = Label(root, font=("cascadia code semibold",
              30, 'bold'), fg="white", bg="aqua")
clock.place(x=30, y=20)

# timezone
timezone = Label(root, font=("cascadia code semibold", 20),
                 fg="white", bg="aqua")
timezone.place(x=700, y=20)

long_lat = Label(root, font=("cascadia code semibold", 10),
                 fg="white", bg="aqua")
long_lat.place(x=700, y=50)


# thpwd
t = Label(root, font=("cascadia code semibold", 10), fg="white", bg="black")
t.place(x=110, y=120)
h = Label(root, font=("cascadia code semibold", 10), fg="white", bg="black")
h.place(x=110, y=140)
p = Label(root, font=("cascadia code semibold", 10), fg="white", bg="black")
p.place(x=110, y=160)
w = Label(root, font=("cascadia code semibold", 10), fg="white", bg="black")
w.place(x=110, y=180)
d = Label(root, font=("cascadia code semibold", 10), fg="white", bg="black")
d.place(x=110, y=200)


# first-cell
firstFrame = Frame(root, width=230, height=132, bg="#282829")
firstFrame.place(x=35, y=315)

day1 = Label(firstFrame, font="arial 20", bg="#282829", fg="#fff")
day1.place(x=100, y=5)
firstImage = Label(firstFrame, bg="#282829")
firstImage.place(x=1, y=15)

day1_temp = Label(firstFrame, bg="#282829", fg="white", font="arial 15 bold")
day1_temp.place(x=100, y=50)


# second-cell
secondFrame = Frame(root, width=70, height=115, bg="#282829")
secondFrame.place(x=305, y=325)
day2 = Label(secondFrame, font="arial 8", bg="#282829", fg="#fff")
day2.place(x=10, y=5)
secondImage = Label(secondFrame, bg="#282829")
secondImage.place(x=7, y=20)

day2_temp = Label(secondFrame, bg="#282829", fg="#fff")
day2_temp.place(x=10, y=70)


# third-cell
thirdFrame = Frame(root, width=70, height=115, bg="#282829")
thirdFrame.place(x=405, y=325)
day3 = Label(thirdFrame, font="arial 8", bg="#282829", fg="#fff")
day3.place(x=10, y=5)
thirdImage = Label(thirdFrame, bg="#282829")
thirdImage.place(x=7, y=20)

day3_temp = Label(thirdFrame, bg="#282829", fg="#fff")
day3_temp.place(x=10, y=70)


# fourth-cell
fourthFrame = Frame(root, width=70, height=115, bg="#282829")
fourthFrame.place(x=505, y=325)
day4 = Label(fourthFrame, font="arial 8", bg="#282829", fg="#fff")
day4.place(x=10, y=5)
fourthImage = Label(fourthFrame, bg="#282829")
fourthImage.place(x=7, y=20)

day4_temp = Label(fourthFrame, bg="#282829", fg="#fff")
day4_temp.place(x=10, y=70)


# fifth-cell
fifthFrame = Frame(root, width=70, height=115, bg="#282829")
fifthFrame.place(x=605, y=325)
day5 = Label(fifthFrame, font="arial 8", bg="#282829", fg="#fff")
day5.place(x=10, y=5)
fifthImage = Label(fifthFrame, bg="#282829")
fifthImage.place(x=7, y=20)

day5_temp = Label(fifthFrame, bg="#282829", fg="#fff")
day5_temp.place(x=10, y=70)


# sixth-cell
sixthFrame = Frame(root, width=70, height=115, bg="#282829")
sixthFrame.place(x=705, y=325)
day6 = Label(sixthFrame, font="arial 8", bg="#282829", fg="#fff")
day6.place(x=10, y=5)
sixthImage = Label(sixthFrame, bg="#282829")
sixthImage.place(x=7, y=20)

day6_temp = Label(sixthFrame, bg="#282829", fg="#fff")
day6_temp.place(x=10, y=70)


# seventh-cell
seventhFrame = Frame(root, width=70, height=115, bg="#282829")
seventhFrame.place(x=805, y=325)
day7 = Label(seventhFrame, font="arial 8", bg="#282829", fg="#fff")
day7.place(x=10, y=5)
seventhImage = Label(seventhFrame, bg="#282829")
seventhImage.place(x=7, y=20)

day7_temp = Label(seventhFrame, bg="#282829", fg="#fff")
day7_temp.place(x=10, y=70)


root.mainloop()
