import customtkinter as ctk
from enum import Enum
import pygame.mixer
import os

# color palette
class Color(str, Enum):
    BACKGROUND_1 = '#222831'
    BACKGROUND_2 = '#2A2F38'
    BACKGROUND_3 = '#31363F'
    TILE_1 = '#547177'
    TILE_2 = '#76ABAE'
    TILE_3 = '#B2CDCE'
    TEXT = '#EEEEEE'

# handlig files
def resource_path(file_name: str) -> str:
    dirname = os.path.dirname(__file__)
    storage = os.path.join(dirname, 'storage') # now its just for testing
    return os.path.join(storage, file_name)

# handling music
def load_music(file_name: str) -> None:
    pygame.mixer.music.load(file_name)

def play_pause_music(play_button, currently_playing):
    if play_button.cget('text') == 'PLAY' and currently_playing[0] == 0:
        file_name = resource_path('test.mp3')
        load_music(file_name)
        pygame.mixer.music.play()
        play_button.configure(text='PAUSE')
        currently_playing[0] = 1
    elif play_button.cget('text') == 'PLAY' and currently_playing[0] == 1:
        pygame.mixer.music.unpause()
        play_button.configure(text='PAUSE')
    else:
        pygame.mixer.music.pause()
        play_button.configure(text='PLAY')

def abort_music():
    ...

def set_volume():
    ...

# GUI

def player_menu(app):
    currently_playing = [0]
    play_button = ctk.CTkButton(master=app, text='PLAY', command=lambda: play_pause_music(play_button, currently_playing))
    play_button.pack(side='top', anchor='center')

def app_frame():
    width, height = 1080, 720
    app = ctk.CTk()
    app.configure(fg_color='#222831')
    app.title('Music Player')
    app.geometry(f'{width}x{height}')

    player_menu(app)

    app.mainloop()


def main() -> None:
    pygame.mixer.init()
    app_frame()

if __name__ == "__main__":
    main()
