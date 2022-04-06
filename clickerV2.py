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
    if O:
        V += 1
    elif not O:
        V -= 1
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
label.bind('<Enter>', on_Enter)
label.bind('<Leave>', on_Leave)

root.mainloop()