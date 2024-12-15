from tkinter import Label, Frame, Entry, Button

# -----------------------------------------------------
#
# Search Student Frame for fetching a student based on the ID
#
# -----------------------------------------------------

class SearchStudentFrame(Frame):
    def __init__(self, parent, student_controller):
        super().__init__(parent, bg="white")
        self.student_controller = student_controller

        # Title label
        Label(self, text="Search for a student", font=("Arial", 16)).pack(pady=20)

        # Student ID entry field
        self.id_entry = Entry(self, font=("Arial", 12), width=30)
        self.id_entry.pack(pady=10)

        # Search button
        search_button = Button(self, text="Search", font=("Arial", 12), command=self.search_student)
        search_button.pack(pady=10)

        # Profile Section for displaying student info (initially hidden)
        self.profile_section = Frame(self, bg="lightgray", padx=20, pady=20)
        # Initially not displayed
        self.profile_section.pack_forget()  

        # Info label style
        info_label_style = ("Arial", 14)

        # Labels for displaying student info
        self.name_label = Label(self.profile_section, font=info_label_style, anchor="w", bg="lightgray")
        self.name_label.pack(fill="x", pady=5)
        self.age_label = Label(self.profile_section, font=info_label_style, anchor="w", bg="lightgray")
        self.age_label.pack(fill="x", pady=5)
        self.id_label = Label(self.profile_section, font=info_label_style, anchor="w", bg="lightgray")
        self.id_label.pack(fill="x", pady=5)
        self.email_label = Label(self.profile_section, font=info_label_style, anchor="w", bg="lightgray")
        self.email_label.pack(fill="x", pady=5)
        self.phone_label = Label(self.profile_section, font=info_label_style, anchor="w", bg="lightgray")
        self.phone_label.pack(fill="x", pady=5)

        self.error_box = Frame(self, bg="lightgray", padx=20, pady=20)
        self.error_label = Label(
            self.error_box, 
            text="No student found.", 
            font=("Arial", 14), 
            anchor="w", 
            bg="lightgray",
            wraplength=300,
            justify="left"
        )
        self.error_label.pack(fill="x", pady=5)
        self.error_box.pack_forget()

    def search_student(self):
        student_id = self.id_entry.get()

        result = self.student_controller.fetch_student_by_id(student_id)

        self.name_label.config(text="")
        self.age_label.config(text="")
        self.id_label.config(text="")
        self.email_label.config(text="")
        self.phone_label.config(text="")
        self.profile_section.pack_forget()
        self.error_box.pack_forget()

        # Display result
        if result:
            id = result.id
            name = result.name
            age = result.age
            email = result.email
            phone = result.phone

            self.name_label.config(text=f"Name: {name}")
            self.age_label.config(text=f"Age: {age}")
            self.id_label.config(text=f"ID: {id}")
            self.email_label.config(text=f"Email: {email}")
            self.phone_label.config(text=f"Phone: {phone}")

            self.profile_section.pack(fill="both", padx=30, pady=20)
        else:
            self.error_box.pack(fill="both", padx=30, pady=20)
            self.error_label.config(text=f"No student found with ID: {student_id}")