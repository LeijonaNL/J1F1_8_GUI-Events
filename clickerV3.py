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
    style = 'button_Config.TButton',
    command = lambda: update(value, True)
)
button2 = Button(
    root,
    text = 'Down',
    style = 'button_Config.TButton',
    command = lambda: update(value, False)
)
label = Label(
    root,
    style = 'button_Config.TButton',
    text = (f'{value}')
)
button1.pack(ipadx = 50, ipady = 10, pady = 50)
label.pack(ipadx = 50, ipady = 10)
button2.pack(ipadx = 50, ipady = 10, pady = 50)

def update(V, O):
    global value
    global last_Event
    if O:
        V += 1
        last_Event = 'Up'
    elif not O:
        V -= 1
        last_Event = 'Down'
    value = V
    label.config(text = f'{V}')
    if V == 0:
        root.config(bg = 'GREY')
    elif V > 0:
        root.config(bg = 'GREEN')
    elif V < 0:
        root.config(bg = 'RED')

def on_Enter(self):
    root.config(bg = 'YELLOW')
def on_Leave(self):
    global value
    V = value
    if V == 0:
        root.config(bg = 'GREY')
    elif V > 0:
        root.config(bg = 'GREEN')
    elif V < 0:
        root.config(bg = 'RED')

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

label.bind('<Enter>', on_Enter)
label.bind('<Leave>', on_Leave)
label.bind('<Double-Button-1>', on_Double)

root.mainloop()