import nltk
from tkinter import *
from tkinter import messagebox

window = Tk()
window.config(width=540, height=540)
window.title("Jumbled Words")

def jumble():
    puzzle_letters = nltk.FreqDist(Entry1.get())
    obligatory = Entry2.get()
    numletters = Entry3.get()
    wordlist = nltk.corpus.words.words()
    result = [w for w in wordlist if len(w) >= int(numletters) and obligatory in w and nltk.FreqDist(w) <= puzzle_letters ]
    messagebox.showinfo(title="Here are the words", message=f"{result}")


Label1 = Label(text="Jumbled Words", font=("Arial",28,"normal"))
Label1.grid(row=0, column=1)
Label2 = Label(text="Enter the jumbled letters:", font=("Arial",15,"normal"))
Label2.grid(row=1, column=1)
Label3 = Label(text="What is the obligatory letter?", font=("Arial",15,"normal"))
Label3.grid(row=2, column=1)
Label4 = Label(text="Number of letters:", font=("Arial",15,"normal"))
Label4.grid(row=3, column=1)
Entry1 = Entry(width=35)
Entry1.grid(row=1, column=2)
Entry2 = Entry(width=35)
Entry2.grid(row=2, column=2)
Entry3 = Entry(width=35)
Entry3.grid(row=3, column=2)

button1 = Button(text="Generate", command=jumble)
button1.grid(row=4, column=2)
window.mainloop()

