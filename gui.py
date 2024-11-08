from pathlib import Path

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage 
import time


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")

date = time.strftime("%d/%m/%y")

start , current = 0 , 0

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def enter_start(event):
    global start
    global use
    start = float(entry_star.get())
    use = float(start)
    canvas.itemconfig(start_id,    text=f"Starting - ₹{start}",)    

def button_click():
    global current
    global use
    current = float(entry_cur.get())

    real = float(use -  current)
    if real < 0:
        canvas.itemconfig(curr_id,    text=f"Current - Poor",)
    else:
        canvas.itemconfig(curr_id,    text=f"Current - ₹{real}",)
    
    use = real

def button_press(event):
    button_1.config(image=pressimage , bg="#D9D9D9")

def button_release(event):
    button_1.config(image=relimage, bg="#D9D9D9" )


window = Tk()

window.geometry("782x544")
window.configure(bg = "#D3F58C")


canvas = Canvas(
    window,
    bg = "#D3F58C",
    height = 544,
    width = 782,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    392.0,
    297.0,
    image=image_image_1
)

pressimage = PhotoImage(
    file=relative_to_assets("but_1.png")
)

relimage = PhotoImage(
    file=relative_to_assets("but_2.png")
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    677.0,
    83.0,
    image=image_image_2
)

canvas.create_text(
    612.0,
    71.0,
    anchor="nw",
    text="date - ",
    fill="#000000",
    font=("Holtwood One SC", 13 * -1)
)

canvas.create_text(
    671.0,
    71.0,
    anchor="nw",
    text=f"{date}",
    fill="#000000",
    font=("Holtwood One SC", 13 * -1)
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    392.0,
    32.0,
    image=image_image_3
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    306.0,
    317.5,
    image=entry_image_1
)

entry_star = Entry(
    bg="#A1EFF4",
    bd= 0,
    highlightthickness=0,
)

entry_star.place(
    x =51.0, 
    y = 206.0,
    width=494.0,
    height=39.0
)

entry_cur = Entry(
    bd=0,
    bg="#A1EFF4",
    fg="#000716",
   highlightthickness=0
)
entry_cur.place(
    x=51.0,
    y=372.0,
    width=494.0,
    height=39.0
)

canvas.create_text(
    31.0,
    0.0,
    anchor="nw",
    text="Your Daily Expense",
    fill="#2B7FCC",
    font=("Holtwood One SC", 39 * -1)
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    137.0,
    83.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    379.0,
    83.0,
    image=image_image_5
)

start_id = canvas.create_text(
    36.0,
    73.0,
    anchor="nw",
    text="Starting - ₹",
    fill="#000000",
    font=("Holtwood One SC", 13 * -1)
)

curr_id = canvas.create_text(
    277.0,
    73.0,
    anchor="nw",
    text="Current - ₹",
    fill="#000000",
    font=("Holtwood One SC", 13 * -1)
)


button_1 = Button(
    image=relimage,
    bg="#D9D9D9",
    borderwidth=0,
    highlightthickness=0,
    command=button_click,
    relief="flat"
)
button_1.place(
    x=661.0,
    y=412.0,
    width=87.0,
    height=92.0
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    330.0,
    371.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    299.0,
    201.0,
    image=image_image_7
)

button_1.bind("<Button-1>", button_press)
button_1.bind("<ButtonRelease-1>", button_release)
entry_star.bind("<Return>" , enter_start)

window.resizable(False, False)
window.mainloop()