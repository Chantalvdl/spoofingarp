from Tkinter import *
import ttk as t
import scanning as scan

def scanNetworklist():
    networklist= scan.network_scanning()
    return networklist


def scanOpenUsers():
    network = networkChoice.get()
    print(network)
    networkSplit = network.split(', ')
    ipList = scan.ip_scanning(networkSplit)
    return ipList


screen = Tk()
ipList = ["none yet"]
selectNText = Label(screen, text="Select network:")
selectNText.grid(row=0, column=0)
networkChoice = StringVar(screen)
networkChoice.set(scanNetworklist()[0]) # default value
w = OptionMenu(screen, networkChoice, *scanNetworklist())
w.grid(row=0, column=1)

scanOpenButton = Button(screen, text="Scan for victims!", command=scanOpenUsers)
scanOpenButton.grid(row=1, column=1)

ipList = scanOpenUsers()

selectIPText = Label(screen, text="Select victim:")
selectIPText.grid(row=2, column=0)
w2 = t.Combobox(screen, values=ipList[0])
w2.grid(row=2, column=1)

selectRouterText = Label(screen, text="Select router:")
selectRouterText.grid(row=3, column=0)
w3 = t.Combobox(screen, values=ipList[0])
w3.grid(row=3, column=1)

screen.mainloop()

# def button(string, i):
#     i = 0
#     if string == "button":
#         return button
#     return 0

# if button("check", 5) == 1:
#     ipList = scanOpenUsers
#     button(button, 0)
#
# elif button("check", 5) != 1:
#     ipList = ["none yet"]

# ipChoice = StringVar(screen)
# ipChoice.set(ipList[0])
# w2 = OptionMenu(screen, ipChoice, *ipList)
# w2.grid(row=2, column=1)

# routerChoice = StringVar(screen)
# routerChoice.set(ipList[0])
# w3 = OptionMenu(screen, routerChoice, *ipList)
# w3.grid(row=3, column=1)

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