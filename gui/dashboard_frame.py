from tkinter import Frame, Button, Label

from functools import partial
from .config.color import *

from .contents.profile_frame import ProfileFrame
from .contents.register_student_frame import RegisterStudentFrame
from .contents.view_all_students_frame import ViewAllStudentsFrame

class DashboardFrame(Frame):
    def __init__(self, parent, auth, student_controller, frame_manager):
        super().__init__(parent, bg="lightgrey")
        self.student_controller = student_controller
        self.user = auth.user
        self.frame_manager = frame_manager

        content_frames = [ProfileFrame(self, self.user), 
                          SearchStudentFrame(self, self.student_controller), 
                          ViewAllStudentsFrame(self, self.student_controller), 
                          RegisterStudentFrame(self, self.student_controller)]
        self.nav_frame = Frame(self, bg="grey", width=200)
        self.nav_frame.pack(side="left", fill="y")

        self.content_frame = Frame(self, bg="white")
        self.content_frame.pack(side="right", fill="both", expand=True)
        
        self.btn_txt = ["View Profile", "Search Student", "View All Student", "Register Student", "Logout"]
        for i, text in enumerate(self.btn_txt[:-1]):
            Button(self.nav_frame, text=text, font=("Arial", 14), bg="skyblue", 
                   command=partial(self.switch_frame, content_frames[i], *content_frames)).pack(pady=5, padx=10)
        
        # Logout Button
        Button(self.nav_frame, text="Logout", font=("Arial", 14), bg="red", command=parent.quit).pack(pady=5, padx=10)

    def switch_frame(self, frame_to_show, *frames_to_hide):
        """Switch between content frames when a navigation button is clicked."""
        for frame in frames_to_hide:
            frame.pack_forget()
        frame_to_show.pack(fill="both", expand=True)


class SearchStudentFrame(Frame):
    def __init__(self, parent, student_controller):
        super().__init__(parent, bg="white")
        self.student_controller = student_controller
        Label(self, text="Search for a student", font=("Arial", 16)).pack(pady=20)