# # import smtplib, ssl
# # smtp_server = 'smtp.gmail.com'
# # port = 465
# # sender = 'sreedhargit@gmail.com'
# # password=input('Enter your password here')
# # context = ssl.create_default_context()
# # with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
# #     server.login(sender, password)
# #     print("in gmail")
#
import requests
#
#
# from tkinter import *
#
# def get_quote():
#     response = requests.get(url="https://api.kanye.rest")
#     response.raise_for_status()
#     data = response.json()
#     quote = data['quote']
#     canvas.itemconfig(quote_text, text=quote)
# window = Tk()
# window.title("Kanye says...")
# window.config(padx=50, pady=50)
# canvas=Canvas(width=300, height=414)
# background_img = PhotoImage(file="img.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250)
# canvas.grid(row=0, column=0)
#
# Kanye_img = PhotoImage(file="Kanye.png")
# Kanye_button = Button(image=Kanye_img, highlightthickness=0, command=get_quote)
# Kanye_button.grid(row=1, column=0)
#
#
# window.mainloop()

import datetime

My_LAT = 34.345012
My_Lon = -0.125543

def is_iss_overhead():
    response = requests.get("https://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if My_LAT - 5 <= iss_latitude <= My_LAT + 5 and My_Lon -5 <= iss_longitude <= My_Lon + 5:
        return True
    

parameters = {
    "lat" : My_LAT,
    "lon" : My_Lon,
    "formatted" : 0
}


sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
sunrise_hour = sunrise.split("T")[1].split(":")[0]
sunset_hour = sunset.split("T")[1].split(":")[0]
current_hour = datetime.datetime.now().hour
print((sunrise_hour, sunset_hour))
print(current_hour)


