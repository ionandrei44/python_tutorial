from tkinter import *
import os

WIDTH = 500
HEIGHT = 500
IMAGE_WIDTH = 100

x_velocity = 3
y_velocity = 2

script_directory = os.path.dirname(os.path.abspath(__file__))

window = Tk()

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

image_path = os.path.join(script_directory, "car.png")
photo_image = PhotoImage(file=image_path)

# Resize the image to the desired width while preserving aspect ratio
photo_image = photo_image.subsample(int(photo_image.width() / IMAGE_WIDTH))
my_image = canvas.create_image(0, 0, image=photo_image, anchor=NW)

image_width = photo_image.width()
image_height = photo_image.height()


def update_position():
    global x_velocity, y_velocity
    coordinates = canvas.coords(my_image)

    if coordinates[0] >= (WIDTH - image_width) or coordinates[0] < 0:
        x_velocity = -x_velocity

    if coordinates[1] >= (HEIGHT - image_height) or coordinates[1] < 0:
        y_velocity = -y_velocity

    canvas.move(my_image, x_velocity, y_velocity)
    window.after(10, update_position)


update_position()

window.mainloop()
