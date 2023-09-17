from tkinter import *

window = Tk()
window.title("GUI size converter cm to inches")
window.minsize(width=500, height=300)


# Label
my_label = Label(text="cm")
my_label.grid(column=4, row=0)
is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=2, row=1)
km = Label(text="inches")
km.grid(column=4, row=1)
result = Label(text="")
result.grid(column=3, row=1)



def calculate():
      conv = int(input.get())
      converter =  conv * 2.54
      result.config(text= f"{converter}")

#Button


button = Button(text="click me", command=calculate)
button.grid(column=3, row=3)



#entry

input = Entry()
input.grid(column=3, row=0)

window.mainloop()
