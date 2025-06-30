import tkinter as tk
import random
from core.draw import draw_array
from core.sorter import algorithm_map
from core.controls import create_controls
from core.state import array
from core.theme import theme  # ← Added

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 500

def generate_array(size):
    array.clear()
    array.extend([random.randint(10, 400) for _ in range(size)])
    draw_array(canvas, array, [])

root = tk.Tk()
root.title("Sorting Algorithm Visualizer")
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT + 120}")
root.config(bg=theme["bg"])  # ← Uses theme

canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg=theme["canvas"])  # ← Uses theme
canvas.pack(pady=10)

controls_frame = tk.Frame(root, bg=theme["bg"])
controls_frame.pack()

# Sliders
tk.Label(controls_frame, text="Array Size:", bg=theme["bg"], fg=theme["fg"]).grid(row=0, column=0, padx=5)
size_slider = tk.Scale(controls_frame, from_=10, to=100, orient=tk.HORIZONTAL)
size_slider.set(50)
size_slider.grid(row=0, column=1, padx=5)

tk.Label(controls_frame, text="Speed (ms):", bg=theme["bg"], fg=theme["fg"]).grid(row=0, column=2, padx=5)
speed_slider = tk.Scale(controls_frame, from_=1, to=500, resolution=10, orient=tk.HORIZONTAL)
speed_slider.set(50)
speed_slider.grid(row=0, column=3, padx=5)

algo_var = tk.StringVar()
algo_var.set("Bubble Sort")

create_controls(root, canvas, controls_frame, algo_var, algorithm_map, speed_slider, size_slider, generate_array)

generate_array(size_slider.get())
root.mainloop()
