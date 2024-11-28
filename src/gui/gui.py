from tkinter import *
import config.app

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
            'add_student' : None,
        }

    def configure_root(self):
        root_window = Tk()
        root_window.geometry(config.app.APP_RESOLUTION)
        root_window.title(config.app.APP_TITLE)
        return root_window
    
    def switch_view(self, view_name):
        for view in self.views.values():
            view.pack_forget()
        view = self.views.get(view_name)
        if view:
            view.pack()
    
    def create_views(self):
        self.views['login'] = LoginView(self.root, self.auth, self.student_controller)
        self.views['dashboard'] = DashboardView(self.root, self.auth, self.student_controller)
        self.views['add_student'] = AddStudentView(self.root, self.auth, self.student_controller)

    def run(self):
        self.create_views()
        self.switch_view('login')
        self.root.mainloop()
