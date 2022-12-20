# Importing Module
from pygame import mixer
import customtkinter
from PIL import Image
import eyed3

mixer.init()

# Variables
sList = ["Bambiha Bole - Sidhu Moose Wala.mp3", "Old Skool Ft. Sidhu Moose Wala - Prem Dhillon.mp3"]
current = sList[0]
start = False

# Functions
def changeThumb():
    audio_file = eyed3.load("home/bir/Music/"+current)
    album_name = audio_file.tag.album
    artist_name = audio_file.tag.artist
    for image in audio_file.tag.images:
        image_file = open("{0} - {1}({2}).jpg".format(artist_name, album_name, image.picture_type), "wb")
        image_file.write(image.image_data)
        image_file.close()

def play():
    global start
    i = sList.index(current)

    changeThumb()

    if start:
        mixer.music.unpause()
    else:
        mixer.music.load('/home/bir/Music/'+current)
        mixer.music.play()
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
    
# Main GUI Code   
root = customtkinter.CTk()
root.geometry("840x505")
root.minsize(840, 505)
root.maxsize(840, 505)
root.title("Music Player")

# Variables

# Fonts
bg = customtkinter.CTkFont(family="Helevetica", size=35, weight = 'bold')
md = customtkinter.CTkFont(family="Helevetica", size=18, weight='bold')
sm = customtkinter.CTkFont(family="Helevetica", size=15)

# Music List
mList = customtkinter.CTkFrame(master=root, width=300, height=370)
mList.grid(row=0, column=0, padx=5, pady=5)

# Music Thumbnail
mThumb = customtkinter.CTkFrame(master=root, width=500, height=370)
mThumb.grid(row=0, column=1, padx=5, pady=5)

# Music Player Options
mPlay = customtkinter.CTkFrame(master=root, width=820, height=110, fg_color='transparent')
mPlay.grid(row=1, columnspan=2, column=0, padx=5, pady=15)

# playImg = customtkinter.CTkImage(light_image=Image.open("play.png"), dark_image=Image.open("play.png"), size=(95,73))

playBtn = customtkinter.CTkButton(mPlay, text="Play", width=75, height=75, corner_radius=75, font=md, border_spacing=0, command=play)
playBtn.pack(side='left', padx=7)  

pauseBtn = customtkinter.CTkButton(mPlay, text="Pause", width=75, height=75, corner_radius=75, font=md, border_spacing=0, command=pause)
pauseBtn.pack(side='left', padx=7)

nextBtn = customtkinter.CTkButton(mPlay, text="Next", width=75, height=75, corner_radius=75, font=md, border_spacing=0, command=next)
nextBtn.pack(side='left', padx=7)

root.mainloop()