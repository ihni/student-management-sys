from tkinter import StringVar

import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import re

# -----------------------------------------------------
#
# Registration Frame for adding students to the system
#
# -----------------------------------------------------

class RegisterStudentFrame(ctk.CTkFrame):
    def __init__(self, parent, student_controller, view_all):
        super().__init__(parent, bg_color="#010409", fg_color="#010409",)
        self.student_controller = student_controller
        self.view_all = view_all


        self.center = ctk.CTkFrame(self, fg_color="#010409", bg_color="#010409")
        self.center.pack(expand=True, padx=20, pady=20)
        
        ctk.CTkLabel(
            self.center,
            text="Register a Student",
            font=("Helvetica", 18, "bold"),
            bg_color="#010409",
            fg_color="#010409"
        ).pack(pady=20)

        self.form_container = ctk.CTkFrame(
            self.center,
            fg_color="#151B23",
            border_color="#313840",
            border_width=1,
        )
        self.form_container.pack()

        self.form_frame = ctk.CTkFrame(
            self.form_container,
            fg_color="transparent",
            bg_color="transparent"
        )
        self.form_frame.pack(padx=20, pady=(15,5))

        self.fields = {
            "Name"       : {"var": StringVar(), "error": ctk.CTkLabel(self.form_frame, text="", font=("Helvetica", 12), text_color="#e84343")},
            "Age"        : {"var": StringVar(), "error": ctk.CTkLabel(self.form_frame, text="", font=("Helvetica", 12), text_color="#e84343")},
            "Student ID" : {"var": StringVar(), "error": ctk.CTkLabel(self.form_frame, text="", font=("Helvetica", 12), text_color="#e84343")},
            "Email"      : {"var": StringVar(), "error": ctk.CTkLabel(self.form_frame, text="", font=("Helvetica", 12), text_color="#e84343")},
            "Phone"      : {"var": StringVar(), "error": ctk.CTkLabel(self.form_frame, text="", font=("Helvetica", 12), text_color="#e84343")},
        }

        for label, field in self.fields.items():
            self.create_input_field(label, field["var"], field["error"])

        register_button = ctk.CTkButton(
            self.form_frame,
            text="Register",
            font=("Helvetica", 14),
            fg_color="#238636",
            border_color="#39924A",
            border_width=1,
            hover_color="#1f7530",
            text_color="white",
            command=self.register_user
        )
        register_button.pack(padx=100, pady=(5, 20))

    def create_input_field(self, label, variable, error_label):
        label_widget = ctk.CTkLabel(self.form_frame, text=label, font=("Helvetica", 14))
        label_widget.pack(anchor="w", padx=20)

        entry = ctk.CTkEntry(
            self.form_frame, 
            textvariable=variable,
            font=("Helvetica", 14),
            width=30,
            border_width=1,
            fg_color="#0D1117",
        )

        entry.pack(pady=5, padx=20, fill="x")

        error_label.pack(anchor="w", padx=20)

    def register_user(self):
        self.clear_error_messages()

        error_found = False
        form_data = {
            "Name"       : self.fields["Name"]["var"].get().strip(),
            "Age"        : self.fields["Age"]["var"].get().strip(),
            "Student ID" : self.fields["Student ID"]["var"].get().strip(),
            "Email"      : self.fields["Email"]["var"].get().strip(),
            "Phone"      : self.fields["Phone"]["var"].get().strip()
        }

        for field, value in form_data.items():
            if not value:
                self.fields[field]["error"].configure(text=f"{field} cannot be empty.")
                error_found = True
            elif field == "Name" and not value.replace(" ", "").isalpha():
                self.fields[field]["error"].configure(text="Name must only contain letters.")
                error_found = True
            elif field == "Age" and not value.isdigit():
                self.fields[field]["error"].configure(text="Age must be a number.")
                error_found = True
            elif field == "Student ID" and self.student_controller.fetch_student_by_id(value):
                self.fields[field]["error"].configure(text=f"Student ID {value} is already taken.")
                error_found = True
            elif field == "Email" and not self.is_valid_email(value):
                self.fields["Email"]["error"].configure(text="Please enter a valid email address.")
                error_found = True
            elif field == "Phone" and not value.isdigit():
                self.fields[field]["error"].configure(text="Phone number should only contain digits.")
                error_found = True

        if error_found:
            return

        result = self.student_controller.add_student(
            name  = form_data["Name"], 
            age   = form_data["Age"], 
            id    = form_data["Student ID"], 
            email = form_data["Email"], 
            phone = form_data["Phone"])

        if isinstance(result, object):
            CTkMessagebox(
                message="The student was successfully registered.",
                icon="check", 
                option_1="Continue",
                title="Success!",
            )

        self.view_all.update_view()
        self.clear_form()

    def clear_error_messages(self):
        for field in self.fields.values():
            field["error"].configure(text="")

    def clear_form(self):
        for field in self.fields.values():
            field["var"].set("")

    def is_valid_email(self, email):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return bool(re.match(email_regex, email))