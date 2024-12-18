from functools import partial
import customtkinter as ctk
from PIL import Image

from .contents.profile_frame import ProfileFrame
from .contents.register_student_frame import RegisterStudentFrame
from .contents.view_all_students_frame import ViewAllStudentsFrame
from .contents.search_student_frame import SearchStudentFrame

# -----------------------------------------------------
#
# Dashboard Frame for navbar and content frames
#
# -----------------------------------------------------

class DashboardFrame(ctk.CTkFrame):
    def __init__(self, parent, auth, student_controller, frame_manager):
        super().__init__(parent, fg_color="#010409")
        self.student_controller = student_controller
        self.auth = auth
        self.user = auth.user
        self.frame_manager = frame_manager

        # content frames
        self.content_frame = ctk.CTkFrame(self, fg_color="#010409")
        self.content_frame.pack(side="right", fill="both", expand=True)

        self.profile = ProfileFrame(self.content_frame, self.user)
        self.search = SearchStudentFrame(self.content_frame, self.student_controller)
        self.view_all = ViewAllStudentsFrame(self.content_frame, self.student_controller)
        self.register = RegisterStudentFrame(self.content_frame, self.student_controller, self.view_all)

        self.content_frames = [self.profile, self.search, self.view_all, self.register]

        # navbar frame
        self.nav_frame = ctk.CTkFrame(self, fg_color="#0D1117")
        self.nav_frame.pack(side="left", fill="y")

        self.nav_label = ctk.CTkLabel(self.nav_frame, text="Dashboard", fg_color="#0D1117", font=("Helvetica", 18, "bold"))
        self.nav_label.pack(fill="x", pady=(40,0))

        self.nav_button_container = ctk.CTkFrame(self.nav_frame, fg_color="#0D1117")
        self.nav_button_container.pack(expand=True, fill="both", padx=(30, 80), pady=(100,20))

        # nav button styles
        button_style = {
            "font": ("Helvetica", 14),
            "fg_color": "#0D1117",
            "text_color": "white",
            "hover_color": "#1A1F25",
            "width": 230,
            "corner_radius": 30,
            "height": 2,
            "anchor": "w",
        }

        self.buttons = []
        #user_name = '-'.join(self.user.name.strip().lower().split())
        btn_txt = [f"View profile", f"Search student", f"View all students", f"Register student", "Sign out"]
        btn_icons = [
            ctk.CTkImage(light_image=Image.open("gui/images/icons/profile-icon.png"),size=(20, 20)),
            ctk.CTkImage(light_image=Image.open("gui/images/icons/search-icon.png"),size=(20, 20)),
            ctk.CTkImage(light_image=Image.open("gui/images/icons/users-icon.png"),size=(20, 20)),
            ctk.CTkImage(light_image=Image.open("gui/images/icons/register-icon.png"),size=(20, 20)),
            ctk.CTkImage(light_image=Image.open("gui/images/icons/logout-icon.png"),size=(20, 20)),
        ]
        for i, text in enumerate(btn_txt[:-1]):
            button = ctk.CTkButton(
                self.nav_button_container,
                image=btn_icons[i],
                text=text,
                **button_style,
                command=partial(self.switch_frame, self.content_frames[i], *self.content_frames)
            )
            button.pack(fill="x", padx=(2,10), pady=10, anchor="w")
            self.buttons.append(button)

        logout_style = button_style.copy()
        logout_style.update({
            "font": ("Helvetica", 14),
            "text_color": "white",
            "fg_color": "#0D1117",
            "hover_color": "#1A1F25",
            "image": btn_icons[-1],
            "width": button_style["width"],
            "height": button_style["height"],
            "anchor": "w",
        })

        ctk.CTkButton(
            self.nav_button_container,
            text=btn_txt[-1],
            **logout_style,
            command=self.logout
        ).pack(fill="x", padx=(2,10), pady=(0, 40), side="bottom", anchor="w")

        #highlighting view profile since view profile was made to be the first frame shown
        self.highlight_button(self.buttons[0])
        self.switch_frame(self.profile, *self.content_frames)

    def switch_frame(self, frame_to_show, *frames_to_hide):
        for frame in frames_to_hide:
            frame.pack_forget()
        frame_to_show.pack(side="right", fill="both", expand=True, padx=20, pady=20)
        self.highlight_button(self.buttons[self.content_frames.index(frame_to_show)])

    def highlight_button(self, selected_button):
        for button in self.buttons:
            button.configure(fg_color="#0D1117", text_color="white", hover_color="#1A1F25")
        selected_button.configure(fg_color="#232a32", text_color="white", hover_color="#232a32")

    def logout(self):
        self.auth.logout()
        self.user = None
        self.frame_manager.switch_to('login')
