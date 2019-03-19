from Tkinter import *
import scanning as scan

def scanNetworklist():
    networklist = scan.network_scanning()
    return networklist


def scanOpenUsers():
    ipList = scan.ip_scanning()
    return True


def spoofclick():
    spoof = 1


screen = Tk()
selectNText = Label(screen, text="Select network:")
selectNText.grid(row=0, column=0)
variable = StringVar(screen)
variable.set(scanNetworklist()[0]) # default value

w = OptionMenu(screen, variable, *scanNetworklist())
w.grid(row=0, column=1)
scanOpenButton = Button(screen, text="Scan for victims!")
scanOpenButton.grid(row=1, column=1)

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