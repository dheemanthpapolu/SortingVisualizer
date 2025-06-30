WINDOW_WIDTH = 900
WINDOW_HEIGHT = 500
BAR_COLOR = "#4a90e2"
BAR_GAP = 2

def draw_array(canvas, arr, color_indices=[]):
    canvas.delete("all")
    canvas_width = WINDOW_WIDTH - 40
    bar_width = canvas_width / len(arr)
    for i, value in enumerate(arr):
        x0 = i * bar_width + BAR_GAP
        y0 = WINDOW_HEIGHT - value
        x1 = (i + 1) * bar_width
        y1 = WINDOW_HEIGHT
        color = "red" if i in color_indices else BAR_COLOR
        canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline="")
    canvas.update_idletasks()
