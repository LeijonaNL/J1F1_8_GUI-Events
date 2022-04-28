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
last_Event = ''

button1 = Button(
    root,
    text = 'Up',
    style = 'button_Config.TButton'
)
button2 = Button(
    root,
    text = 'Down',
    style = 'button_Config.TButton'
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
    global last_Event
    if x == 1:
        last_Event = 'Up'
    elif x == -1:
        last_Event = 'Down'
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

def on_Double(self):
    global value
    global last_Event
    if last_Event == 'Up':
        value *= 3
    elif last_Event == 'Down':
        value /= 3
    if value == 0:
        label.config(text = "There is no number.")
    else:
        label.config(text = f'{value}')
# Binds added for V1
button1.bind("<Button-1>", lambda e: update(1))
button2.bind("<Button-1>", lambda e: update(-1))
# Binds added for V2
label.bind("<Enter>", on_Enter)
label.bind("<Leave>", lambda e: update(0))
# Binds added for V3
label.bind("<Double-Button-1>", on_Double)
# Binds added for V4
root.bind("<Up>", lambda e: update(1))
root.bind("<space>", on_Double)
root.bind("<Down>", lambda e: update(-1))

root.mainloop()