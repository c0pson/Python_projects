import customtkinter as ctk
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

class ascii_symbols(str, Enum):
    PLAY =  '\u23F5'
    PAUSE = '\u23F8'
    STOP =  '\u23F9'
    PREV =  '\u23EE'
    NEXT =  '\u23ED'

# handlig files
def resource_path(file_name: str) -> str:
    dirname = os.path.dirname(__file__)
    storage = os.path.join(dirname, 'storage') # now its just for testing
    return os.path.join(storage, file_name)

# handling music
def load_music(file_name: str) -> None:
    pygame.mixer.music.load(file_name)

def play_pause_music(app, play_button, currently_playing, lenght, lenght_bar) -> None:
    if play_button.cget('text') == ascii_symbols.PLAY and currently_playing[0] == 0:
        lenght_bar.configure(progress_color=Color.TEXT)
        get_lenght(lenght)
        file_name = resource_path('test2.mp3')
        load_music(file_name)
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

def set_volume(value):
    pygame.mixer.music.set_volume(value)

def get_lenght(lenght):
    lenght[0] = (pygame.mixer.Sound.get_length(pygame.mixer.Sound(resource_path('test2.mp3'))) / 360000)

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

def player_menu(app, font_x21, font_x16):
    menu_frame = ctk.CTkFrame(master=app, corner_radius=0, fg_color=Color.BACKGROUND_2)
    menu_frame.pack(side='bottom', fill='x')
    currently_playing = [0]
    lenght = [0]

    lenght_bar = ctk.CTkProgressBar(master=app, fg_color=Color.TILE_2, progress_color=Color.TILE_2,
                                    determinate_speed=0.2, indeterminate_speed=0.2, bg_color=Color.TILE_2)
    lenght_bar.pack(side='bottom', padx=0, pady=0, fill='x')
    lenght_bar.set(0)

    play_button = ctk.CTkButton(master=menu_frame, text=ascii_symbols.PLAY, font=font_x21,
                                command=lambda: play_pause_music(app, play_button, currently_playing, lenght, lenght_bar),
                                fg_color=Color.TILE_2, hover_color=Color.TILE_1, text_color=Color.TEXT, width=10)
    play_button.pack(side='left', anchor='center', padx=10, pady=10)

    volume_bar  = ctk.CTkSlider(master=menu_frame, command=set_volume, fg_color=Color.TILE_2, hover=False, progress_color=Color.TEXT,
                                button_color=Color.TEXT, )
    volume_bar.set(1)
    volume_bar.pack(side='right', padx=10, pady=10)

def playlists_list(app):
    scrollable_frame = ctk.CTkScrollableFrame(master=app, corner_radius=0)
    scrollable_frame.pack(side='left', fill='y')

def album_list(app):
    scrollable_frame = ctk.CTkScrollableFrame(master=app, corner_radius=0)
    scrollable_frame.pack(side='top', anchor='center', expand=True, fill='x')

def app_frame():
    width, height = 1080, 720
    app = ctk.CTk()
    app.configure(fg_color=Color.BACKGROUND_1)
    app.title('Music Player')
    app.geometry(f'{width}x{height}')
    font_x21 = ctk.CTkFont(family='Hack Nerd Font', size=21)
    font_x16 = ctk.CTkFont(family='Arial', size=16, weight='bold')

    player_menu(app, font_x21, font_x16)
    playlists_list(app)
    album_list(app)

    app.mainloop()


def main() -> None:
    pygame.mixer.init()
    app_frame()

if __name__ == "__main__":
    main()
