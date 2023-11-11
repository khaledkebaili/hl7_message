from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image ,ImageTk,ImageFilter
import os
from subprocess import call

def showimage():
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select image file",filetype=(("All file","*.*"),("JPG File","*.jpg"),("PNG file","*.png"),("BMP file","*.bmp")))
    img = Image.open(filename)
    img2=img
    img = ImageTk.PhotoImage(img)
    lbl2.configure(image=img)
    lbl2.image=img
    img2 = img2.filter(ImageFilter.MedianFilter(size=3))
    img2 = ImageTk.PhotoImage(img2)
    lbl1.configure(image=img2)
    lbl1.image=img2
    
    
def back():
    root.destroy()
    call(["python", "bienvenue.py"])
    
    

root = Tk()
root.title("filter Moyenneur")
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

