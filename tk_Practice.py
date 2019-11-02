import random
import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Hello World\n(click me)"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

        self.change = tk.Button(self, text="change", fg="blue", command=self.change2)
        self.change.pack(side="left")

    def say_hi(self):
        print("hi there, everyone!")

    def change2(self):
        colorlist = ['red', 'blue', 'green', 'gray', 'yellow']
        color = random.choice(colorlist)
        color2 = random.choice(colorlist)
        print(color)
        # self.hi_there["fg"] = color
        self.hi_there.config(fg=color, bg=color2)


root = tk.Tk()
app = Application(master=root)
app.master.minsize(400, 400)
text = tk.Entry(root)
text.pack(side="top")
# rum = text+text
dip = tk.Label(text)
dip.pack(side="top")
app.mainloop()
