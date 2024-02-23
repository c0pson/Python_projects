from pytube import YouTube

url: str = 'https://youtu.be/zFD20EQHpUM'

yt = YouTube(url)
streams = yt.streams.all()

all_res: list = []

for s in streams:
    all_res.append(s.resolution)
    print(s.resolution)

print(all_res)

resolutions: list = list(set(all_res))
resolutions: list = [x for x in resolutions if x is not None]
resolutions: list = [res.replace('p', '') for res in resolutions]
resolutions: list = [int(res) for  res in resolutions]
resolutions.sort()

print(resolutions)
