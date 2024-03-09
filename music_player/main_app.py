import customtkinter as ctk
from PIL import Image  # noqa: F401
from enum import Enum
import pygame.mixer
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
    return os.path.join(dirname, ''.join(file_name))

def get_files_in_folder():
    files_list = []
    for root, dirs, files in os.walk(os.path.join('storage')):
        for file in files:
            files_list.append(os.path.join('storage', file))
    return files_list

# handling music
def load_music(file_name: str) -> None:
    pygame.mixer.music.load(''.join(file_name))

def play_pause_music(app, play_button, currently_playing, lenght, lenght_bar, file_name, shuffle, files_list) -> None:
    if file_name[0] != '':
        if play_button.cget('text') == ascii_symbols.PLAY and currently_playing[0] == 0:
            lenght_bar.configure(progress_color=Color.TEXT)
            get_lenght(lenght, file_name)
            load_music(resource_path(file_name))
            pygame.mixer.music.play()
            play_button.configure(text=ascii_symbols.PAUSE)
            currently_playing[0] = 1
            update_len_bar(app, lenght_bar, lenght, play_button, currently_playing, True, shuffle, files_list, file_name)
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
def update_len_bar(app, lenght_bar, lenght, play_button, currently_playing, update: bool, shuffle, files_list, file_name):
    if lenght[0] != 0:
        value = ((pygame.mixer.music.get_pos() / 360000) - lenght[0]) / (lenght[0]*1000)
        lenght_bar.set(value)
    if update and currently_playing[0] == 1:
        app.after(100, lambda e, a: update_len_bar(app, lenght_bar, lenght, play_button, currently_playing, True, shuffle, files_list, file_name), lenght_bar, shuffle)
    if currently_playing[0] == 1 and abs(value-1) < 0.03:
        play_button.configure(text=ascii_symbols.PLAY)
        currently_playing[0] = 0
        pygame.mixer.music.unload()
        app.after(100, lambda e, a: update_len_bar(app, lenght_bar, lenght, play_button, currently_playing, False, shuffle, files_list, file_name), lenght_bar, shuffle)
        app.after(100, lambda: lenght_bar.set(1))
        value = -1
        if shuffle[0] == 1:
            if files_list.index(''.join(file_name))+1 <= len(files_list):
                next_song = files_list[(files_list.index(''.join(file_name)))+1]
                app.after(140, lambda: start_new_song(app, next_song, play_button, currently_playing, lenght, lenght_bar, shuffle, files_list))

def player_menu(app, font_x21):
    menu_frame = ctk.CTkFrame(master=app, corner_radius=0, fg_color=Color.BACKGROUND_2)
    menu_frame.pack(side='bottom', fill='x')
    currently_playing = [0]
    lenght = [0]
    file_name = ['']
    shuffle = [1]

    lenght_bar = ctk.CTkProgressBar(master=app, fg_color=Color.TILE_2, progress_color=Color.TILE_2,
                                    determinate_speed=0.2, indeterminate_speed=0.2, bg_color=Color.TILE_2)
    lenght_bar.pack(side='bottom', padx=0, pady=0, fill='x')
    lenght_bar.set(0)

    play_button = ctk.CTkButton(master=menu_frame, text=ascii_symbols.PLAY, font=font_x21,
                                command=lambda: play_pause_music(app, play_button, currently_playing, lenght, lenght_bar, file_name, shuffle, []),
                                fg_color=Color.TILE_2, hover_color=Color.TILE_1, text_color=Color.TEXT, width=10)
    play_button.pack(side='left', anchor='center', padx=10, pady=10)

    volume_bar  = ctk.CTkSlider(master=menu_frame, command=set_volume, fg_color=Color.TILE_2, hover=False, progress_color=Color.TEXT,
                                button_color=Color.TEXT, )
    volume_bar.set(1)
    volume_bar.pack(side='right', padx=10, pady=10)

    songs_list(app, play_button, currently_playing, lenght, lenght_bar, file_name, shuffle)

def start_new_song(app, file_name, play_button, currently_playing, lenght, lenght_bar, shuffle, files_list):
    pygame.mixer.music.unload()
    play_button.configure(text=ascii_symbols.PLAY)
    currently_playing[0] = 0
    load_music(''.join(file_name))
    play_pause_music(app, play_button, currently_playing, lenght, lenght_bar, file_name, shuffle, files_list)

def click_button(app, play_button, currently_playing, lenght, lenght_bar, button, file_name, shuffle, files_list):
    file_name[0] = ('storage\\' + button.cget('text') + '.mp3')
    start_new_song(app, file_name, play_button, currently_playing, lenght, lenght_bar, shuffle, files_list)

def create_button(app, frame, info, play_button, currently_playing, lenght, lenght_bar, file_name, shuffle, files_list):
    button = ctk.CTkButton(master=frame, text=os.path.basename(info).strip('.mp3'),
                            command=lambda: click_button(app, play_button, currently_playing, lenght, lenght_bar, button, file_name, shuffle, files_list))
    button.pack()

def songs_list(app, play_button, currently_playing, lenght, lenght_bar, file_name, shuffle):
    scroll_frame = ctk.CTkFrame(master=app, corner_radius=0, fg_color=Color.BACKGROUND_3)
    scroll_frame.pack(side='top', fill='both', expand=True)
    files_list = get_files_in_folder()
    for item in files_list:
        create_button(app, scroll_frame, item.strip(), play_button, currently_playing, lenght, lenght_bar, file_name, shuffle, files_list)

def app_frame() -> None:
    width, height = 1080, 720
    app = ctk.CTk()
    app.configure(fg_color=Color.BACKGROUND_1)
    app.title('Music Player')
    app.geometry(f'{width}x{height}')
    font_x21 = ctk.CTkFont(family='Hack Nerd Font', size=21)

    player_menu(app, font_x21)

    app.mainloop()

def main() -> None:
    pygame.mixer.init()
    app_frame()

if __name__ == "__main__":
    main()
