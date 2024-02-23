from pytube import YouTube

url = 'https://youtu.be/zFD20EQHpUM'

yt = YouTube(url)
streams = yt.streams.all()

all_res = []

for s in streams:
    all_res.append(s.resolution)
    print(s.resolution)

print(all_res)
