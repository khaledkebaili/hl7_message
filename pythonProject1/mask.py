from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image ,ImageTk,ImageFilter
import os
from subprocess import call
import numpy as np
from matplotlib import pyplot as plt

def showimage():
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select image file",filetype=(("All file","*.*"),("JPG File","*.jpg"),("PNG file","*.png"),("BMP file","*.bmp")))
    img = Image.open(filename)
    
    img2 = img
    img1 = np.array(img2)
    indices = np.where(np.logical_and(img1 >= 0, img1 <= 15))
    indices2 = np.where(np.logical_and(img1 >= 240, img1 <= 255))
    img1[indices] = 128
    img1[indices2] = 128
    img3 = Image.fromarray(img1)
    img2=img3
    img2 = ImageTk.PhotoImage(img2) 
    lbl1.configure(image=img2)
    lbl1.image=img2
    img = ImageTk.PhotoImage(img)
    lbl2.configure(image=img)
    lbl2.image=img
    
def back():
    root.destroy()
    call(["python", "bienvenue.py"])
    
    

root = Tk()
root.title("Mask")
root.geometry("910x600")
root.resizable(width=False,height=False)


lbl2=Label(root)
lbl2.place(x=10,y=0,width=400)

lbl1=Label(root)
lbl1.place(x=500,y=0,width=400)

btn=Button(root,text="Select Image",command=showimage)
btn.place(x=50,y=550,width=250)
btn=Button(root,text="Back",command=back)
btn.place(x=310,y=550,width=250)
                                        

                                       
root.mainloop()
