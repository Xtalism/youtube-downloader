import customtkinter
import tkinter

def app():
    # Our app frame
    app = customtkinter.CTk()
    app.geometry("720x480")
    app.title("Youtube Downloader")

def link():
    # Link input
    url_var = tkinter.StringVar()
    link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
    link.pack()
    
def pPercentage():
    # Progress percentage
    pPercentage = customtkinter.CTkLabel(app, text="0%")
    pPercentage.pack()

def title():
    # Adding UI Elements
    title = customtkinter.CTkLabel(app, text="YouTube Link")
    title.pack(padx=10, pady=10)

def finishLabel():
    # Finished downloading
    finishLabel = customtkinter.CTkLabel(app, text="")
    finishLabel.pack()
    
def ply_finishLabel():
    # Temporary, only for testing
    ply_finishLabel = customtkinter.CTkLabel(app, text="")
    ply_finishLabel.pack()

def progressBar():
    # Progress percentage
    progressBar = customtkinter.CTkProgressBar(app, width=400)
    progressBar.set(0)
    progressBar.pack(padx=10, pady=10)

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

app.mainloop()