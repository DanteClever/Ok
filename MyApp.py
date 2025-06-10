import tkinter as tk
import json
import pygame
import time
from tkinter.messagebox import showinfo
from tkinter.messagebox import askyesno
from tkinter import filedialog
from tkinter import filedialog as fd
import cv2 
import numpy as np
import audioread
from tkinter.colorchooser import askcolor
root = tk.Tk()


root.configure(bg='#38b6ff')

root.title("Wave Of Emotions")

root.resizable(False, False)
root.geometry('800x600+50+50')

p1 = tk.PhotoImage(file = 'C:/Users/dani/Desktop/p_music_play/image/icon.png') 
  
# Setting icon of master window 
root.iconphoto(False, p1)


#aks ha ....
#bg="#08022D
aks_play = tk.PhotoImage(file="C:/Users/dani/Desktop/p_music_play/image/play.png")
aks_chap_play = tk.PhotoImage(file='C:/Users/dani/Desktop/p_music_play/image/chap.png')
aks_rast_play =   tk.PhotoImage(file='C:/Users/dani/Desktop/p_music_play/image/rast.png')
stop_play = tk.PhotoImage(file='C:/Users/dani/Desktop/p_music_play/image/stop.png')
tekrar = tk.PhotoImage(file='C:/Users/dani/Desktop/p_music_play/image/tekrar.png')
tekrar_koli = tk.PhotoImage(file='C:/Users/dani/Desktop/p_music_play/image/01.png')
setarh = tk.PhotoImage(file='C:/Users/dani/Desktop/p_music_play/image/setarh.png')
#aks_number0 = tk.PhotoImage(file='C:/Users/dani/Desktop/p_music_play/image/stop.png')
#.........................................................................................................................

#tk.Label(root,image=img).place(x=-10,y=470)






filename = fd.askopenfilename(initialdir="/", title="Open File", filetypes=((".MP3", "*.mp3"),(".WMA", "*.wma"),(".WAV", "*.wav"), ("All Files", "*.*")))



def play():
        tek = pygame.mixer.music.load((filename))
        piplay = pygame.mixer.music.play()
        def time_music(length): 
            hours = length // 3600  # calculate in hours 
            length %= 3600
            mins = length // 60  # calculate in minutes 
            length %= 60
            seconds = length  # calculate in seconds 
  
            return hours, mins, seconds

            with audioread.audio_open(filename) as f:
                    
                    
    

                    totalsec = f.duration
    
                    hours, mins, seconds = time_music(int(totalsec)) 
                    tk.Label(root,text='Time Music: {}:{}:{}'.format(hours, mins, seconds)).place(x=0 , y=510)

   


        
#def color_list():
        
        
   
#   color = askcolor()
#   print(color)

   

#colors = tk.Button(root , text='color'  , command=color_list).pack()

def rast_play():
        
        pass
def chap_play():
        pass








        









pygame.init()

        
def tekrar_music():
        pygame.mixer.music.play(-1)








def unpause():
        un2 = tk.Button(root,text="Play", image = stop_play, borderwidth=-0, command=pause).place(x=460 , y=530)
        pygame.mixer.music.unpause()

def pause():
        unpp = tk.Button(root,text="Play", image = stop_play, borderwidth=-0, command=unpause).place(x=460 , y=530)
        pygame.mixer.music.pause()

def stop():
        pygame.mixer.music.stop()



tekk= tk.Button(root,text="0", image = tekrar, borderwidth=-0, command=tekrar_music).place(x=230 , y=530)

play_chap  = tk.Button(root,text="00", image = aks_chap_play, borderwidth=-0, command=chap_play).place(x=290 , y=530)
stop_koli = tk.Button(root,text="Play", image = tekrar_koli, borderwidth=-0, command=stop).place(x=340 , y=530)
play  = tk.Button(root,text="Play", image = aks_play, borderwidth=-0, command=play).place(x=400 , y=530)
stop= tk.Button(root,text="Play", image = stop_play, borderwidth=-0, command=pause).place(x=460 , y=530)
play_rast = tk.Button(root,text="00", image = aks_rast_play, borderwidth=-0, command=rast_play).place(x=510 , y=530)
#tk.Button(root,text="Play", image = stop_play, borderwidth=-0, command=open_file_me()).place(x=0 , y=0)
#tx = tk.Label(root, text="Welcome To App Me" , bg="blue" ).grid(padx=1,pady=0)

def foff(event):
        
        root.focus()
        

def quit_app(event):
        
        foff(event)
    
        answer = askyesno(title='confirmation',
                          
                      
                      
                          
                      
                      
                      
                        
                      
                        message='Are you sure that you want to quit?')
        if answer:
        
                root.destroy()
    
root.bind("<Shift_L> <Q>" , quit_app) 
root.bind("<Shift_L> <q>" , quit_app)
root.bind("<BackSpace>",pause)
#gr = root.bind("<Return>" , foff)


def quit_appp():
    
    answer = askyesno(title='Quit?',
                      
                      
                      
                     message='Are you sure that you want to quit?')
    if answer:
        
        root.destroy()

#

#





#def grftan_chat():
    
#

def file_save():
        detame ={1:filename} 
        print(detame[1])
        
   
        
        with open("f/p_music_play/deta/Deta001.json", "w") as outfile: 
            json.dump(detame, outfile)


dk = tk.Button(root, text="Save Music Link",  command=file_save).pack()


#



#chat =tk.Entry(root,text="Text...",bg="white" , fg="red")
#chat.pack()
#chat.focus()


#


#


root.mainloop()
