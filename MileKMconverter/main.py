from tkinter import *

window = Tk()
window.title("Widget Examples")
window.minsize(width=300, height=300)
window.config(padx=50, pady=50)

typeText = Label(text="Miles or KM ?")
typeText.grid(column=2, row=2)
equalText = Label(text="", font=("Arial", 16), pady=40)
equalText.grid(column=1, row=5)

def button_calculate():
    if radio_state.get() == 1 or radio_state.get() == 2:
        amount = float(input.get())
        if radio_state.get() == 1:
           amount *= 1.61
        elif radio_state.get() == 2:
            amount /= 1.61

        amount = round(amount, 1)
        text = str(input.get()) + " is equal to " + str(amount)
        equalText["text"] = text
    else:
        equalText["text"] = "Please choose miles or kilometers"

def radio_used():
    if radio_state.get() == 1:
        print("Tjek 1")
        typeText["text"] = "Miles"
    elif radio_state.get() == 2:
        print("Tjek 2")
        typeText["text"] = "Kilometers"



radio_state = IntVar()
radiobutton1 = Radiobutton(text="Miles to KM", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="KM to Miles", value=2, variable=radio_state, command=radio_used)
radiobutton1.grid(column=1, row=0)
radiobutton2.grid(column=1, row=1)

input = Entry(width=20)
input.grid(column=1, row=2)

button = Button(text="Calculate", command=button_calculate)
button.grid(column=1, row=3)


window.mainloop()
