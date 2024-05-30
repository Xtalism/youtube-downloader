import tkinter
import customtkinter
import os
from pytube import YouTube
from pytube import Playlist

os.chdir(r'C:\Users\manue\Downloads')
os.mkdir("PyTube")
os.chdir(r'C:\Users\manue\Downloads\PyTube')

cur_directory = os.getcwd()

def videoDownloader():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")

        dl_video = video.download()
        os.path.join(cur_directory, dl_video)

        finishLabel.configure(text="Video Downloaded!", text_color="green")
        # print ("Download complete")
    except:
        if ytLink == "":
            finishLabel.configure(text="Please Enter a Link",text_color="red")
        else:
            finishLabel.configure(text="Video Download Error!",text_color="red")
            # print("YouTube link is invalid")

def audioDownloader():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        audio = ytObject.streams.get_audio_only()

        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")

        dl_audio = audio.download()
        os.path.join(cur_directory, dl_audio)

        finishLabel.configure(text="Audio Downloaded!", text_color="green") 
        # print ("Download complete")
    except:
        if ytLink == "":
            finishLabel.configure(text="Please Enter a Link",text_color="red")
        else:
            finishLabel.configure(text="Audio Download Error!",text_color="red")
            # print("YouTube link is invalid")

# The following code needs to be fixed
def playlistDownloader():
    try:
        plyLink = link.get()
        plyObject = YouTube(plyLink, on_progress_callback=on_progress)
        p = Playlist(plyLink)
        for plyObject in p.videos:
            playlist = plyObject.streams.get_highest_resolution()
            title.configure(text=plyObject.title, text_color="white")
            ply_finishLabel.configure(text="")
            playlist.download()
            ply_finishLabel.configure(text="Playlist Downloaded!", text_color="green")
    except:
        if plyLink == "":
            ply_finishLabel.configure("Please Enter a Link",text_color="red")
        else:
            ply_finishLabel.configure(text="Playlist Download Error!",text_color="red")
        
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=per + '%')
    pPercentage.update()
    print(str(int(percentage_of_completion)))

    # Update progess bar
    progressBar.set(float(percentage_of_completion / 100))

# System settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Downloader")

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="YouTube Link")
title.pack(padx=10, pady=10)

# Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finished downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

# Temporary, only for testing
ply_finishLabel = customtkinter.CTkLabel(app, text="")
ply_finishLabel.pack()

# Progress percentage
pPercentage = customtkinter.CTkLabel(app, text="0%")
pPercentage.pack()

# Directory os.path.join
directoryLabel = customtkinter.CTkLabel(app, text="")
directoryLabel.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

# Download button
download = customtkinter.CTkButton(app, text="Video Downloader", command=videoDownloader) # command is used to start a function
download.pack(padx=10, pady=10)

download = customtkinter.CTkButton(app, text="Playlist Downloader", command=playlistDownloader) # command is used to start a function
download.pack(padx=10, pady=10)

download = customtkinter.CTkButton(app, text="Audio Downloader", command=audioDownloader) # command is used to start a function
download.pack(padx=10, pady=10)

# Run app
app.mainloop()