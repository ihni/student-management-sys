from functools import partial
from tkinter import Frame, Button

from .contents.profile_frame import ProfileFrame
from .contents.register_student_frame import RegisterStudentFrame
from .contents.view_all_students_frame import ViewAllStudentsFrame
from .contents.search_student_frame import SearchStudentFrame

# -----------------------------------------------------
#
# Dashboard Frame for navbar and content frames
#
# -----------------------------------------------------

class DashboardFrame(Frame):
    def __init__(self, parent, auth, student_controller, frame_manager):
        super().__init__(parent, bg="white")
        self.student_controller = student_controller
        self.auth = auth
        self.user = auth.user
        self.frame_manager = frame_manager

        # content frames
        self.profile = ProfileFrame(self, self.user)
        self.search = SearchStudentFrame(self, self.student_controller)
        self.view_all = ViewAllStudentsFrame(self, self.student_controller)
        self.register = RegisterStudentFrame(self, self.student_controller, self.view_all)

        self.content_frames = [self.profile, self.search, self.view_all, self.register]

        # navbar frame
        self.nav_frame = Frame(self, bg="#282828")
        self.nav_frame.pack(side="left", fill="y")

        # content display frame
        self.content_frame = Frame(self, bg="white")
        self.content_frame.pack(side="right", fill="both", expand=True)

        # button styles
        button_style = {
            "font": ("Arial", 12, "bold"),
            "bg": "#282828",
            "fg": "#737373",
            "activebackground": "#2e2e2e",
            "activeforeground": "white",
            "relief": "flat",
            "bd": 0,
            "width": 20,
            "height": 2,
            "anchor": "w",
        }

        # Create buttons and assign commands
        self.buttons = []
        self.btn_txt = ["View Profile", "Search Student", "View All Students", "Register Student", "Logout"]

        for i, text in enumerate(self.btn_txt[:-1]):
            button = Button(
                self.nav_frame,
                text=text,
                **button_style,
                command=partial(self.switch_frame, self.content_frames[i], *self.content_frames)
            )
            button.pack(pady=5, anchor="w")
            self.buttons.append(button)

        # Highlight the first button by default
        self.highlight_button(self.buttons[0])

        # Logout button
        logout_style = button_style.copy()
        logout_style.update({
            "fg": "white",
            "bg": "#E74C3C",
            "activebackground": "#e26c5f"
        })

        # Logout button
        Button(
            self.nav_frame,
            text="Logout",
            **logout_style,
            command=self.logout
        ).pack(pady=20, side="bottom", anchor="w")

        # View profile is the first frame when dashboard is created
        self.switch_frame(self.profile, *self.content_frames)

    def switch_frame(self, frame_to_show, *frames_to_hide):
        for frame in frames_to_hide:
            frame.pack_forget()

        frame_to_show.pack(fill="both", expand=True)
        self.highlight_button(self.buttons[self.content_frames.index(frame_to_show)])

    def highlight_button(self, selected_button):
        for button in self.buttons:
            button.config(bg="#282828", fg="#737373")
        selected_button.config(bg="#282828", fg="white")

    def logout(self):
        self.auth.logout()
        self.user = None
        self.pack_forget()
        self.frame_manager.switch_to('login')
