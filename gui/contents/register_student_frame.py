from ..config.color import *
from tkinter import Frame, Label, StringVar, Button, Entry, messagebox
import re
# -----------------------------------------------------
#
# Registration Frame for adding students to the system
#
# -----------------------------------------------------

class RegisterStudentFrame(Frame):
    def __init__(self, parent, student_controller):
        super().__init__(parent, bg="white")
        self.student_controller = student_controller

        print(f"{BRIGHT_CYAN}Initializing RegisterStudentFrame...{RESET}")

        Label(self, text="Register a Student", font=("Arial", 18, "bold"), bg="white").pack(pady=20)

        # Store all field configurations in a dictionary
        self.fields = {
            "Name"       : {"var": StringVar(), "error": Label(self, text="", font=("Arial", 12), fg="red", bg="white")},
            "Age"        : {"var": StringVar(), "error": Label(self, text="", font=("Arial", 12), fg="red", bg="white")},
            "Student ID" : {"var": StringVar(), "error": Label(self, text="", font=("Arial", 12), fg="red", bg="white")},
            "Email"      : {"var": StringVar(), "error": Label(self, text="", font=("Arial", 12), fg="red", bg="white")},
            "Phone"      : {"var": StringVar(), "error": Label(self, text="", font=("Arial", 12), fg="red", bg="white")},
        }

        for label, field in self.fields.items():
            self.create_input_field(label, field["var"], field["error"])

        register_button = Button(self, text="Register", font=("Arial", 14), command=self.register_user)
        register_button.pack(pady=20)

    def create_input_field(self, label, variable, error_label):
        label_widget = Label(self, text=label, font=("Arial", 14), bg="white")
        label_widget.pack(anchor="w", padx=20)

        entry = Entry(self, textvariable=variable, font=("Arial", 14), bg="#f0f0f0", width=30)
        entry.pack(pady=5, padx=20, fill="x")

        error_label.pack(anchor="w", padx=20)


    # Deals with the business logic of registering a student
    def register_user(self):
        print(f"{BRIGHT_BLUE}Registering user...{RESET}")

        self.clear_error_messages()

        error_found = False
        form_data = {
            "Name"       : self.fields["Name"]["var"].get().strip(),
            "Age"        : self.fields["Age"]["var"].get().strip(),
            "Student ID" : self.fields["Student ID"]["var"].get().strip(),
            "Email"      : self.fields["Email"]["var"].get().strip(),
            "Phone"      : self.fields["Phone"]["var"].get().strip()
        }

        # Validation logic
        for field, value in form_data.items():
            if not value:
                print(f"{BRIGHT_RED}Error: {field} cannot be empty.{RESET}")
                self.fields[field]["error"].config(text=f"{field} cannot be empty.")
                error_found = True
            elif field == "Student ID" and self.student_controller.fetch_student_by_id(value):
                print(f"{BRIGHT_RED}Error: Student ID {value} is already taken.{RESET}")
                self.fields[field]["error"].config(text=f"Student ID {value} is already taken.")
                error_found = True
            elif field == "Email" and not self.is_valid_email(value):
                print(f"{BRIGHT_RED}Error: Invalid email format.{RESET}")
                self.fields["Email"]["error"].config(text="Please enter a valid email address.")
                error_found = True
            elif field == "Phone" and not value.isdigit():
                print(f"{BRIGHT_RED}Error: Phone number should only contain digits.{RESET}")
                self.fields["Phone"]["error"].config(text="Phone number should only contain digits.")
                error_found = True

        if error_found:
            return

        print(f"{BRIGHT_GREEN}Registration data valid, proceeding to add student...{RESET}")
        result = self.student_controller.add_student(
            name  = form_data["Name"], 
            age   = form_data["Age"], 
            id    = form_data["Student ID"], 
            email = form_data["Email"], 
            phone = form_data["Phone"])

        if isinstance(result, object):
            print(f"{BRIGHT_YELLOW}Student added successfully!{RESET}")
            messagebox.showinfo("Success", "Student added successfully!")

        self.clear_form()

    def clear_error_messages(self):
        """Clear all error messages."""
        for field in self.fields.values():
            field["error"].config(text="")

    def clear_form(self):
        """Clear all input fields."""
        for field in self.fields.values():
            field["var"].set("")

    def is_valid_email(self, email):
        """Validate email format."""
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return bool(re.match(email_regex, email))