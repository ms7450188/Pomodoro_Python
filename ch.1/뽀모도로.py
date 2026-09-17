import tkinter
from tkinter import messagebox

focus_time = 10
break_time = 5

count = focus_time
running = False
is_break = False

def start_timer() :
  global running
  if not running :
    running = True
    countdown()

def stop_timer() :
  global running
  if running :
    running = False

def countdown() :
  global count, running, is_break
  if count > 0 and running :
    count -= 1
    minutes = count // 60
    seconds = count % 60
    label.config(text = f"{minutes:02d}:{seconds:02d}")
    window.after(1000, countdown)
  elif count == 0 :
    if not is_break :
      is_break = True
      count = break_time
      messagebox.showinfo("종료", "집중 끝! 쉬는 시간이다!👏")
    else :
      is_break = False
      count = focus_time
      messagebox.showinfo("집중", "열심히 달려보자!🔥")
    countdown()

window = tkinter.Tk()

window.title("뽀모도로")
window.geometry("620x500+100+100")
window.resizable(True, True)

label = tkinter.Label(window, text = "60:00", width = 20, height = 2, font = ("맑은 고딕", 100))
label.pack()

def toggle_timer() :
  global running
  if not running :
    running = True
    button.config(text = "정지")
    countdown()
  else :
    running = False
    button.config(text = "시작")

button = tkinter.Button(window, text = "시작", width = 10, height = 2, font = ("맑은 고딕", 20), command = toggle_timer)
button.pack()

window.mainloop()