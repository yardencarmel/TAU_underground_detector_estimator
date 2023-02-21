from ursina import *


def create_line(start, end, thickness, line_color):
    line = Entity(model=Mesh(vertices=[start, end], mode='line', thickness=thickness), color=line_color)
    return line


def change_app_title(app,title):
    if isinstance(title, str):
        window.title = title


def setup_window(app, borderless=False, fullscreen=False, exit_button=True, fps=False):
    window.borderless = borderless  # Show a border
    window.fullscreen = fullscreen  # Do not go Fullscreen
    window.exit_button.visible = exit_button  # Do not show the in-game red X that loses the window
    window.fps_counter.enabled = fps  # Show the FPS (Frames per second) counter
