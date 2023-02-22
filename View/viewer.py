from ursina import Entity, Mesh, window


def draw_line(start, end, thickness, line_color):
    line = Entity(model=Mesh(vertices=[start, end], mode='line', thickness=thickness), color=line_color)
    return line


def draw_cube(pos, size, color):
    cube = Entity(model='cube', world_position=pos, scale=size, color=color, collider='box', mode='line')
    return cube


def draw_wireframe_cube(pos, size, color):
    cube = Entity(model='wireframe_cube', world_position=pos, scale=size, color=color, collider='box', mode='line')
    return cube


# TODO: understand if there is a gridded full box (not transparent)

def change_app_title(app, title):
    if isinstance(title, str):
        print(title)
        window.borderless = False
        window.title = title


def setup_window(app, borderless=False, fullscreen=False, exit_button=True, fps=False):
    window.borderless = borderless  # Show a border
    window.fullscreen = fullscreen  # Do not go Fullscreen
    window.exit_button.visible = exit_button  # Do not show the in-game red X that loses the window
    window.fps_counter.enabled = fps  # Show the FPS (Frames per second) counter
