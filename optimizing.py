import tkinter
import customtkinter
import os
from pytube import YouTube
from pytube import Playlist

            
def directory(path):
            
    if os.path.exists(r'C:\Users\manue\Downloads\pytube'):
        os.chdir(r'C:\Users\manue\Downloads\pytube')
    else:
        os.chdir(r'C:\Users\manue\Downloads')
        os.mkdir("pytube")
        os.chdir(r'C:\Users\manue\Downloads\pytube')
        
    if path == "video":
        if os.path.exists(r'C:\Users\manue\Downloads\pytube\video'):
            os.chdir(r'C:\Users\manue\Downloads\pytube\video')
        else:
            os.chdir(r'C:\Users\manue\Downloads\pytube')
            os.mkdir("video")
            os.chdir(r'C:\Users\manue\Downloads\pytube\video')
            
    elif path == "audio":
        if os.path.exists(r'C:\Users\manue\Downloads\pytube\audio'):
            os.chdir(r'C:\Users\manue\Downloads\pytube\audio')
        else:
            os.chdir(r'C:\Users\manue\Downloads\pytube')
            os.mkdir("audio")
            os.chdir(r'C:\Users\manue\Downloads\pytube\audio')
            
    elif path == "playlist":
        if os.path.exists(r'C:\Users\manue\Downloads\pytube\playlist'):
            os.chdir(r'C:\Users\manue\Downloads\pytube\playlist')
        else:
            os.chdir(r'C:\Users\manue\Downloads\pytube')
            os.mkdir("playlist")
            os.chdir(r'C:\Users\manue\Downloads\pytube\playlist')
            
    return os.getcwd()
                        
def videoDownloader():
    try:
        youtubeLink = link.get()
        ytObject = YouTube(youtubeLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")
        
        download_path = directory("video")
        video.download(output_path=download_path)
        
        finishLabel.configure(text="Video Downloaded!", text_color="green")
        # print ("Download complete")
    except Exception as e:
        if youtubeLink == "":
            finishLabel.configure(text=f"Please Enter a Link {e}",text_color="red")
        else:
            finishLabel.configure(text=f"Video Download Error! {e}",text_color="red")
            # print("YouTube link is invalid")


def audioDownloader():
    try:
        youtubeLink = link.get()
        ytObject = YouTube(youtubeLink, on_progress_callback=on_progress)
        audio = ytObject.streams.get_audio_only()

        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")

        download_path = directory("audio")
        audio.download(output_path=download_path)

        finishLabel.configure(text="Audio Downloaded!", text_color="green")
        # print ("Download complete")
    except Exception as e:
        if youtubeLink == "":
            finishLabel.configure(text=f"Please Enter a Link {e}",text_color="red")
        else:
            finishLabel.configure(text=f"Audio Download Error! {e}",text_color="red")
            # print("YouTube link is invalid")


def playlistDownloader():
    try:
        playlistLink = link.get()
        p = Playlist(playlistLink)
        
        for video in p.video_urls:
            try:
                ytObject = YouTube(video, on_progress_callback=on_progress)
                playlist = ytObject.streams.get_highest_resolution()

                title.configure(text=ytObject.title, text_color="white")
                ply_finishLabel.configure(text="")
                
                download_path = directory("playlist")
                playlist.download(output_path=download_path)
                            
                ply_finishLabel.configure(text="Playlist Downloaded!", text_color="green")
            except Exception as e:
                print(f"Error downloading video {video}: {e}")
                ply_finishLabel.configure(text=f"Error downloading video: {e}", text_color="red")
                continue
    except Exception as e:
        if playlistLink == "":
            ply_finishLabel.configure(text=f"Please Enter a Link {e}",text_color="red")
        else:
            ply_finishLabel.configure(text=f"Playlist Download Error: {e}",text_color="red")
        
    
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