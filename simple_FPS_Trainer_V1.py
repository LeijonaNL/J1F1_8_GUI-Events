from random import randint
from tkinter import Tk, messagebox
from tkinter.ttk import Style, Label, Button

def FPStrainer():
    global countdown_time
    global score
    events = [' Press: W ', ' Press: A ', ' Press: S ', ' Press: D ', ' Press: Space ', ' Single Click ', ' Double Click ', ' Triple Click ']
    keys = ('<w>', '<a>', '<s>', '<d>', '<space>', '<Button-1>', '<Double-Button>', '<Triple-Button>')

    countdown_time = 20
    score = 0

    root = Tk()
    root.title('FPS trainer')
    root.geometry('500x400')

    button_Style = Style()
    scoreboard_Style = Style()
    label_Style = Style()

    button_Style.configure(
        'button_Config.TButton',
        background = 'grey',
        foreground = 'black',
        height = 3,
        font = ('Arial', 20)
    )
    scoreboard_Style.configure(
        'scoreboard_Config.TLabel',
        background = 'black',
        foreground = 'white',
        width = 250,
        height = 1,
        font = ('Arial', 11)
    )
    label_Style.configure(
        'label_Config.TLabel',
        background = 'grey',
        foreground = 'black',
        height = 2,
        font = ('Arial', 11)
    )

    start_Button = Button(
        root,
        style = 'button_Config.TButton',
        text = 'Press to start'
    )
    scoreboard_time = Label(
        root,
        style = 'scoreboard_Config.TLabel',
        text = f'    Time Remaining: {countdown_time} sec',
    )
    scoreboard_score = Label(
        root,
        style = 'scoreboard_Config.TLabel',
        text = f'Score: {score} points'
    )
    label = Label(
        root,
        style = 'label_Config.TLabel'
    )

    start_Button.pack()
    start_Button.place(x = 160, y = 180)
    scoreboard_time.pack()
    scoreboard_time.place(x = 0, y = 1)
    scoreboard_score.pack()
    scoreboard_score.place(x = 300, y = 1)

    def update_time(t):
        scoreboard_time.configure(text = f'    Time Remaining: {t} sec')
        t -= 1
        root.after(1000, lambda: update_time(t))

    def update(s):
        global score
        score+=s
        scoreboard_score.configure(text = f'Score: {score} points')
        for i in keys:
            root.unbind(i)
        event = events[randint(0, 7)]
        label.configure(text = event)
        label.place(x = randint(75, 410), y = randint(25, 375))
        if event == events[0]:
            root.bind("<w>", lambda e: update(2))
        elif event == events[1]:
            root.bind("<a>", lambda e: update(2))
        elif event == events[2]:
            root.bind("<s>", lambda e: update(2))
        elif event == events[3]:
            root.bind("<d>", lambda e: update(2))
        elif event == events[4]:
            root.bind("<space>", lambda e: update(2))
        elif event == events[5]:
            root.bind("<Button-1>", lambda e: update(1))
        elif event == events[6]:
            root.bind("<Double-Button>", lambda e: update(1))
        elif event == events[7]:
            root.bind("<Triple-Button>", lambda e: update(1))

    def end_yes_no():
        global score
        response = messagebox.askquestion('Retry?', f'Score: {score}\nWould you like to try again?')
        if response == 'yes':
            messagebox.showinfo('Response', 'The trainer has been reset.')
            refresh()
        elif response == 'no':
            messagebox.showinfo('Response', 'The trainer has closed.')
            root.destroy()
        else:
            messagebox.showwarning('ERROR', 'Something went wrong.')

    def main_function():
        global score
        global countdown_time
        start_Button.destroy()
        label.pack()
        update(0)
        update_time(countdown_time)
        start_Button.after(20000, lambda: end_yes_no())

    start_Button.configure(command= lambda: main_function())

    def refresh():
        root.destroy()
        FPStrainer()

    root.mainloop()

FPStrainer()