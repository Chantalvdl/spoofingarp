from tkinter import *

screen = Tk()
text = Label(screen, text="Spoofing is leuk!")
text.pack(side=BOTTOM)
bottomframe = Frame(screen)
bottomframe.pack(side=TOP)
buttonSelect = Button(bottomframe, text="Select", fg="blue")
buttonSelect.pack(side=TOP)
screen.mainloop()