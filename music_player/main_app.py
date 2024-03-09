import customtkinter as ctk
from PIL import Image  # noqa: F401
from enum import Enum
import pygame.mixer
import tkinter
import os

# color palette
class Color(str, Enum):
    BACKGROUND_1 = '#222831'
    BACKGROUND_2 = '#2A2F38'
    BACKGROUND_3 = '#31363F'
    TILE_1 =       '#547177'
    TILE_2 =       '#76ABAE'
    TILE_3 =       '#B2CDCE'
    TEXT =         '#EEEEEE'
    TRANSPARENT =  'transparent'

# characters
class ascii_symbols(str, Enum):
    PLAY =  '\u23F5'
    PAUSE = '\u23F8'
    STOP =  '\u23F9'
    PREV =  '\u23EE'
    NEXT =  '\u23ED'
    HOME =  '\u2302 '

# general use
def destroy_old_page(page):
    for child in page.winfo_children():
        child.destroy()

# handlig files
def resource_path(file_name: str) -> str:
    dirname = os.path.dirname(__file__)
    return os.path.join(dirname, file_name)

def get_files_in_folder(album_name):
    print(album_name)
    files_list = []
    for root, dirs, files in os.walk(os.path.join('storage', album_name)):
        for file in files:
            files_list.append(os.path.join('storage', album_name, file))
    return files_list

def get_folders_from_storage() -> list[str]:
    folders = []
    for item in os.listdir('storage'):
        if os.path.isdir(os.path.join('storage', item)):
            folders.append(item)
    return folders

# handling music
def load_music(file_name: str) -> None:
    pygame.mixer.music.load(file_name)

def play_pause_music(app, play_button, currently_playing, lenght, lenght_bar, file_name) -> None:
    if file_name[0] != '':
        if play_button.cget('text') == ascii_symbols.PLAY and currently_playing[0] == 0:
            lenght_bar.configure(progress_color=Color.TEXT)
            get_lenght(lenght, file_name[0])
            load_music(resource_path(file_name[0]))
            pygame.mixer.music.play()
            play_button.configure(text=ascii_symbols.PAUSE)
            currently_playing[0] = 1
            update_len_bar(app, lenght_bar, lenght, play_button, currently_playing, True)
        elif play_button.cget('text') == ascii_symbols.PLAY and currently_playing[0] == 1:
            pygame.mixer.music.unpause()
            play_button.configure(text=ascii_symbols.PAUSE)
        else:
            pygame.mixer.music.pause()
            play_button.configure(text=ascii_symbols.PLAY)

def set_volume(value) -> None:
    pygame.mixer.music.set_volume(value)

def get_lenght(lenght, file_name) -> None:
    lenght[0] = (pygame.mixer.Sound.get_length(pygame.mixer.Sound(resource_path(file_name))) / 360000)

# GUI
# player informations
def update_len_bar(app, lenght_bar, lenght, play_button, currently_playing, update: bool):
    if lenght[0] != 0:
        value = ((pygame.mixer.music.get_pos() / 360000) - lenght[0]) / (lenght[0]*1000)
        lenght_bar.set(value)
    if update and currently_playing[0] == 1:
        app.after(100, lambda e: update_len_bar(app, lenght_bar, lenght, play_button, currently_playing, True), lenght_bar)
    if currently_playing[0] == 1 and abs(value-1) < 0.03:
        play_button.configure(text=ascii_symbols.PLAY)
        currently_playing[0] = 0
        pygame.mixer.music.unload()
        app.after(100, lambda e: update_len_bar(app, lenght_bar, lenght, play_button, currently_playing, False), lenght_bar)
        app.after(100, lambda: lenght_bar.set(1))
        value = -1

def player_menu(app, font_x21, file_name, album_name):
    menu_frame = ctk.CTkFrame(master=app, corner_radius=0, fg_color=Color.BACKGROUND_2)
    menu_frame.pack(side='bottom', fill='x')
    currently_playing = [0]
    lenght = [0]

    lenght_bar = ctk.CTkProgressBar(master=app, fg_color=Color.TILE_2, progress_color=Color.TILE_2,
                                    determinate_speed=0.2, indeterminate_speed=0.2, bg_color=Color.TILE_2)
    lenght_bar.pack(side='bottom', padx=0, pady=0, fill='x')
    lenght_bar.set(0)

    play_button = ctk.CTkButton(master=menu_frame, text=ascii_symbols.PLAY, font=font_x21,
                                command=lambda: play_pause_music(app, play_button, currently_playing, lenght, lenght_bar, file_name),
                                fg_color=Color.TILE_2, hover_color=Color.TILE_1, text_color=Color.TEXT, width=10)
    play_button.pack(side='left', anchor='center', padx=10, pady=10)

    volume_bar  = ctk.CTkSlider(master=menu_frame, command=set_volume, fg_color=Color.TILE_2, hover=False, progress_color=Color.TEXT,
                                button_color=Color.TEXT, )
    volume_bar.set(1)
    volume_bar.pack(side='right', padx=10, pady=10)

    album_list(app, font_x21, file_name, album_name, play_button, currently_playing, lenght, lenght_bar)

# albums view
def show_album(app, radio_var, albums_list, font_x21, file_name, album_name, play_button, currently_playing, lenght, lenght_bar):
    album_name[0] = albums_list[radio_var.get()]
    songs_list(app, radio_var, albums_list, font_x21, file_name, album_name, currently_playing, play_button)

def album_list(app, font_x21, file_name, album_name, play_button, currently_playing, lenght, lenght_bar):
    scrollable_frame = ctk.CTkScrollableFrame(master=app, corner_radius=0, fg_color=Color.BACKGROUND_3)
    scrollable_frame.pack(side='left', fill='both')
    albums_list = get_folders_from_storage()
    radio_var = tkinter.IntVar(value=0)
    for i, item in enumerate(albums_list):
        button = ctk.CTkRadioButton(master=scrollable_frame, text=f'{item} ', font=font_x21, variable= radio_var,
                                    value=i, border_width_checked=0, border_width_unchecked=0,
                                    command=lambda: show_album(app, radio_var, albums_list, font_x21, file_name, album_name, play_button, currently_playing, lenght, lenght_bar))
        image = Image.open('storage\\test.jpg')
        image_d = ctk.CTkImage(dark_image=image, size=(40,40))
        label = ctk.CTkLabel(master=button, image=image_d, fg_color=Color.BACKGROUND_3, text='')
        label.grid(row=0, column=0, sticky='w')
        button.pack(side='top', pady=8, padx=5, fill='x')

# songs view
def choose_song(file_name, radio_var_2, files_in_album, currently_playing, play_button):
    if currently_playing[0] == 0:
        file_name[0] = files_in_album[radio_var_2.get()]
        currently_playing[0] = 1
    else:
        currently_playing[0] = 0
        pygame.mixer.music.unload()
        play_button.configure(text=ascii_symbols.PLAY)

def songs_list(app, radio_var, albums_list, font_x21, file_name, album_name, currently_playing, play_button):
    destroy_old_page(app)
    print(album_name[0])
    player_menu(app, font_x21, file_name, album_name)
    scrollable_frame = ctk.CTkScrollableFrame(master=app, corner_radius=0, fg_color=Color.BACKGROUND_1)
    scrollable_frame.pack(side='top', anchor='center', expand=True, fill='both')
    if albums_list[0] != '':
        print(albums_list[radio_var.get()])
        radio_var_2 = tkinter.IntVar(value=0)
        files_in_album = get_files_in_folder((albums_list[radio_var.get()]))
        for i, item in enumerate(files_in_album):
            button = ctk.CTkRadioButton(master=scrollable_frame, text=f'{os.path.basename(item)}'.strip('.mp3'), font=font_x21, variable=radio_var_2,
                                        value=i, border_width_checked=0, border_width_unchecked=0,
                                        command=lambda: choose_song(file_name, radio_var_2, files_in_album, currently_playing, play_button))
            button.pack(side='top', pady=8, padx=5, fill='x')

def app_frame():
    width, height = 1080, 720
    app = ctk.CTk()
    app.configure(fg_color=Color.BACKGROUND_1)
    app.title('Music Player')
    app.geometry(f'{width}x{height}')
    font_x21 = ctk.CTkFont(family='Hack Nerd Font', size=21)
    album_name = ['']
    file_name = ['']

    player_menu(app, font_x21, file_name, album_name)

    app.mainloop()


def main() -> None:
    pygame.mixer.init()
    app_frame()

if __name__ == "__main__":
    main()
