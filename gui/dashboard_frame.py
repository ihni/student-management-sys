from functools import partial

from tkinter import Frame, Button
from .contents.profile_frame import ProfileFrame
from .contents.register_student_frame import RegisterStudentFrame
from .contents.view_all_students_frame import ViewAllStudentsFrame
from .contents.search_student_frame import SearchStudentFrame

class DashboardFrame(Frame):
    def __init__(self, parent, auth, student_controller, frame_manager):
        super().__init__(parent, bg="lightgrey")
        self.student_controller = student_controller
        self.auth = auth
        self.user = auth.user
        self.frame_manager = frame_manager

        # Initialize content frames
        profile = ProfileFrame(self, self.user)
        search = SearchStudentFrame(self, self.student_controller)
        view_all = ViewAllStudentsFrame(self, self.student_controller)
        register = RegisterStudentFrame(self, self.student_controller, view_all)

        content_frames = [
            profile,
            search,
            view_all,
            register
        ]

        # Create navbar frame
        self.nav_frame = Frame(self, bg="grey", width=200)
        self.nav_frame.pack(side="left", fill="y")

        # Create content display frame
        self.content_frame = Frame(self, bg="white")
        self.content_frame.pack(side="right", fill="both", expand=True)

        # Navigation buttons
        self.btn_txt = ["View Profile", "Search Student", "View All Student", "Register Student", "Logout"]
        for i, text in enumerate(self.btn_txt[:-1]):
            Button(self.nav_frame, text=text, font=("Arial", 14), bg="skyblue", 
                   command=partial(self.switch_frame, content_frames[i], *content_frames)).pack(pady=5, padx=10)

        # Logout button
        Button(self.nav_frame, text="Logout", font=("Arial", 14), bg="red", 
               command=self.logout).pack(pady=5, padx=10)

    def switch_frame(self, frame_to_show, *frames_to_hide):
        for frame in frames_to_hide:
            frame.pack_forget()
        frame_to_show.pack(fill="both", expand=True)

    def logout(self):
        self.auth.logout()
        self.user = None
        self.pack_forget()
        self.frame_manager.switch_to('login')