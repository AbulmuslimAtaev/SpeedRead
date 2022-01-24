import tkinter as tk


class StatFrame(tk.Frame):
    '''
    Модуль отображения справочной информации:
    - Текущий источник
    - Количество прочитанных слов
    '''

    def __init__(self, master, GV):
        super().__init__(master)
        self.master = master
        self.GV = GV

        self.info_file = tk.StringVar()
        self.info_file.set(f'input: {self.GV.file_name.split("/")[-1]}')

        self.info_count = tk.StringVar()
        self.info_count.set(f'{self.GV.ind + 1} words out of {self.GV.size}')

        self.create_bar()

    def create_bar(self):
        self.label_file = tk.Label(self, textvariable=self.info_file, font=('Arial', '10'),
                                   bd=0, anchor='sw')
        self.label_file.pack(side='left', padx=5)

        self.label_count = tk.Label(self, textvariable=self.info_count, font=('Arial', '10'),
                                    bd=0, anchor='se')
        self.label_count.pack(side='right', padx=5)

    def update_bar(self):
        self.info_file.set(f'input: {self.GV.file_name.split("/")[-1]}')
        self.info_count.set(f'{self.GV.ind + 1} words out of {self.GV.size}')
