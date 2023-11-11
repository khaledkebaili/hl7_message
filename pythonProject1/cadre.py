from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image ,ImageTk,ImageFilter
import os
from subprocess import call

def showimage():
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),title="Select image file",filetype=(("All file","*.*"),("JPG File","*.jpg"),("PNG file","*.png"),("BMP file","*.bmp")))
    img = Image.open(filename)
    img = img.resize((350, 500), Image.ANTIALIAS)
    img2=img
    img2 = img2.resize((330, 480), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    lbl2.configure(image=img)
    lbl2.image=img
    border_size = 10
    border_color = (255, 100, 0)
    new_width = img2.width + 2 * border_size
    new_height = img2.height + 2 * border_size
    new_img = Image.new("RGB", (new_width, new_height), border_color)
    x = border_size
    y = border_size
    new_img.paste(img2, (x, y))
    new_img = ImageTk.PhotoImage(new_img)
    lbl1.configure(image=new_img)
    lbl1.image=new_img
    
    
def back():
    root.destroy()
    call(["python", "bienvenue.py"])
    
    

root = Tk()
root.title("cadre")
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
