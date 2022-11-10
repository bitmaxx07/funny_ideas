from tkinter import *
from tkinter import messagebox, filedialog
import moviepy.editor as mp
import os


class Window(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.select_btn = Button(master, text="select video file", command=self.select_file)
        self.select_btn.place(x=40, y=20)
        self.video_file = ""
        self.output_btn = Button(master, text="select output path", command=self.select_output)
        self.output_btn.place(x=40, y=60)
        self.output_file = ""
        self.start_btn = Button(master, text="start", command=self.start)
        self.start_btn.place(x=40, y=100)

    def select_file(self):
        self.video_file = filedialog.askopenfile(title="select video file").name

    def select_output(self):
        self.output_file = filedialog.askdirectory(title="select output path")

    def start(self):
        if self.video_file == "" or self.output_file == "":
            answer = messagebox.askokcancel(message="file selection not completed")
            if answer:
                messagebox.showinfo(message="pls select again")
        else:
            clip = mp.VideoFileClip(self.video_file)
            clip.audio.write_audiofile(self.output_file + os.path.basename(self.video_file) + ".mp3")
            messagebox.showinfo("done!")


root = Tk()
Window(root)
root.title("audio_extractor")
root.geometry("400x300")
root.mainloop()
