from ctypes import windll, byref, sizeof, c_int
import customtkinter as ctk
from enum import Enum

class Colors(str, Enum):
    BACK = '#F5F7F8'
    INCO = '#F4CE14'
    BUT1 = '#495E57'
    TEXT = '#45474B'

class Board(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master=master, fg_color=Colors.BUT1)
        master.bind('<Key>', self.cell_keyboard_input_handle)
        self.selected_cell = None
        self.all_cells = []

        self.create_board()

        self.check_button = ctk.CTkButton(master=master, text='CHECK', command=self.check_board)
        self.check_button.pack(side='bottom', padx=10, pady=10)

        self.pack(side='top', padx=10, pady=10, anchor='center', expand=True)

    def cell_keyboard_input_handle(self, event):
        accepted_input = '1234567890'
        if not self.selected_cell:
            pass
        elif event.keysym in accepted_input:
            self.selected_cell.configure(text=f'{event.keysym}')
        self.move_on_board(event)

    def cell_clicked(self, cell):
        if not self.selected_cell:
            cell.configure(fg_color=Colors.BUT1)
            self.selected_cell = cell
        else:
            self.selected_cell.configure(fg_color=Colors.TEXT)
            cell.configure(fg_color=Colors.BUT1)
            self.selected_cell = cell

    def create_cell(self, row, column, box):
        cell = ctk.CTkLabel(box, text='   ', fg_color=Colors.TEXT, corner_radius=10, width=50, height=50)
        cell.grid(row=row, column=column, padx=3, pady=3)
        self.all_cells.append(cell)
        cell.bind('<Button-1>', lambda event: self.cell_clicked(cell))

    def create_cells_box(self, row, column):
        box = ctk.CTkFrame(self, fg_color=Colors.INCO)
        box.grid(row=row, column=column, padx=10, pady=10)
        for i in range(3):
            for j in range(3):
                self.create_cell(i, j%3, box)

    def create_board(self):
        for i in range(3):
            for j in range(3):
                self.create_cells_box(i, j%3)

    def find_index(self, list, value):
        for i in range(len(list)):
            for j in range(len(list[0])):
                if list[i][j] == value:
                    return(i, j)
        return (0, 0)

    def move_on_board(self, event):
        board_ids = [
            [0,  1,  2,  9,  10, 11, 18, 19, 20],
            [3,  4,  5,  12, 13, 14, 21, 22, 23],
            [6,  7,  8,  15, 16, 17, 24, 25, 26],
            [27, 28, 29, 36, 37, 38, 45, 46, 47],
            [30, 31, 32, 39, 40, 41, 48, 49, 50],
            [33, 34, 35, 42, 43, 44, 51, 52, 53],
            [54, 55, 56, 63, 64, 65, 72, 73, 74],
            [57, 58, 59, 66, 67, 68, 75, 76, 77],
            [60, 61, 62, 69, 70, 71, 78, 79, 80]
        ]
        if self.selected_cell is None:
            return
        if event.keysym == 'Up' or event.keysym == 'w':
            current_index = self.all_cells.index(self.selected_cell)
            x, y = self.find_index(board_ids, current_index)
            if not x:
                return
            if self.selected_cell:
                self.selected_cell.configure(fg_color=Colors.TEXT)
                self.all_cells[board_ids[x-1][y]].configure(fg_color=Colors.BUT1)
                self.selected_cell = self.all_cells[board_ids[x-1][y]]
        if event.keysym == 'Down' or event.keysym == 's':
            current_index = self.all_cells.index(self.selected_cell)
            x, y = self.find_index(board_ids, current_index)
            if x > 7:
                return
            if self.selected_cell:
                self.selected_cell.configure(fg_color=Colors.TEXT)
                self.all_cells[board_ids[x+1][y]].configure(fg_color=Colors.BUT1)
                self.selected_cell = self.all_cells[board_ids[x+1][y]]
        if event.keysym == 'Left' or event.keysym == 'a':
            current_index = self.all_cells.index(self.selected_cell)
            x, y = self.find_index(board_ids, current_index)
            if not y:
                return
            if self.selected_cell:
                self.selected_cell.configure(fg_color=Colors.TEXT)
                self.all_cells[board_ids[x][y-1]].configure(fg_color=Colors.BUT1)
                self.selected_cell = self.all_cells[board_ids[x][y-1]]
        if event.keysym == 'Right' or event.keysym == 'd':
            current_index = self.all_cells.index(self.selected_cell)
            x, y = self.find_index(board_ids, current_index)
            if y > 7:
                return
            if self.selected_cell:
                self.selected_cell.configure(fg_color=Colors.TEXT)
                self.all_cells[board_ids[x][y+1]].configure(fg_color=Colors.BUT1)
                self.selected_cell = self.all_cells[board_ids[x][y+1]]

    # TODO: detect which is incorrect | in next version - now just basics
    # alghoritm was made for fun | kinda unpractical but was fun to make
    def check_board(self):
        # check in box
        cells = []
        rows = []
        columns = []
        is_good = []
        for i in range(len(self.all_cells)):
            if self.all_cells[i].cget('text') != '   ':
                cells.append(self.all_cells[i].cget('text'))
            if i%9 == 8:
                if len(cells) != len(set(cells)):
                    is_good.append(0)
                else:
                    is_good.append(1)
                cells = []
        # check in row
        multi = 0
        for i in range(9):
            if i%3 == 0 and i != 0:
                multi += 2
            for j in range(9):
                index = j + (6*(j//3)) + (i*3) + (9*multi)
                if self.all_cells[index].cget('text') != '   ':
                    rows.append(self.all_cells[index].cget('text'))
            if len(rows) != len(set(rows)):
                is_good.append(0)
            else:
                is_good.append(1)
            rows = []
        # check in column
        multi = 0
        for i in range(9):
            if i%3 == 0 and i != 0:
                multi += 2
            for j in range(9):
                index = 3*j + 16*(j//3) + (j//3)*2 + i + (3*multi)
                if self.all_cells[index].cget('text') != '   ':
                    columns.append(self.all_cells[index].cget('text'))
            if len(columns) != len(set(columns)):
                is_good.append(0)
            else:
                is_good.append(1)
            columns = []
        if 0 in is_good:
            print('u good bro?')

class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color=Colors.BACK)
        self.title('Sudoku')
        self.geometry('1080x720+40+40')
        self.change_title_bar_color()
        Board(self)

    def change_title_bar_color(self) -> None:
        HWND = windll.user32.GetParent(self.winfo_id())
        DWMWA_CAPTION_COLOR = 35
        COLOR_1 = 0x00F8F7F5 # 0x00bbggrr
        windll.dwmapi.DwmSetWindowAttribute(HWND, DWMWA_CAPTION_COLOR,
                                    byref(c_int(COLOR_1)), sizeof(c_int))

if __name__ == "__main__":
    app = App()
    app.mainloop()
