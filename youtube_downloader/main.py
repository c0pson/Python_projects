import customtkinter as ctk
from pytube import YouTube
from io import BytesIO
from PIL import Image
import requests
import re

def get_title(url):
    yt = YouTube(url)
    return yt.title

def is_valid_youtube_link(link):
    pattern = r'^https?://(?:www\.)?youtube\.com/watch\?(?=.*v=\w+)(?:\S+)?$'
    if re.match(pattern, link):
        return True
    return False

def get_thumbnail_url(url):
    yt = YouTube(url)
    thumbnail_url = yt.thumbnail_url
    return thumbnail_url

def display_thumbnail(url, frame_for_image, my_font, app):
    global counter
    global progress_bar
    progress_bar.set(0.0)
    if counter > 0:
        for widget in frame_for_image.winfo_children():
            widget.destroy()
    if url != '' and is_valid_youtube_link(url):
        desired_width = 400
        desired_height = int((16 / 9) * desired_width)
        thumbnail_url = get_thumbnail_url(url)
        response = requests.get(thumbnail_url)
        image_data = response.content
        image = Image.open(BytesIO(image_data))
        thumbnail = ctk.CTkImage(light_image=image, dark_image=image, size=(desired_height, desired_width))
        image_label = ctk.CTkLabel(master=frame_for_image, image=thumbnail, text='', anchor='center')
        image_label.pack(side ='top', anchor='center', expand=True)
        frame_for_image.update()
        app.title(f'Downloading: {get_title(url)}')
        download_video(url)
    else:
        error_label = ctk.CTkLabel(master=frame_for_image, text='Invalid URL!', font=my_font, anchor='center')
        error_label.pack(side='top', anchor='center', expand=True)
    counter += 1

def on_progress(stream, chunk, bytes_remaining):
    global progress_bar
    global frame_for_buttons
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage = (bytes_downloaded / total_size) * 100
    progress_bar.set(float(percentage / 100))
    frame_for_buttons.update()

def download_video(url):
    global progress_bar
    progress_bar.set(0.0)
    try:
        yt_object = YouTube(url, on_progress_callback=on_progress)
        video = yt_object.streams.get_highest_resolution()
        if video:
            video.download()
    except NotImplementedError:
        pass

def application_window():
    global url
    global counter
    global progress_bar
    global frame_for_buttons # im sorry for this but this library is pain to use without it not making it whole globals
    WINDOW_X , WINDOW_Y = 1080, 720 # idk why
    app = ctk.CTk() # root
    app.geometry(f'{WINDOW_X}x{WINDOW_Y}') # size of window
    app.title('YouTube Downloader') # title
    app.resizable(False, False) # set static size
    my_font = ctk.CTkFont(family='Hack Nerd Font Regular', size=24) # set font
    counter = 0 # to handle unknown urls

    main_frame = ctk.CTkFrame(master=app, corner_radius=0)
    main_frame.pack(side='top', fill='both', expand=True, padx=0, pady=0)

    frame_for_image = ctk.CTkFrame(master=main_frame)
    frame_for_image.pack(side='top', fill='both', expand=True, padx=10, pady=5)

    frame_for_buttons = ctk.CTkFrame(master=main_frame, width=100)
    frame_for_buttons.pack(side='top', fill='both', expand=False, padx=10, pady=5)

    progress_bar = ctk.CTkProgressBar(master=frame_for_buttons, width=500, height=15)
    progress_bar.set(0.0)
    progress_bar.pack(side='top', fill='both', expand=False, padx=40, pady=10)

    url_input = ctk.CTkEntry(master=frame_for_buttons, corner_radius=10, width=700, height=80, font=my_font)
    url_input.pack(side='left', padx=40, pady=10, fill='x')

    download_button = ctk.CTkButton(master=frame_for_buttons, text='Download',
                                    font=my_font, command=lambda: display_thumbnail(url_input.get(), frame_for_image, my_font, app),
                                    width=200, height=80)
    download_button.pack(side='right', padx=40, pady=15)

    app.mainloop()

if __name__ == "__main__":
    application_window()
