import directoryOs
from pytube import YouTube

def videoDownloader(link, on_progress, title, finishLabel):
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
