import requests
from py7zr import py7zr
from tkinter import *

class DuckStationGui:
    def __init__(self,master):
        self.master = master
        master.title('Duckstation Updater')
        master.geometry('200x200')
        self.lbl = Label(master, text="Location Of Duckstation Executable", padx='5', pady='10')
        self.lbl.pack()
        self.location = Entry(master, width=30)
        self.location.pack()
        btn = Button(master, text="Download & Unzip", command=downloadLatest(self), padx='10', pady='10')
        btn.pack()
        self.lbl2 = Label(master, text="Idle", padx='5', pady='10')
        self.lbl2.pack()


        def downloadLatest(self):
            self.lbl2.configure(text='Downloading....')
            url = 'https://github.com/stenzek/duckstation/releases/download/latest/duckstation-windows-x64-release.7z'
            r = requests.get(url, allow_redirects=True)
            open('duckstationlatestwin.7z', 'wb').write(r.content)
            self.lbl2.configure(text='Done :)')



    def unzip_to_folder():
        archive = py7zr.SevenZipFile('duckstationlatestwin.7z', mode='r')
        archive.extractall(path="c:\emulators\duckstation")
        archive.close()

root = Tk()
my_gui = DuckStationGui(root)
root.mainloop()