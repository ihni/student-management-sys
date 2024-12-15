from tkinter import Tk
from .config.attributes import *
from .utils import FrameManager

from .login_frame import LoginFrame
from .dashboard_frame import DashboardFrame

class RootWindow:
    def __init__(self, auth, student_controller):
        print("Creating root window")
        self.auth = auth
        self.student_controller = student_controller
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
        root_geometry = f"{int(root_width)}x{int(root_height)}+{int(root_center_x)}+{int(root_center_y)}"
        self.root.geometry(root_geometry)

    def init_frames(self):
        self.login_frame = LoginFrame(self.root, self.auth, self.switch_to_dashboard)
        self.frame_manager.add_frame("login", self.login_frame)

        self.frame_manager.switch_to('login')
    
    def switch_to_login(self):
        self.frame_manager.switch_to("login")

    def switch_to_dashboard(self):
        '''
        This is a helper function to delay the creation of the dashboard so that when the user logs in, their info is saved
        This is then passed onto the auth which is stored in the dashboard to be used to view their own info
            - Without it, there would be no user saved if it was created side by side with the login frame.
        '''
        if self.frame_manager.frames.get('dashboard'):
            self.frame_manager.switch_to("dashboard")
        else:
            self.dashboard_frame = DashboardFrame(self.root, self.auth, self.student_controller, self.frame_manager)
            self.frame_manager.add_frame("dashboard", self.dashboard_frame)
            self.frame_manager.switch_to("dashboard")