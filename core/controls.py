from tkinter import *
from core.draw import draw_array
from core.state import array
from core.theme import theme, toggle_theme
from core.descriptions import descriptions
from core.complexity_info import complexity_data

is_paused = False
step_mode = False
step_generator = None
current_generator = None
controls_state = {}

def create_controls(root, canvas, controls_frame, algo_var, algorithm_map, speed_slider, size_slider, generate_array):
    def update_theme(root, canvas, controls_frame):
        root.config(bg=theme["bg"])
        canvas.config(bg=theme["canvas"])
        controls_frame.config(bg=theme["bg"])
        for widget in controls_frame.winfo_children():
            if isinstance(widget, (Button, Label, Checkbutton, Scale, OptionMenu)):
                widget.config(
                    bg=theme["button_bg"],
                    fg=theme["button_fg"],
                    highlightbackground=theme["button_bg"]
                )
        update_checkbox_theme()

    Label(controls_frame, text="Algorithm:", bg=theme["bg"], fg=theme["fg"]).grid(row=1, column=0, pady=10)
    algo_menu = OptionMenu(controls_frame, algo_var, *algorithm_map.keys())
    algo_menu.grid(row=1, column=1, pady=10)

    start_btn = Button(controls_frame, text="Start Sorting", command=lambda: start_sorting(canvas, algo_var.get(), algorithm_map, speed_slider))
    start_btn.grid(row=1, column=2, padx=10)

    controls_state["step_mode_var"] = IntVar()
    step_checkbox = Checkbutton(
        controls_frame,
        text="Step-by-step Mode",
        variable=controls_state["step_mode_var"],
        bg=theme["bg"],
        command=lambda: toggle_step_mode(canvas, speed_slider)
    )
    step_checkbox.grid(row=1, column=3, padx=10)
    controls_state["step_checkbox"] = step_checkbox

    pause_btn = Button(controls_frame, text="Pause", command=lambda: pause_sorting())
    pause_btn.grid(row=1, column=4, padx=5)

    resume_btn = Button(controls_frame, text="Resume", command=lambda: resume_sorting(canvas, speed_slider))
    resume_btn.grid(row=1, column=5, padx=5)

    desc_btn = Button(controls_frame, text="View Description", command=lambda: show_description(algo_var.get()))
    desc_btn.grid(row=2, column=0, columnspan=3, padx=10, pady=(10, 0), sticky="w")

    comp_btn = Button(controls_frame, text="View Complexity", command=lambda: show_complexity(algo_var.get()))
    comp_btn.grid(row=2, column=3, columnspan=3, padx=10, pady=(10, 0), sticky="e")

    controls_state["pause_btn"] = pause_btn
    controls_state["resume_btn"] = resume_btn

    controls_state["next_step_btn"] = Button(controls_frame, text="Next Step", command=lambda: next_step(canvas))
    controls_state["next_step_btn"].grid(row=1, column=6, padx=5)
    controls_state["next_step_btn"].config(state=DISABLED)

    controls_state["generate_btn"] = Button(
        controls_frame, text="Generate Array",
        command=lambda: generate_array(size_slider.get())
    )
    controls_state["generate_btn"].grid(row=0, column=4, padx=10)

    theme_btn = Button(
        controls_frame, text="Dark Mode 🌙",
        command=lambda: [toggle_theme(), update_theme(root, canvas, controls_frame)]
    )
    theme_btn.grid(row=0, column=5, padx=10)

    controls_state["speed_slider"] = speed_slider
    update_theme(root, canvas, controls_frame)

def update_checkbox_theme():
    checkbox = controls_state["step_checkbox"]
    if theme["mode"] == "light":
        checkbox.config(
            selectcolor="#ffffff",  # White box
            fg="#000000",           # Black tick
            activeforeground="#000000"
        )
    else:
        checkbox.config(
            selectcolor="#000000",  # Black box
            fg="#ffffff",           # White tick
            activeforeground="#ffffff"
        )

def start_sorting(canvas, selected_algo, algorithm_map, speed_slider):
    global current_generator, step_generator, step_mode, is_paused
    sorting_fn = algorithm_map[selected_algo]
    generator = sorting_fn(array)
    current_generator = generator
    is_paused = False
    controls_state["generate_btn"].config(state=DISABLED)

    if step_mode:
        step_generator = generator
        controls_state["next_step_btn"].config(state=NORMAL)
        disable_pause_resume()
    else:
        controls_state["next_step_btn"].config(state=DISABLED)
        enable_step_checkbox()
        animate(canvas, generator, speed_slider)

def animate(canvas, generator, speed_slider):
    global is_paused
    try:
        if not is_paused and canvas.winfo_exists():
            arr, highlights = next(generator)
            draw_array(canvas, arr, highlights)
            canvas.after(speed_slider.get(), lambda: animate(canvas, generator, speed_slider))
    except StopIteration:
        draw_array(canvas, array)
        controls_state["generate_btn"].config(state=NORMAL)

def next_step(canvas):
    global step_generator
    try:
        arr, highlights = next(step_generator)
        draw_array(canvas, arr, highlights)
    except StopIteration:
        controls_state["next_step_btn"].config(state=DISABLED)
        draw_array(canvas, array)
        controls_state["generate_btn"].config(state=NORMAL)

def pause_sorting():
    global is_paused
    is_paused = True
    if not step_mode:
        enable_step_checkbox()

def resume_sorting(canvas, speed_slider):
    global is_paused
    if current_generator is None or step_mode:
        return
    is_paused = False
    disable_step_checkbox()
    animate(canvas, current_generator, speed_slider)

def toggle_step_mode(canvas, speed_slider):
    global step_mode, step_generator, is_paused

    requested = controls_state["step_mode_var"].get() == 1

    if requested:
        if not is_paused and current_generator is not None:
            # Disallow entering step mode unless paused
            controls_state["step_mode_var"].set(0)
            print("Pause sorting first before entering step-by-step mode.")
            return
        step_mode = True
        step_generator = current_generator
        controls_state["next_step_btn"].config(state=NORMAL)
        disable_pause_resume()
    else:
        step_mode = False
        is_paused = True  # Stay paused after unchecking
        controls_state["next_step_btn"].config(state=DISABLED)
        enable_pause_resume()

def disable_pause_resume():
    controls_state["pause_btn"].config(state=DISABLED)
    controls_state["resume_btn"].config(state=DISABLED)

def enable_pause_resume():
    controls_state["pause_btn"].config(state=NORMAL)
    controls_state["resume_btn"].config(state=NORMAL)

def disable_step_checkbox():
    controls_state["step_checkbox"].config(state=DISABLED)

def enable_step_checkbox():
    controls_state["step_checkbox"].config(state=NORMAL)



from tkinter import Toplevel, Text, Scrollbar, RIGHT, Y, END, DISABLED, NORMAL

def show_popup(title, text, theme):
    win = Toplevel()
    win.title(title)
    win.config(bg=theme["bg"])
    win.resizable(False, False)

    text_box = Text(win, height=12, width=60, wrap="word", bg=theme["bg"], fg=theme["fg"])
    text_box.insert(END, text)
    text_box.config(state=DISABLED)
    text_box.pack(padx=10, pady=10)

def show_description(algo_name):
    from core.controls import theme  # use current theme
    desc = descriptions.get(algo_name, "No description available.")
    show_popup(f"{algo_name} - Description", desc, theme)

def show_complexity(algo_name):
    from core.controls import theme
    data = complexity_data.get(algo_name)
    if not data:
        text = "No complexity data available."
    else:
        text = f"""Algorithm: {algo_name}

Time Complexity:
  Best: {data['best']}
  Average: {data['avg']}
  Worst: {data['worst']}

Space Complexity: {data['space']}
Stable: {data['stable']}"""
    show_popup(f"{algo_name} - Complexity", text, theme)
