import tkinter
import customtkinter
import directoryOs
from pytube import YouTube
from pytube import Playlist
    
def videoDownloader():
    try:
        youtubeLink = link.get() 
        if not youtubeLink:
            raise ValueError("Please enter a link")
        
        ytObject = YouTube(youtubeLink, on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")
        
        download_path = directoryOs.directory("video")
        video.download(output_path=download_path)
        
        finishLabel.configure(text="Video Downloaded!", text_color="green")
        # print ("Download complete")
    except Exception as e:
            finishLabel.configure(text=f"Video Download Error! {e}",text_color="red")
            # print("YouTube link is invalid")


def audioDownloader():
    try:
        youtubeLink = link.get()
        if not youtubeLink:
            raise ValueError("Please enter a link")
        
        ytObject = YouTube(youtubeLink, on_progress_callback=on_progress)
        audio = ytObject.streams.get_audio_only()

        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")

        download_path = directoryOs.directory("audio")
        audio.download(output_path=download_path)

        finishLabel.configure(text="Audio Downloaded!", text_color="green")
        # print ("Download complete")
    except Exception as e:
            finishLabel.configure(text=f"Audio Download Error! {e}",text_color="red")
            # print("YouTube link is invalid")


def playlistDownloader():
    try:
        playlistLink = link.get()
        if not playlistLink:
            raise ValueError("Please enter a link")
        p = Playlist(playlistLink)
        
        for video in p.video_urls:
            try:
                ytObject = YouTube(video, on_progress_callback=on_progress)
                playlist = ytObject.streams.get_highest_resolution()

                title.configure(text=ytObject.title, text_color="white")
                ply_finishLabel.configure(text="")
                
                download_path = directoryOs.directory("playlist")
                playlist.download(output_path=download_path)
                            
                ply_finishLabel.configure(text="Playlist Downloaded!", text_color="green")
            except Exception as e:
                print(f"Error downloading video {video}: {e}")
                ply_finishLabel.configure(text=f"Error downloading video: {e}", text_color="red")
                continue
    except Exception as e:
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