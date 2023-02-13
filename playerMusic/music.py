import tkinter
from tkinter import *
import pygame
from tkinter import filedialog
import shutil
import os

gui = Tk()
gui.geometry("400x500")

def loop():
    global song
    if song == False:
        pygame.mixer.music.play(loops=-1)
        song = True
    else:
        pygame.mixer.music.play()
        song = False

def play():
    pygame.mixer.music.load("Music/" + music_list.get(music_list.curselection()))
    pygame.mixer.music.play()


def pause():
    global song
    if song == False:
        pygame.mixer.music.pause()
        song = True
        buttonpause["image"] = play_image_button
    else:
        pygame.mixer.music.unpause()
        song = False
        buttonpause["image"] = pause_image_button

def stop():
    pygame.mixer.music.stop()


def add():
    open_file = filedialog.askopenfilename(title="Choose a song",defaultextension=".wav",filetypes=[("WAV file",".wav"),("MP3 file","mp3"),("M4A file",".m4a"),("OGG file",".ogg"),("Flac file",".flac")])
    if not os.path.exists("Music/"):
        os.makedirs("Music/", mode=0o755, exist_ok=True)
    shutil.copyfile(open_file, os.path.join("Music/", os.path.basename(open_file)))
    music_list.config()


def remove():
    open_file = filedialog.askopenfilename(title="Choose a song", defaultextension=".wav",filetypes=[("WAV file", ".wav"), ("MP3 file", "mp3"), ("M4A file", ".m4a"),("OGG file", ".ogg"), ("Flac file", ".flac")],initialdir="Music/")
    os.remove(open_file)

def volume_sound(event):
    pygame.mixer.music.set_volume(volume_bar.get())


pygame.mixer.init()

song = False


play_image_button = PhotoImage(file='image/play.png')
pause_image_button = PhotoImage(file='image/pause-button.png')
loop_image_button = PhotoImage(file='image/loop-icon.png')
stop_image_button = PhotoImage(file='image/stop-icon.png')
scrolling_sound_bar = PhotoImage(file='image/scroll-bar-in-horizontal.png')


extension_list = [".wav", ".mp3", ".m4a", ".ogg", ".flac"]

music_list = tkinter.Listbox(gui, width=36, font=('Arial', 14))
music_list.grid(row=1, columnspan=7)

def music_file():
    music_list.delete(0, 'end')
    for root, dirs, files in os.walk("Music/"):
        for music in files:
            if any(music.endswith(ext) for ext in extension_list):
                music_list.insert('end', music)
    gui.after(5000, music_file)


name_of_the_song =tkinter.Label(gui, text="", font=('Arial',15))
name_of_the_song.grid(columnspan = 7, row =2)

buttonplay = Button(gui, image=play_image_button, command=play, font=('Arial', 15), height=80, width=60)
buttonplay.grid(column=3, row=6,padx=2)

buttonpause = Button(gui, image=pause_image_button, command=pause, font=('Arial', 15), height=80, width=60)
buttonpause.grid(column=4, row=6,padx=2)

buttonloop = Button(gui, image=loop_image_button, command=loop,font=('Arial',15),height=80,width=60)
buttonloop.grid(column=0 , row=6,padx=2)

buttonstop = Button(gui, image=stop_image_button, command=stop,font=('Arial',15),height=80,width=60)
buttonstop.grid(column=5 , row=6,padx=2)

addbutton = Button(gui, text="add a music", command=add,font=('Arial',15),height=3,width=10)
addbutton.grid(column=2 , row=6,padx=2)

volume_bar = tkinter.Scale(gui, from_=0, to_=1.0, orient="horizontal", resolution=0.1, command=volume_sound,showvalue=0,length=200)
volume_bar.set(0.7)
volume_bar.grid(columnspan=7,row=7, pady=20)

volume_title = Label(text="Volume", font=('Arial',15))
volume_title.grid(column=0,row=7, pady=20)

delete_button =Button(gui, text="Delete", font=('Arial',15), command =remove ,height= 2 , width= 20)
delete_button.grid(columnspan = 7, row =8)


music_file()
gui.mainloop()