import tkinter as tk
from tkinter import filedialog
from pygame import mixer

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.path = '' #define a variable for music path in this class

    def create_widgets(self):
        #file selection button
        self.choose = tk.Button(self)
        self.choose['text'] = 'choose a music to play'
        self.choose['command'] = self.choosemusic
        self.choose.pack(side='top')        

        #play button
        self.play = tk.Button(self)
        self.play['text'] = 'Play'
        self.play['command'] = self.playmusic
        self.play.pack(side='top')

        #pause button
        self.pause = tk.Button(self)
        self.pause['text'] = 'Pause'
        self.pause['command'] = self.pausemusic
        self.pause.pack(side='left')

        #resume button
        self.unpause = tk.Button(self)
        self.unpause['text'] = 'Resume'
        self.unpause['command'] = self.unpausemusic
        self.unpause.pack(side='right')

        #stop button
        self.stop = tk.Button(self)
        self.stop['text'] = 'Stop'
        self.stop['command'] = self.stopmusic
        self.stop.pack(side='bottom')

        #quit button
        self.quit = tk.Button(self, text='Quit', fg='red', command=root.destroy)
        self.quit.pack(side='bottom')

    #functions to be defined
    def choosemusic(self):
        self.path = filedialog.askopenfile(mode='rb',title='Pick a music file')
 

    def playmusic(self):
        mixer.init()
        mixer.music.load(self.path)
        mixer.music.play()

    def pausemusic(self):
        mixer.music.pause()

    def unpausemusic(self):
        mixer.music.unpause()

    def stopmusic(self):
        mixer.music.stop()



root = tk.Tk()
app = Application(master=root)
app.master.title('yuzuohong music player')
app.master.maxsize(1000,500)
app.mainloop()

