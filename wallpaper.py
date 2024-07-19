from tkinter import *
from PIL import ImageTk, Image
import os

def next_img():
    global counter
    if counter==len(imgs):
        counter=0
    il.config(image=imgs[counter])
    counter += 1
counter =1
r = Tk()
r.title('Wallpaper Viewer')

r.geometry("400x500")
r.config(background='black')
f=os.listdir('wallpapers')
imgs=[]
for i in f:
    imgs.append(ImageTk.PhotoImage(Image.open(os.path.join('wallpapers',i)).resize((300,400))))
il=Label(r,image=imgs[0])
il.pack(pady=(15,15))
next=Button(r,text='Next',width=42,height=2,command=next_img)
next.pack()
r.mainloop()