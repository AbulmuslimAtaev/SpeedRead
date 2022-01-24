import tkinter as tk


class TextFrame(tk.Frame):
    '''
    Класс отвечает только за отрисовку основного поля: рамка и слово.
    Отрисовка по глобальным параметрам: текущий размер окна, номер слова.
    Параметр 'n' -- номер буквы, относительно которой центрируется слово.

    При желании можно добавить масштабируемость при изменении размеров окна.
    '''

    def __init__(self, master, GV):
        super().__init__(master, background="#ffffff")
        self.master = master
        self.GV = GV

        self.canvas = None
        self.update(1)

    def update(self, n):
        w_ = self.GV.width
        h_ = self.GV.height

        if self.canvas is not None:
            self.canvas.delete('all')
        else:
            self.canvas = tk.Canvas(self, width=w_, height=h_ / 3,
                                    bg='white', bd=0, highlightthickness=0)

        # Рамка
        self.canvas.create_line(0, 0, w_, 0, width=5)
        self.canvas.create_line(2 * w_ / 5, 0, 2 * w_ / 5, 10, width=2.5)
        self.canvas.create_line(0, h_ / 3 - 1, w_, h_ / 3 - 1, width=5)
        self.canvas.create_line(2 * w_ / 5, h_ / 3, 2 * w_ / 5, h_ / 3 - 10, width=2.5)

        # Отображение слова. Рисуем по бувам. На каждую букву отводим 'p' пикселей.
        if self.GV.size != 0:
            if n > len(self.GV.words[self.GV.ind]):
                n = len(self.GV.words[self.GV.ind])

            p = 40
            starting_coord = 2 * w_ / 5 - p * (n - 1)
            for j, sym in enumerate(self.GV.words[self.GV.ind]):
                x = starting_coord + p * j
                if j == n - 1:
                    self.canvas.create_text(x, 50 - 4, text=sym, font=('Courier', '50'), justify='center',
                                            fill='#ce0018')
                else:
                    self.canvas.create_text(x, 50 - 4, text=sym, font=('Courier', '50'), justify='center')

        self.canvas.pack(expand=True)
