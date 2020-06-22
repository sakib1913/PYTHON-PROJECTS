try:
    from pytube import YouTube
    from pytube import Playlist
except Exception as e:
    print("some modules are missing{}".format(e))


url="https://www.youtube.com/watch?v=668nUCeBHyY"

ytd =YouTube(url).streams.first().download()

print(ytd)
