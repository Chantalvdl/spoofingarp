from tkinter import *

screen = Tk()
text = Label(screen, text="Spoofing is leuk!")
text.pack(side=BOTTOM)
bottomframe = Frame(screen)
bottomframe.pack(side=TOP)
buttonSelect = Button(bottomframe, text="Select", fg="blue")
buttonSelect.pack(side=TOP)
one = Label(screen, text="hoi", bg="red", fg="white")
one.pack()
two = Label(screen, text="hoi2", bg="red", fg="white")
two.pack(fill=X)
three = Label(screen, text="hoi3", bg="red", fg="white")
three.pack(side=LEFT, fill=Y)

screen.mainloop()