from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #
def cancel():
    window.after_cancel(timer)
    global reps
    reps = 0
    title_label.config(text="Timer")
    checkLabel.config(text="")
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #

minutes = WORK_MIN


def start():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    formatted_time = f"{count // 60}:{'%02d' % (count % 60,)}"
    canvas.itemconfig(timer_text, text=formatted_time)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start()
        # checkLabel['text'] += "✔"
        mark = ""
        work_sessions = reps // 2
        for _ in range(work_sessions):
            mark += "✔"
        checkLabel['text'] = mark

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

img = PhotoImage(file="tomato.png")
canvas = Canvas(width=220, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(103, 112, image=img)
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(column=1, row=1)

title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, "normal"))
title_label.grid(column=1, row=0)

start_button = Button(text="Start", border=0, highlightthickness=0, padx=10, pady=3, command=start)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", border=0, highlightthickness=0, padx=10, pady=3, command=cancel)
reset_button.grid(column=2, row=2)

checkLabel = Label(fg=GREEN, bg=YELLOW)
checkLabel.grid(column=1, row=3)

window.mainloop()
