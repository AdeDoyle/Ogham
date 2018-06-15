"""This version especially for use reverse-transliterating the transcriptions on ogham.celt.dias.ie without losing
   metadata and diacritics present in the transcriptions."""

from tkinter import *
from Ogham_GO_For3D import deanogham
from Ogham_OG import aistrighogham


class Application(Frame):
    """The GUI Application"""

    def __init__(self, master):
        """Initialises the frame"""
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """Creates Widgets for Buttons and Text Input and Output"""
        self.instruction = Label(self, text = "Enter Text Here:")
        self.instruction.grid(row=0, column=0, columnspan=2, sticky=W)

        self.intext = Text(self, width=149, height=15, wrap=WORD)
        self.intext.grid(row=1, column=0, columnspan=2, sticky=W)

        self.runapp = Button(self, text = "Gaeilge - Ogham (Orthodox)", command=self.ga_og)
        self.runapp.grid(row=2, column=1, sticky=W)

        self.runapp = Button(self, text="Gaeilge - Ogham (Scholastic)", command=self.ga_sog)
        self.runapp.grid(row=3, column=1, sticky=W)

        self.runapp = Button(self, text="Ogham - Gaeilge", command=self.og_ga)
        self.runapp.grid(row=4, column=1, sticky=W)

        self.outtext = Text(self, width=149, height=15, wrap=WORD)
        self.outtext.grid(row=5, column=0, columnspan=2, sticky=W)

    def ga_og(self):
        """Display output text in Orthodox Ogham."""
        content = self.intext.get(1.0, END)
        output = deanogham(content)
        output = output[:-2]+output[-1:]
        self.outtext.delete(1.0, END)
        self.outtext.insert(0.0, output)

    def ga_sog(self):
        """Display output text in Scholastic Ogham."""
        content = self.intext.get(1.0, END)
        output = deanogham(content, "scholastic")
        output = output[:-2] + output[-1:]
        self.outtext.delete(1.0, END)
        self.outtext.insert(0.0, output)

    def og_ga(self):
        """Display output text in Irish (Roman characters)."""
        content = self.intext.get(1.0, END)
        output = aistrighogham(content)
        output = output[:-1]
        self.outtext.delete(1.0, END)
        self.outtext.insert(0.0, output)


app = Tk()
app.title("Ogham")
app.geometry('1200x600')
appli = Application(app)

app.mainloop()
