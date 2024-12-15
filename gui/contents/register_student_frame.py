from tkinter import Frame, Label, StringVar, Button, Entry, messagebox
import re

# -----------------------------------------------------
#
# Registration Frame for adding students to the system
#
# -----------------------------------------------------

class RegisterStudentFrame(Frame):
    def __init__(self, parent, student_controller, view_all):
        super().__init__(parent, bg="white")
        self.student_controller = student_controller
        self.view_all = view_all

        Label(self, text="Register a Student", font=("Arial", 18, "bold"), bg="white").pack(pady=20)

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
                self.fields[field]["error"].config(text=f"{field} cannot be empty.")
                error_found = True
            elif field == "Age" and not value.isdigit():
                self.fields["Age"]["error"].config(text="Age must be a number.")
                error_found = True
            elif field == "Student ID" and self.student_controller.fetch_student_by_id(value):
                self.fields[field]["error"].config(text=f"Student ID {value} is already taken.")
                error_found = True
            elif field == "Email" and not self.is_valid_email(value):
                self.fields["Email"]["error"].config(text="Please enter a valid email address.")
                error_found = True
            elif field == "Phone" and not value.isdigit():
                self.fields["Phone"]["error"].config(text="Phone number should only contain digits.")
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
            messagebox.showinfo("Success", "Student added successfully!")

        self.view_all.update_view()
        self.clear_form()

    def clear_error_messages(self):
        for field in self.fields.values():
            field["error"].config(text="")

    def clear_form(self):
        for field in self.fields.values():
            field["var"].set("")

    def is_valid_email(self, email):
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return bool(re.match(email_regex, email))