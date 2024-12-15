from tkinter import Tk
from .config.attributes import *
from .utils import FrameManager

from .login_frame import LoginFrame

class RootWindow:
    def __init__(self):
        print("Creating root window")
        self.root = Tk()
        self.root.config(bg = ROOT_BACKGROUND)
        self.root.title(ROOT_TITLE)
        self.setup_geometry()
        
        self.frame_manager = FrameManager(self.root)

        self.init_frames()

    def setup_geometry(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        root_width = screen_width // ROOT_SCALE
        root_height = screen_height // ROOT_SCALE
        root_center_x = (screen_width - root_width) // 2
        root_center_y = (screen_height - root_height) // 2
        root_geometry = f"{root_width}x{root_height}+{root_center_x}+{root_center_y}"
        self.root.geometry(root_geometry)

    def init_frames(self):
        self.login_frame = LoginFrame(self.root)

        self.frame_manager.add_frame("login", self.login_frame)

        self.frame_manager.switch_to("login")