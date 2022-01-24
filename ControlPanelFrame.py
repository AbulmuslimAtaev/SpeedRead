import tkinter as tk
from CreateToolTip import *

# base64 иконок
pause_ = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAQAAADZc7J/AAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAAmJLR0QAAKqNIzIAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAAHdElNRQfkBAUSMzvZnV7MAAAAoklEQVRIx+2VOwrCQBRFTz5MpV1IIYKt6A6yjWwhnb1CViBuwO2I1pZ2NkpMaWHpv5DIPDIDgu27U907hzPlBORMiWjnTMHx24Ys6TqoG2x5eU5pgQsfFWOAK5XwGvqAEQvAgYfgBkQxAHvG4mLEDlcyatFP9EL+jApUoAIVqEAFdj4/U8JMrKmHnnARvdMIUuY/PVe2p5CVB76zsdqapxt7A1pCLl6RYXB/AAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDIwLTA0LTA1VDE4OjUxOjU5KzAwOjAwG0wI1gAAACV0RVh0ZGF0ZTptb2RpZnkAMjAyMC0wNC0wNVQxODo1MTo1OSswMDowMGoRsGoAAAAZdEVYdFNvZnR3YXJlAHd3dy5pbmtzY2FwZS5vcmeb7jwaAAAAAElFTkSuQmCC'
play_ = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAQAAADZc7J/AAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAAmJLR0QAAKqNIzIAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAAHdElNRQfkBAUSMxB1IaeMAAABCElEQVRIx73VLUvDURQH4GcTEVQU1GQwGEwmk0WLTfAr/G0GDfsKg2WFNa1+ARFBm81kcMVisQgLwkRQZPhyLJNZPRe8/T5w7j3nd4A9Tw5MSZ9zIXRtq5UAIVxbzQInToXw6chcBmhjw60QehpGMgCjGp6F0LGWAWDesS8hnFnIALCuI4RXTWMZgLrKoxDubGYAmNH2MShmMQPAiish9LVNZgBqKl0hPKgyAExo6gvh0nIGgCUXQnjXNp0BYMv9YPB21DMA41rehNDCb6Xk/FMJRY9Y9I2FjVTUykXDVDjOP4HykgmUokgbhupNJlSLYn24WA7N/uXyD1C82kJXlV2uu3r2c+v9G6kqv5QdbaipAAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDIwLTA0LTA1VDE4OjUxOjE2KzAwOjAwaU52xQAAACV0RVh0ZGF0ZTptb2RpZnkAMjAyMC0wNC0wNVQxODo1MToxNiswMDowMBgTznkAAAAZdEVYdFNvZnR3YXJlAHd3dy5pbmtzY2FwZS5vcmeb7jwaAAAAAElFTkSuQmCC'
prev_ = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAQAAADZc7J/AAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAAmJLR0QAAKqNIzIAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAAHdElNRQfkBAUSNxgfluq6AAAA70lEQVRIx+3UrU5DQRRF4Y+mAkWCqMBU19fhkDgMr9BXqEPzFDwACTgcRSIqGjwKgUAgSEgIJM1BzIVA2zsNHAnLzaydSeZv8886hm5c/cKBrrFXIX7oGgamwnxlqObAhpFn4c7eUqjmGvouhXBqm4VQ36TVNRx6FB4cNOOvoZoDPWdCuLDzOfcR6jlvdQ377oUno2+LllDNgS0nQpjoL2wpRNWBXbfCi7HO0pmEqDqbjs2FqcHKK401zrXw5kiX1lDFdaRJbyF9iIXkNRZSD6mQfMqF1GcqJL8z6UIppCqtkCzVwtCsUuuzeq3/Fd4BirfYqjKMET8AAAAldEVYdGRhdGU6Y3JlYXRlADIwMjAtMDQtMDVUMTg6NTU6MjQrMDA6MDB5tcB1AAAAJXRFWHRkYXRlOm1vZGlmeQAyMDIwLTA0LTA1VDE4OjU1OjI0KzAwOjAwCOh4yQAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAASUVORK5CYII='
next_ = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAQAAADZc7J/AAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAAmJLR0QAAKqNIzIAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAAHdElNRQfkBAUSNA+3aDy+AAAA2klEQVRIx+3UIU5DURCF4Q/SIBB1iBoENXgcDomrYQvdAg7NFmq6hLpKAuKlAkFYAAJTgUCQkJBAYHBNXtP7+soE12P/k5PMvTOHrbj16OQPbKEQvlzb25DVTN/CveONWM106kn4cGm3NauZ6BoJodJvyZZMcG4uvBm2YitMHJgIYaq3lq0MgAuvwovBGlYM4NCNEMaNrFsOYMfQu2hkz87KAdBXFdmRSvgxsl8OoNPIrnwKs8JytFb80wjJR0x+Y2qRkqucOqbkOacLJV1pqVK981Cs7ia21UK/obPZyXDRFNQAAAAldEVYdGRhdGU6Y3JlYXRlADIwMjAtMDQtMDVUMTg6NTI6MTUrMDA6MDCzkddbAAAAJXRFWHRkYXRlOm1vZGlmeQAyMDIwLTA0LTA1VDE4OjUyOjE1KzAwOjAwwsxv5wAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAAASUVORK5CYII='
begin_ = b'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAQAAADZc7J/AAAABGdBTUEAALGPC/xhBQAAACBjSFJNAAB6JgAAgIQAAPoAAACA6AAAdTAAAOpgAAA6mAAAF3CculE8AAAAAmJLR0QAAKqNIzIAAAAJcEhZcwAADsQAAA7EAZUrDhsAAAAHdElNRQfkBAUSNzAqI0JAAAABEklEQVRIx+3UPy9DURzG8Q+NgZBISDRhYGBhYbKyG61GC0nfgrfQt9DYjDaGRpHYRLwAi8EimohE/OnPcFOl1fb2NhbxnPE+zzf3/M45D//iXDSt05TJddfKWuIhUoTzSmqJtznQHZCzqyo8ZQOsuBDCodneAeOK3oRbWw1vesCmO+FF0ehXbzrAgmMhnFhs9nYHjNjzLNzbNtDq7QbYcCO8K5lo+a+ugBkHQri0+uNUOgKGFDwKVQW5NmPtCEiu+L689gox2OFjSv3aFmC6nyHWlRxjTclkNgDD/V2kRPOOhFCxlA1A/TG9KhrLBuj7OSda/iyUueyVtuPhe6X1XqpTjVI9a4lXUgBgzZVySu+f1gfuU+vJjN0NowAAACV0RVh0ZGF0ZTpjcmVhdGUAMjAyMC0wNC0wNVQxODo1NTo0OCswMDowMHh6o4YAAAAldEVYdGRhdGU6bW9kaWZ5ADIwMjAtMDQtMDVUMTg6NTU6NDgrMDA6MDAJJxs6AAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAABJRU5ErkJggg=='


class ControlPanelFrame(tk.Frame):
    """
    Модуль управления воспроизведением:
    === Четыре кнопки, управляются нажатием на иконку + управление с клавиатуры ===
        "в начало"           [0]
        "предыдущее слово"   [←]
        "пауза / пуск"       [space]
        "следующее слово"    [→]

    === Меню выбора wpm + управление стрелками ↑ ↓ c шагом GlobalVariables.step_wpm ===
    """

    def __init__(self, master, GV, next_frame):
        super().__init__(master, background="#ffffff")
        self.master = master
        self.GV = GV
        self.next_frame = next_frame

        self.load_icon()
        self.create_panel()

    def load_icon(self):
        self.photo_pause = tk.PhotoImage(data=pause_)
        self.photo_play = tk.PhotoImage(data=play_)
        self.photo_prev = tk.PhotoImage(data=prev_)
        self.photo_next = tk.PhotoImage(data=next_)
        self.photo_begin = tk.PhotoImage(data=begin_)

    def create_panel(self):
        b_clr = 'white'

        # Кнопки:
        self.button_begin = tk.Button(self, command=self.to_begining, image=self.photo_begin,
                                      width=32, height=32, bd=0, background=b_clr)
        self.button_begin.grid(row=0, column=0, padx=10)
        self.tool_begin = CreateToolTip(self.button_begin, 'В начало')

        self.button_prev = tk.Button(self, command=self.prev_word, image=self.photo_prev,
                                     width=32, height=32, bd=0, background=b_clr)
        self.button_prev.grid(row=0, column=1, padx=10)
        self.tool_prev = CreateToolTip(self.button_prev, 'Предыдущее слово')

        self.button_playback = tk.Button(self, command=self.playback, image=self.photo_play,
                                         width=32, height=32, bd=0, background=b_clr)
        self.button_playback.grid(row=0, column=2, padx=10)
        self.tool_playback = CreateToolTip(self.button_playback, 'Запуск')

        self.button_next = tk.Button(self, command=self.next_word, image=self.photo_next,
                                     width=32, height=32, bd=0, background=b_clr)
        self.button_next.grid(row=0, column=3, padx=10)
        self.tool_next = CreateToolTip(self.button_next, 'Следующее слово')

        # Меню wpm:
        self.values_wpm = ['100 wpm', '150 wpm', '200 wpm', '250 wpm', '300 wpm', '350 wpm',
                           '400 wpm', '500 wpm', '600 wpm', '700 wpm', '800 wpm', '900 wpm']
        self.info_wpm = tk.StringVar()
        self.info_wpm.set(f'{self.GV.wpm} wpm')

        self.menu_wpm = tk.OptionMenu(self, self.info_wpm, *self.values_wpm, command=self.update_menu_wpm)
        self.menu_wpm.config(font=('Calibri', '10'), background=b_clr, bd=0, highlightthickness=1, width=8)
        self.menu_wpm.grid(row=0, column=4, padx=10, sticky='e')

    # Функции команд для кнопок:
    def update_menu_wpm(self, event):
        self.GV.wpm = int(self.info_wpm.get()[:-3])

    def wpm_down(self):
        if self.GV.wpm - self.GV.step_wpm > 0:
            self.GV.wpm -= self.GV.step_wpm
            self.info_wpm.set(f'{self.GV.wpm} wpm')

    def wpm_up(self):
        self.GV.wpm += self.GV.step_wpm
        self.info_wpm.set(f'{self.GV.wpm} wpm')

    def playback(self):
        if self.GV.status == 'stop':
            self.GV.status = 'play'
            self.button_playback['image'] = self.photo_pause
            self.tool_playback.text = 'Пауза'

            self.next_frame()

        elif self.GV.status == 'play':
            if self.GV.status_stack != None:
                self.master.after_cancel(self.GV.status_stack)
            self.GV.status = 'stop'
            self.button_playback['image'] = self.photo_play
            self.tool_playback.text = 'Запуск'

            if self.GV.ind > 0:
                self.GV.ind -= 1

    def prev_word(self):
        if self.GV.ind > 0 and self.GV.status == 'stop':
            self.GV.ind -= 1

            self.next_frame()

    def next_word(self):
        if self.GV.ind < self.GV.size - 1 and self.GV.status == 'stop':
            self.GV.ind += 1

            self.next_frame()

    def to_begining(self):
        self.GV.status = 'play'
        self.playback()
        self.GV.ind = 0

        self.next_frame()

    def keypress(self, event):
        if event.keysym == 'Left':
            self.prev_word()
        elif event.keysym == 'Right':
            self.next_word()
        elif event.keysym == 'Down':
            self.wpm_down()
        elif event.keysym == 'Up':
            self.wpm_up()
        elif event.keysym == 'space':
            self.playback()
        elif event.keysym == '0':
            self.to_begining()
