import tkinter as tk, requests
from tkinter import messagebox

root = tk.Tk()
entry = tk.Entry()

def SetLikeGeometry():
    root.geometry('1000x350')

def Request():

    try:

        global data

        city = entry.get()
        appid = 'ffd367d42caa2e04d9b6846d3a9f6d07'

        result = requests.get('http://api.openweathermap.org/data/2.5/find',
        params={'q': city, 'type': 'like', 'units': 'metric', 'lang': 'ru', 'APPID': appid})

        data = result.json()

        SetLikeGeometry()

        ObjWeather4.configure(text='\nОсновная информация о погоде:')

        ObjWeather5.configure(text='Средняя температура в реальном времени: {0} C'.format(data['list'][0]['main']['temp']))
        ObjWeather6.configure(text='Минимальная ожидаемая температура в реальном времени: {0} C'.format(data['list'][0]['main']['temp_min']))
        ObjWeather7.configure(text='Максимальная ожидаемая температура в реальном времени: {0} C'.format(data['list'][0]['main']['temp_max']))
        ObjWeather8.configure(text='Без дождливых осадков' if data['list'][0]['rain'] == None else 'Имеются дождливые осадки' + '| Без снегопада' if data['list'][0]['snow'] == None else 'Проходит снегопад')
        ObjWeather9.configure(text='Облачность: {} %'.format(data['list'][0]['clouds']['all']))
        ObjWeather10.configure(text='Атмосферное давление рт. ст.: {0}'.format(data['list'][0]['main']['pressure']))

        ObjWeather11.configure(text='\nДополнительная информация о погоде:\n')

        ObjWeather12.configure(text='Скорость ветра: {0} м/с'.format(data['list'][0]['wind']['speed']))
        ObjWeather13.configure(text='Влажность в реальном времени: {0} %'.format(data['list'][0]['main']['humidity']))

    except:

        if data['message'] == 'Nothing to geocode':
            root.geometry('400x100')
            root.configure(bg='RED')

            messagebox.showerror(title='Weatherca', message='Поле для ввода города/региона пусто или содержит некорректные символы.')
            
            root.configure(bg='DARK BLUE')
            return

        else:

            root.configure(bg='RED')
            root.geometry('400x100')

            messagebox.showerror(title='Weatherca', message='Произошла неизвестная ошибка в ходе исполнения программы. Попробуйте перезапустить программу.')
            
            root.configure(bg='DARK BLUE')

root.geometry('400x100')
root.title('Weatherca')
root.configure(background='DARK BLUE')

cityreceive = tk.Label(text='В каком городе вы хотите определить погодную информацию?')
buttcity = tk.Button(text='Далее', command=Request)
ObjWeather1 = tk.Label()
ObjWeather2 = tk.Label()
ObjWeather3 = tk.Label()
ObjWeather4 = tk.Label()
ObjWeather5 = tk.Label()
ObjWeather6 = tk.Label()
ObjWeather7 = tk.Label()
ObjWeather8 = tk.Label()
ObjWeather9 = tk.Label()
ObjWeather10 = tk.Label()
ObjWeather11 = tk.Label()
ObjWeather12 = tk.Label()
ObjWeather13 = tk.Label()

cityreceive.pack()
entry.pack()
buttcity.pack()


ObjWeather4.pack()
ObjWeather5.pack()
ObjWeather6.pack()
ObjWeather7.pack()
ObjWeather8.pack()
ObjWeather9.pack()
ObjWeather10.pack()
ObjWeather11.pack()
ObjWeather12.pack()
ObjWeather13.pack()


root.mainloop()