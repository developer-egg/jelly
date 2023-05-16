import sys
import sdl2.ext

class Window:
    """
    Instantiate a game window.

    :param title: The title of the window.
    :type title: str

    :param width: The width of the window.
    :type width: int

    :param height: The height of the window.
    :type height: int
    """

    def __init__(self, title, width, height):
        self.width = width
        self.height = height
        self.title = title

        sdl2.ext.init()

        # sdl_window should be used when accessing sdl window methods
        self.sdl_window = sdl2.ext.Window(title, size=(width, height))

        self.sdl_window.show()

        # fill the background black
        sdl2.ext.fill(self.sdl_window.get_surface(), sdl2.ext.Color(0, 0, 0))

        # renderer must be made using the window surface, not the window itself
        self.renderer = sdl2.ext.renderer.Renderer(self.sdl_window.get_surface())

    def refresh(self):
        self.sdl_window.refresh()
