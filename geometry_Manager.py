from tkinter import *

root = Tk()
root.title('Geometry Manager')
root.geometry('500x500')

label = Label(
    root,
    text = 'label 1',
    bg = 'BLUE',
    fg = 'WHITE'
)
label2 = Label(
    root,
    text = 'label 2',
    bg = 'RED',
    fg = 'WHITE'
)
label.pack()
label2.pack()
label.place(x = 10, y = 20)
label2.place(x = 100, y = 200)
root.mainloop()