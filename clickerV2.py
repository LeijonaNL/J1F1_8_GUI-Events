from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Clicker')
root.geometry('500x400')
root.config(bg = 'GREY')

style = Style()
style.configure(
    'button_Config.TButton',
    bg = 'WHITE',
    fg = 'BLACK',
    width = 10,
    height = 2,
    font = ('Arial', 11)
)

value = 0

button1 = Button(
    root,
    text = 'Up',
    style = 'button_Config.TButton',
    command = lambda: update(1)
)
button2 = Button(
    root,
    text = 'Down',
    style = 'button_Config.TButton',
    command = lambda: update(-1)
)
label = Label(
    root,
    style = 'button_Config.TButton',
    text = (f'{value}')
)
button1.pack(ipadx = 50, ipady = 10, pady = 50)
label.pack(ipadx = 50, ipady = 10)
button2.pack(ipadx = 50, ipady = 10, pady = 50)

def update(x):
    global value
    value += x
    label.config(text = f'{value}')
    if value == 0:
        root.config(bg = 'GREY')
    elif value > 0:
        root.config(bg = 'GREEN')
    elif value < 0:
        root.config(bg = 'RED')

def on_Enter(self):
    root.config(bg = 'YELLOW')
    
label.bind('<Enter>', on_Enter)
label.bind('<Leave>', lambda e: update(0))

root.mainloop()