from tkinter import *
from ball import *

window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas, 0, 0, 100, 1, 1, "red")
tennis_ball = Ball(canvas, 0, 0, 50, 4, 3, "green")
basket_ball = Ball(canvas, 0, 0, 125, 5, 8, "orange")


def animate():
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()
    window.after(10, animate)


animate()

window.mainloop()
