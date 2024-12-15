from .config.attributes import *
from tkinter import Frame, Label, Button, Entry

# -----------------------------------------------------
#
# The entrance to the application
#
# -----------------------------------------------------

class LoginFrame(Frame):
    def __init__(self, parent, auth, switch_to_dashboard):
        super().__init__(parent, bg="#ededed")
        self.auth = auth
        self.switch_to_dashboard = switch_to_dashboard
        
        '''

        Form in the center of the login frame

        '''
        self.form_frame = Frame(self, bg="white", padx=40, pady=40)
        self.form_frame.pack(expand=True)

        self.title_label = Label(self.form_frame, text="Student Login", font=("Helvetica", 24, "bold"), bg="white", fg="#2c3e50")
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(20, 5))

        self.id_label = Label(self.form_frame, text="Enter your Student ID", font=("Helvetica", 12), bg="white", fg="#2c3e50")
        self.id_label.grid(row=1, column=0, columnspan=2, pady=(5, 5))

        # ID Entry Field with centered text and light background
        self.id_entry = Entry(self.form_frame, font=("Helvetica", 14), bd=2, relief="solid", fg="#2c3e50", bg="white", justify="center")
        self.id_entry.grid(row=2, column=0, columnspan=2, pady=(5, 10))  # Grid with some padding

        # Status message (hidden until needed)
        self.status_message = Label(self.form_frame, text="", font=("Helvetica", 10), fg="red", bg="white")
        self.status_message.grid(row=3, column=0, columnspan=2, pady=(5, 15))  # Grid with some padding below entry

        # Login button
        self.login_button = Button(self.form_frame, text="Login", font=("Helvetica", 14, "bold"), bg="#4CAF50", fg="white", bd=0, relief="flat", width=20, command=self.login)
        self.login_button.grid(row=4, column=0, columnspan=2, pady=(10, 20))  # Grid with padding below status message

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
                    text=f"Please enter an ID. {number_attempts} more attempts left",
                    fg="red"
                )
            else:
                self.id_entry.delete(0, 'end')
                self.status_message.config(
                    text=f"ID is incorrect. {number_attempts} more attempts left", 
                    fg="red"
                )
        elif result == -1:
            self.status_message.config(
                text="You have run out of attempts. Please contact the admin.", 
                fg="red"
            )
            self.title_label.grid_forget()
            self.id_label.grid_forget()
            self.id_entry.grid_forget()
            self.login_button.grid_forget()

        if self.status_message.cget("text"):
            self.status_message.grid(row=3, column=0, columnspan=2, pady=(5, 15))

    def reset_status_message(self):
        self.status_message.config(text="")
        self.status_message.grid_forget()
