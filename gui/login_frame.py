import customtkinter as ctk
from PIL import Image, ImageOps, ImageDraw

# -----------------------------------------------------
#
# The entrance to the application
#
# -----------------------------------------------------

class LoginFrame(ctk.CTkFrame):

    FORM_ENTRY_WIDTH = 180
    FORM_ENTRY_HEIGHT = 30

    def __init__(self, parent, auth, switch_to_dashboard):
        super().__init__(parent, fg_color="#0D1117")
        self.auth = auth
        self.switch_to_dashboard = switch_to_dashboard

        self.center = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )
        self.center.pack(expand=True, padx=20, pady=(0,20))
        
        self.status_box = ctk.CTkFrame(
            self.center,
            fg_color="#25171C",
            border_color="#792E2E",
            border_width=1,
        )

        self.status_message = ctk.CTkLabel(
            self.status_box,
            text_color="white",
        )

        self.logo = ctk.CTkButton(
            self.center,
            image=ctk.CTkImage(
                light_image=self.make_image_circular("gui/images/github-icon.ico"),
                size=(100, 100)
            ),
            text="",
            fg_color="transparent",
            hover="#0D1117",
        )
        self.logo.pack(pady=(0,30))

        self.title_label = ctk.CTkLabel(
            self.center,
            text="Student Management System",
            font=("Helvetica", 20),
            text_color="white")
        self.title_label.pack()

        '''

        Form in the center of the login frame

        '''

        self.form_frame = ctk.CTkFrame(
            self.center, 
            fg_color="#151B23",
            border_color="#313840",
            border_width=1,
        )
        self.form_frame.pack(padx=20, pady=20)

        self.id_label = ctk.CTkLabel(self.form_frame, text="Student ID", font=("Helvetica", 14), text_color="white")
        self.id_label.grid(row=2, column=0, columnspan=1, pady=(20, 7))

        # ID Entry Field with centered text and light background
        self.id_entry = ctk.CTkEntry(
            self.form_frame, 
            font=("Helvetica", 14), 
            justify="left", 
            fg_color="#0D1117",
            border_color="#3c4147",
            border_width=1,
            width=LoginFrame.FORM_ENTRY_WIDTH,
            height=LoginFrame.FORM_ENTRY_HEIGHT,
            text_color="white",
        )

        self.id_entry.grid(row=3, column=0, columnspan=4, padx=20, pady=(0, 10))

        # Login button
        self.login_button = ctk.CTkButton(
            self.form_frame, 
            text="Sign in", 
            font=("Helvetica", 14), 
            fg_color="#238636",
            border_color="#39924A",
            border_width=1,
            hover_color="#1f7530",
            width=LoginFrame.FORM_ENTRY_WIDTH, 
            text_color="white", 
            command=self.login
        )
        self.login_button.grid(row=4, column=0, columnspan=4, padx=20, pady=(10, 20))

    def login(self):
        user_id = self.id_entry.get()
        result = self.auth.login(user_id)
        #result = self.auth.login("root")
        self.reset_status_message()

        if result == 1:
            self.id_entry.delete(0, 'end')
            self.auth.reset_attempts()
            self.switch_to_dashboard()
        elif result == 0:
            if not user_id:
                self.status_message.configure(
                    text=f"Fill in the form.",
                )
            else:
                self.id_entry.delete(0, 'end')
                self.status_message.configure(
                    text=f"Incorrect ID.", 
                )
        elif result == -1:
            self.status_message.configure(
                text="You have run out of attempts. Please contact the admin.", 
            )
            self.title_label.grid_forget()
            self.id_label.grid_forget()
            self.id_entry.grid_forget()
            self.login_button.grid_forget()

        if self.status_message.cget("text"):
            self.status_box.pack()
            self.status_message.pack(expand=True, padx=25, pady=5)

    def reset_status_message(self):
        self.status_message.configure(text="")
        self.status_message.pack_forget()
        self.status_box.pack_forget()

    def make_image_circular(self, image_path: str):
        '''
        From stack overflow
        https://stackoverflow.com/questions/890051/how-do-i-generate-circular-thumbnails-with-pil

        Thanks to DRC!
        '''
        mask = Image.new('L', (1000,1000), 0)
        draw = ImageDraw.Draw(mask) 
        draw.ellipse((0, 0) + (1000,1000), fill=255)

        im = Image.open(image_path)

        output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
        output.putalpha(mask)

        return output