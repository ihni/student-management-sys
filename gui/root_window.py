from tkinter import Tk, PhotoImage
from .config.attributes import *
from .utils import FrameManager

from .login_frame import LoginFrame
from .dashboard_frame import DashboardFrame

import customtkinter as ctk

# -----------------------------------------------------
#
# Root Window with configuration settings
#
# -----------------------------------------------------

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class RootWindow:
    
    def __init__(self, auth, student_controller):
        self.auth = auth
        self.student_controller = student_controller
        self.root = ctk.CTk()

        self.root.title(ROOT_TITLE)
        #self.setup_geometry()

        #image = "gui/images/book.png"
        #self.root.iconbitmap(image)

        self.frame_manager = FrameManager(self.root)
        self.root.geometry(RootWindow.CenterWindowToDisplay(self.root, 1200, 700, self.root._get_window_scaling()))
        self.init_frames()
    
    @staticmethod
    def CenterWindowToDisplay(Screen: ctk.CTk, width: int, height: int, scale_factor: float = 1.0):
        """
        Centers the window to the main display/monitor
        
        Thanks to HyperNylium for the function!
        """
        screen_width = Screen.winfo_screenwidth()
        screen_height = Screen.winfo_screenheight()
        x = int(((screen_width/2) - (width/2)) * scale_factor)
        y = int(((screen_height/2) - (height/1.8)) * scale_factor)
        return f"{width}x{height}+{x}+{y}"

    def init_frames(self):
        self.login_frame = LoginFrame(self.root, self.auth, self.switch_to_dashboard)
        self.frame_manager.add_frame("login", self.login_frame)
        self.frame_manager.switch_to("login")

    def switch_to_login(self):
        if self.frame_manager.frames.get("dashboard"):
            self.frame_manager.remove_frame("dashboard")

        self.frame_manager.switch_to("login")

    def switch_to_dashboard(self):
        if self.frame_manager.frames.get("dashboard"):
            self.frame_manager.remove_frame("dashboard")

        self.dashboard_frame = DashboardFrame(self.root, self.auth, self.student_controller, self.frame_manager)
        self.frame_manager.add_frame("dashboard", self.dashboard_frame)
        self.frame_manager.switch_to("dashboard")