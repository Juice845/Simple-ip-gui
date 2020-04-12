
import socket
from tkinter import *
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

class Window(Frame):


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def displayip(self):
        text = Label(self, text=IPAddr)
        text.place(x=200, y=8)
    def displayhost(self):
        text = Label(self, text=hostname)
        text.place(x=200, y=50)
    def init_window(self):
        self.master.title("IP and Hostname Scanner")
        self.pack(fill=BOTH, expand=1)
        ipButton = Button(self, text="Show This Devices' IP Address", command=self.displayip)
        ipButton.place(x=5, y=5)
        hostButton = Button(self, text="Show This Devices' Name", command=self.displayhost )
        hostButton.place(x=5, y=48)

root = Tk()
root.geometry("400x300")
app = Window(root)
root.mainloop()




