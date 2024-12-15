from .config.attributes import *
from tkinter import Frame, Label, Button, Entry

# -----------------------------------------------------
#
# The entrance to the application
#
# -----------------------------------------------------

class LoginFrame(Frame):
    def __init__(self, parent, auth, switch_to_dashboard):
        super().__init__(parent, bg=LOGIN_FRAME_BACKGROUND)
        self.auth = auth
        self.switch_to_dashboard = switch_to_dashboard

        # Introduction label
        self.label = Label(self, text=LOGIN_LABEL, font=LOGIN_LABEL_FONT)
        self.label.pack(pady=LOGIN_LABEL_PADY)

        # Status box
        self.status_message = Label(self, text="", fg=LOGIN_STATUS_FG, font=LOGIN_STATUS_FONT)

        # ID Entry and Label
        self.id_label = Label(self, text=LOGIN_ID_LABEL, font=LOGIN_ID_LABEL_FONT)
        self.id_label.pack(pady=LOGIN_ID_LABEL_PADY)

        self.id_entry = Entry(self, font=LOGIN_ID_ENTRY_FONT)
        self.id_entry.pack(pady=LOGIN_ID_ENTRY_PADY)

        # Login button
        self.login_button = Button(self, text=LOGIN_BUTTON_TEXT, font=LOGIN_BUTTON_FONT, command=self.login)
        self.login_button.pack(pady=LOGIN_BUTTON_PADY)

    def login(self):
        user_id = self.id_entry.get()
        result = self.auth.login(user_id)
        number_attempts = self.auth.number_attempts

        self.reset_status_message()

        if result == 1:
            self.id_entry.delete(0, 'end')
            self.auth.reset_attempts()
            self.switch_to_dashboard()

        elif result == 0:
            if not user_id:
                self.status_message.config(
                    text=f"Please enter an id. {number_attempts} more attempts left", 
                    fg=LOGIN_STATUS_FG,
                    bg="grey",
                )
            else:
                self.id_entry.delete(0, 'end')
                self.status_message.config(
                    text=f"ID is incorrect. {number_attempts} more attempts left", 
                    fg=LOGIN_STATUS_FG,
                    bg=LOGIN_STATUS_FAILED,
                )
        elif result == -1:
            self.status_message.config(
                text="You have run out of attempts, please contact the admin", 
                fg=LOGIN_STATUS_FG,
                bg=LOGIN_STATUS_FAILED,
            )
            self.label.pack_forget()
            self.id_label.pack_forget()
            self.id_entry.pack_forget()
            self.login_button.pack_forget()
        self.status_message.pack(pady=LOGIN_STATUS_PADY)

    def reset_status_message(self):
        self.status_message.config(text="", bg=None, fg=None)
        self.status_message.pack_forget()