# Importing Module
from pygame import mixer
import customtkinter, tkinter
from PIL import Image
import eyed3
import os

mixer.init()

# Variables
sList = []
musicFolder = "/home/bir/Music/"
current = ''
start = False
fname = "assets/notfound.jpg"

# Functions
def changeThumb():
    global fname, playImg, mImg
    audio_file = eyed3.load(musicFolder+current)

    image = audio_file.tag.images[0]
    fname = f"assets/song.png"
    image_file = open(fname, "wb")
    image_file.write(image.image_data)
    image_file.close()

    playImg.configure(light_image=Image.open(fname))

    os.remove(fname)

def play():
    global start, current
    if current == '':
        current = sList[0]

    i = sList.index(current)
    changeThumb()

    if start:
        mixer.music.unpause()
    else:
        mixer.music.load(musicFolder+current)
        mixer.music.play()
        mixer.music.queue(musicFolder+current)
        start = True

def pause():
    mixer.music.pause()    

def resume():
    mixer.music.unpause()

def next():
    global current, start
    length = len(sList)-1
    i = sList.index(current)

    if i < length:
        current = sList[i+1]
    else:
        current = sList[0]
    
    changeThumb()
    start = False
    play()

def prev():
    global current, start
    length = len(sList)-1
    i = sList.index(current)

    if i != length:
        current = sList[i-1]
    else:
        current = sList[0]
    
    changeThumb()
    start = False
    play()

def lsSongs():
    for f in os.listdir(musicFolder):
        if '.mp3' in f or '.wav' in f:
            sList.append(f)

def addsongs():
    global current, musicFolder,sList
    songs = list(tkinter.filedialog.askopenfilenames(initialdir=musicFolder,title="Choose a song", filetypes=(("mp3 Files","*.mp3"),)))
    if len(songs) != 0:
        sList = songs
        current = sList[0]
        print(current)
        musicFolder = ''
        next()

# Main GUI Code   
root = customtkinter.CTk()
root.geometry("840x545")
root.minsize(840, 545)
root.maxsize(840, 545)
root.title("Music Player")

# Fonts
bg = customtkinter.CTkFont(family="Helevetica", size=35, weight = 'bold')
md = customtkinter.CTkFont(family="Helevetica", size=18, weight='bold')
sm = customtkinter.CTkFont(family="Helevetica", size=15)

lsSongs()

# Menu Bar
mainmenu = customtkinter.CTkFrame(root, height=30, width=830)
mainmenu.grid(row=0, column=0,padx=5, pady=5, sticky="nw")

addSongs = customtkinter.CTkButton(mainmenu, text="Add Songs", width=50, height=20, font=md, corner_radius=0, command=addsongs, fg_color="transparent")
addSongs.grid(padx=5,ipadx=5,ipady=5,sticky="w")

# Music Thumbnail
mThumb = customtkinter.CTkFrame(master=root, width=835, height=370, fg_color="transparent")
mThumb.grid(row=1, column=0, padx=5, pady=5)
playImg = customtkinter.CTkImage(light_image=Image.open(fname), size=(835,370))
mImg = customtkinter.CTkLabel(mThumb, image=playImg, text="")
mImg.grid(padx=0)

# Music Player Options
mPlay = customtkinter.CTkFrame(master=root, width=835, height=110, fg_color='transparent')
mPlay.grid(row=2, columnspan=2, column=0, padx=5, pady=15)

nextBtn = customtkinter.CTkButton(mPlay, text="Prev", width=75, height=75, corner_radius=75, font=md, border_spacing=0, command=prev)
nextBtn.pack(side='left', padx=7)

playBtn = customtkinter.CTkButton(mPlay, text="Play", width=75, height=75, corner_radius=75, font=md, border_spacing=0, command=play)
playBtn.pack(side='left', padx=7)  

pauseBtn = customtkinter.CTkButton(mPlay, text="Pause", width=75, height=75, corner_radius=75, font=md, border_spacing=0, command=pause)
pauseBtn.pack(side='left', padx=7)

nextBtn = customtkinter.CTkButton(mPlay, text="Next", width=75, height=75, corner_radius=75, font=md, border_spacing=0, command=next)
nextBtn.pack(side='left', padx=7)

root.mainloop()