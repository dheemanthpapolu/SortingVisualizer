theme = {
    "mode": "light",
    "bg": "#f0f0f0",
    "fg": "black",
    "canvas": "white",
    "button_bg": "#e0e0e0",
    "button_fg": "black"
}

def toggle_theme():
    if theme["mode"] == "light":
        theme.update({
            "mode": "dark",
            "bg": "#1e1e1e",
            "fg": "#f0f0f0",
            "canvas": "#2b2b2b",
            "button_bg": "#333333",
            "button_fg": "#f0f0f0"
        })
    else:
        theme.update({
            "mode": "light",
            "bg": "#f0f0f0",
            "fg": "black",
            "canvas": "white",
            "button_bg": "#e0e0e0",
            "button_fg": "black"
        })
