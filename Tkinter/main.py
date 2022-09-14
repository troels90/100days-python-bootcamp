from tkinter import *

window = Tk()
window.title("First Tkinter GUI")
window.minsize(width=500, height=300)

def button_clicked():
    my_label["text"] = input.get()

my_label = Label(text="I am label!", font=("Arial", 24, "bold"))

### labels
my_label["text"] = "New label!"
my_label.config(text="New label config!")
my_label.grid(column=0, row=0)

### buttons

button = Button(text="Click Me!", command=button_clicked)
button.grid(column=1, row=1)
button2 = Button(text="No click me!")
button2.grid(column=2, row=0)
### entry

input = Entry(width=40)
input.insert(END, "Write something to label")
input.grid(column=3, row=2)



window.mainloop()