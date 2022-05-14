import tkinter as tk
import requests


API_KEY = '28f0fad9a32955ccd41135dadbad75c8'


def search():
    city = city_entry.get()
    weather = get_weather(city)
    
    location_label['text'] = f'{weather[0]}, {weather[1]}'
    img['file'] = f'weather_icons/{weather[3]}.png'
    weather_label['text'] = f'{weather[4]}'
    temp_label['text'] = f'Temperature: {weather[2]:.0f}°C'
    

def get_weather(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}'
    response = requests.get(url)
    data = response.json()
    
    city = data["name"]
    country = data['sys']['country']
    temp = data['main']['temp']-273.15
    icon = data['weather'][0]['icon']
    weather = data['weather'][0]['main']
    final = (city, country, temp, icon, weather)
    
    return final


# root app
root = tk.Tk()
# root.configure(bg="#64C5C8")
root.title("Weather")
root.geometry('300x300')

# city enter fielt
city_entry = tk.Entry(root, font=14, width=300, justify="center")
city_entry.pack()

# widget for presenting city location
location_label = tk.Label(root, text="City", font=("bold", 20))
location_label.pack()

# weather image widget and it photo
img = tk.PhotoImage(file='')
weather_image = tk.Label(root, image=img)
weather_image.pack()

# weather amount widget
weather_label = tk.Label(root, text="Weather", font=11)
weather_label.pack()

# temperature of weather
temp_label = tk.Label(root, text="Temperature", font=11)
temp_label.pack()

# search button
search_button = tk.Button(root, text="Find weather", font=14, command=search)
search_button.pack()


root.mainloop()