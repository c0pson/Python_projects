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

def play_pause_music(play_button, currently_playing, lenght) -> None:
    if play_button.cget('text') == ascii_symbols.PLAY and currently_playing[0] == 0:
        get_lenght(lenght)
        file_name = resource_path('test.mp3')
        load_music(file_name)
        pygame.mixer.music.play()
        play_button.configure(text=ascii_symbols.PAUSE)
        currently_playing[0] = 1
    elif play_button.cget('text') == ascii_symbols.PLAY and currently_playing[0] == 1:
        pygame.mixer.music.unpause()
        play_button.configure(text=ascii_symbols.PAUSE)
    else:
        pygame.mixer.music.pause()
        play_button.configure(text=ascii_symbols.PLAY)

def abort_music(currently_playing, play_button):
    pygame.mixer.music.stop()
    currently_playing[0] = 0
    play_button.configure(text=ascii_symbols.PLAY)

def set_volume(value):
    pygame.mixer.music.set_volume(value)

def get_lenght(lenght):
    lenght[0] = (pygame.mixer.Sound.get_length(pygame.mixer.Sound(resource_path('test.mp3'))) / 360000)

# GUI
def update_len_bar(app, lenght_bar, lenght):
    if lenght[0] != 0:
        value = ((pygame.mixer.music.get_pos() / 360000) - lenght[0]) / (lenght[0]*1000)
        lenght_bar.set(value)
    app.after(100, lambda e: update_len_bar(app, lenght_bar, lenght), lenght_bar)
    # update buttons to respond correctly and unload music

def player_menu(app, font_x21):
    menu_frame = ctk.CTkFrame(master=app, corner_radius=0, fg_color=Color.BACKGROUND_2)
    menu_frame.pack(side='bottom', fill='x')
    currently_playing = [0]
    lenght = [0]
    play_button = ctk.CTkButton(master=menu_frame, text=ascii_symbols.PLAY, command=lambda: play_pause_music(play_button, currently_playing, lenght),
                                font=font_x21, fg_color=Color.TILE_2, hover_color=Color.TILE_1, text_color=Color.TEXT, width=10)
    play_button.pack(side='left', anchor='center', padx=10, pady=10)

    lenght_bar = ctk.CTkProgressBar(master=menu_frame, fg_color=Color.TILE_2, progress_color=Color.TEXT)
    lenght_bar.pack(side='left', padx=10, pady=10, fill='x', expand=True)
    lenght_bar.set(0)

    volume_bar  = ctk.CTkSlider(master=menu_frame, command=set_volume, fg_color=Color.TILE_2, hover=False, progress_color=Color.TEXT,
                                button_color=Color.TEXT)
    volume_bar.set(1)
    volume_bar.pack(side='right', anchor='center', padx=10, pady=10)

    stop_button = ctk.CTkButton(master=menu_frame, text=ascii_symbols.STOP, command=lambda: abort_music(currently_playing, play_button),
                                font=font_x21, fg_color=Color.TILE_2, hover_color=Color.TILE_1, text_color=Color.TEXT, width=10)
    stop_button.pack(side='right', anchor='center', padx=10, pady=10)

    update_len_bar(app, lenght_bar, lenght)

def app_frame():
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
