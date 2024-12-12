from tkinter import *
from .login_view import LoginView
from .dashboard_view import DashboardView
from .add_student_view import AddStudentView

class GUI:
    def __init__(self, auth, student_controller):
        self.auth = auth
        self.student_controller = student_controller
        self.root = self.configure_root()
        self.views = {
            'login' : None,
            'dashboard' : None,
        }

    def configure_root(self):
        root_window = Tk()
        screen_width = root_window.winfo_screenwidth()
        screen_height = root_window.winfo_screenheight()
        # App title
        APP_TITLE = "Student Management System"

        # Scaling factor
        SCALING = 2

        # height and width of app
        APP_WIDTH = screen_width//SCALING
        APP_HEIGHT = screen_height//SCALING

        # Position of app to the center of screen
        X_POS = (screen_width//SCALING) - (APP_WIDTH//2)
        Y_POS = (screen_height//SCALING) - (APP_HEIGHT//2)

        APP_RESOLUTION = f"{APP_WIDTH}x{APP_HEIGHT}+{X_POS}+{Y_POS}"

        root_window.geometry(APP_RESOLUTION)
        root_window.title(APP_TITLE)
        return root_window
    
    def switch_view(self, view_name):
        for view in self.views.values():
            view.pack_forget()
        view = self.views[view_name]
        if view:
            view.pack()
    
    def create_views(self):
        self.views['login'] = LoginView(self, self.auth, self.student_controller)
        self.views['dashboard'] = DashboardView(self, self.auth, self.student_controller)

    def run(self):
        self.create_views()
        self.switch_view('login')
        self.root.mainloop()