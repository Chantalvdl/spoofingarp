from tkinter import *

def scanlist():
    scan = 1

def spoofclick():
    spoof = 1

screen = Tk()

toprightframe = Frame(screen, bg="blue", text="2")
bottomrightframe = Frame(screen, bg="yellow", text="3")
topleftframe = Frame(screen, bg="red", text="1")
bottomleftframe = Frame(screen)
toprightframe.pack(side=TOP)
bottomrightframe.pack(side=BOTTOM)
topleftframe.pack(side=TOP)
bottomleftframe.pack(side=BOTTOM)


screen.mainloop()


# Handige aantekeningen gui tutorials

# dropdown menu
# menu = Menu(screen)
# screen.config(menu=menu)
# submenu = Menu(menu)
# menu.add_cascade(label="Spoofing", menu=submenu)
# submenu.add_command(label="spoof!")


# text = Label(screen, text="Spoofing is leuk!")
# text.pack(side=BOTTOM)
# bottomframe = Frame(screen)
# bottomframe.pack(side=TOP)
# buttonSelect = Button(bottomframe, text="Select", fg="blue", command=scanning.scanning)
# buttonSelect.bind("<Button-1>", def name)
# buttonSelect.pack(side=TOP)
# one = Label(screen, text="hoi", bg="red", fg="white")
# one.pack()
# two = Label(screen, text="hoi2", bg="red", fg="white")
# two.pack(fill=X)
# three = Label(screen, text="hoi3", bg="red", fg="white")
# three.pack(side=LEFT, fill=Y)