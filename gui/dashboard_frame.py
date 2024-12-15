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
        self.user = auth.user  # Updated dynamically on user login
        self.frame_manager = frame_manager

        # Initialize navigation and content frames
        self.nav_frame = Frame(self, bg="grey", width=200)
        self.nav_frame.pack(side="left", fill="y")

        self.content_frame = Frame(self, bg="white")  # Ensure this is defined before using
        self.content_frame.pack(side="right", fill="both", expand=True)

        # Initialize content frames
        self.content_frames = {}
        self.active_frame = None
        self.initialize_content_frames()

        # Create navigation buttons
        self.btn_txt = ["View Profile", "Search Student", "View All Student", "Register Student", "Logout"]
        for i, text in enumerate(self.btn_txt[:-1]):
            Button(self.nav_frame, text=text, font=("Arial", 14), bg="skyblue", 
                   command=partial(self.switch_frame, list(self.content_frames.values())[i])).pack(pady=5, padx=10)

        Button(self.nav_frame, text="Logout", font=("Arial", 14), bg="red", 
               command=self.logout).pack(pady=5, padx=10)

    def initialize_content_frames(self):
        """Initialize content frames."""
        self.content_frames = {
            "profile": ProfileFrame(self.content_frame, self.user),
            "search": SearchStudentFrame(self.content_frame, self.student_controller),
            "view_all": ViewAllStudentsFrame(self.content_frame, self.student_controller),
            "register": RegisterStudentFrame(self.content_frame, self.student_controller, None),
        }

        # Pack all frames but hide them initially
        for frame in self.content_frames.values():
            frame.pack(fill="both", expand=True)
            frame.pack_forget()

    def switch_frame(self, frame_to_show):
        """Switch to the given content frame."""
        # Hide the currently active frame
        if self.active_frame:
            self.active_frame.pack_forget()

        # Show the new frame and set it as active
        frame_to_show.pack(fill="both", expand=True)
        self.active_frame = frame_to_show

    def logout(self):
        """Handle logout functionality."""
        self.auth.logout()  # Clears user session
        self.user = None  # Reset the user
        self.pack_forget()  # Hide dashboard
        self.frame_manager.switch_to("login")  # Switch back to login frame

    def refresh_user(self):
        """Refresh the user-related frames after a new login."""
        self.user = self.auth.user
        self.content_frames["profile"] = ProfileFrame(self.content_frame, self.user)