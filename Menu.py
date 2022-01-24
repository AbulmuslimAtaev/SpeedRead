import tkinter as tk
from tkinter import filedialog as fd


class Menu:
    """
    Модуль меню. Поддерживает загрузку новых файлов и создание текста в редакторе.
    """

    def __init__(self, master, GV):
        self.master = master
        self.GV = GV
        self.create_menu()

    def create_menu(self):
        self.main_menu = tk.Menu()
        self.master.config(menu=self.main_menu)

        self.open_menu = tk.Menu(tearoff=0)
        self.open_menu.add_command(label="File", command=self.load_file)
        self.open_menu.add_command(label="Editor", command=self.create_editor)

        self.main_menu.add_cascade(label="Open", menu=self.open_menu)
        self.main_menu.add_cascade(label="Lib")

    def load_file(self):
        file_name = fd.askopenfilename()
        if file_name != '':
            with open(file_name, encoding="utf-8") as f:
                s = f.read()
                self.GV.file_name = file_name
                self.GV.history[self.GV.file_name] = self.GV.history.get(self.GV.file_name, 0)
                self.GV.new_data(s)

    def create_editor(self):
        self.window = tk.Toplevel(self.master)
        self.window.title("Editor")
        self.window.geometry(f'{self.GV.width}x{self.GV.height}')
        self.window.configure(background='white')

        self.b1 = tk.Button(self.window, text="Читать!", command=self.load_editor)
        self.b1.pack(expand=True, fill='x')
        self.text = tk.Text(self.window)
        self.text.pack(expand=True, fill='both')

    def load_editor(self):
        self.GV.file_name = 'editor'
        self.GV.history[self.GV.file_name] = 0
        self.GV.new_data(self.text.get(1.0, 'end'))
        self.window.destroy()
