from tkinter import *
from tkinter import filedialog as fd 
from PIL import Image, ImageTk,ImageDraw, ImageFont

if __name__ == "__main__":
    root = Tk()

    frame = Frame(root, bd=2, relief=SUNKEN)
    frame.grid_rowconfigure(0, weight=1)
    frame.grid_columnconfigure(0, weight=1)
    xscroll = Scrollbar(frame, orient=HORIZONTAL)
    xscroll.grid(row=1, column=0, sticky=E+W)
    yscroll = Scrollbar(frame)
    yscroll.grid(row=0, column=1, sticky=N+S)
    canvas = Canvas(frame, bd=0, xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
    canvas.grid(row=0, column=0, sticky=N+S+E+W)
    xscroll.config(command=canvas.xview)
    yscroll.config(command=canvas.yview)
    frame.pack(fill=BOTH,expand=1)

    File = fd.askopenfilename(parent=root, initialdir="C:/",title='Choose an image.')
    name = File
    x = name.split('.')
    extension = x[1]

    print(name)
    img = ImageTk.PhotoImage(Image.open(File))
    canvas.create_image(0,0,image=img,anchor="nw")
    canvas.config(scrollregion=canvas.bbox(ALL))

    #function to be called when mouse is clicked
    def printcoords(event):
        #outputting x and y coords to console
        print (event.x,event.y)
        im = Image.open(name)
        d = ImageDraw.Draw(im)
        location = (event.x,event.y)
        text_color = (0, 137, 209)
        font = ImageFont.truetype('arial.ttf', 150)
        d.text(location, 'krish', fill=text_color, font=font)
        im.save('certificate_' + 'krish.'+extension)
        exit(0)


    #mouseclick event
    canvas.bind("<Button 1>",printcoords)

    root.mainloop()
    
