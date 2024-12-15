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
        title_label = Label(self, text="Search for a Student", font=("Arial", 24, "bold"), bg="white", fg="#2c3e50")
        title_label.pack(pady=30)

        # Student ID entry field
        self.id_entry = Entry(self, font=("Arial", 14), width=35, bd=0, relief="flat", 
                              bg="#d5d6d7", fg="#2c3e50", justify="center")
        self.id_entry.pack(pady=20)
        
        # Search button
        search_button = Button(self, text="Search", font=("Arial", 14, "bold"), command=self.search_student,
                               bg="#3498db", fg="white", relief="flat", width=20)
        search_button.pack(pady=20)

        # Profile Section for displaying student info (initially hidden)
        self.profile_section = Frame(self, bg="white", padx=30, pady=30, bd=0)
        self.profile_section.pack_forget()

        # Info label style
        info_label_style = ("Arial", 16)

        # Labels for displaying student info
        self.name_label = Label(self.profile_section, font=info_label_style, anchor="w", bg="white", fg="#34495e")
        self.name_label.pack(fill="x", pady=10)
        self.age_label = Label(self.profile_section, font=info_label_style, anchor="w", bg="white", fg="#34495e")
        self.age_label.pack(fill="x", pady=10)
        self.id_label = Label(self.profile_section, font=info_label_style, anchor="w", bg="white", fg="#34495e")
        self.id_label.pack(fill="x", pady=10)
        self.email_label = Label(self.profile_section, font=info_label_style, anchor="w", bg="white", fg="#34495e")
        self.email_label.pack(fill="x", pady=10)
        self.phone_label = Label(self.profile_section, font=info_label_style, anchor="w", bg="white", fg="#34495e")
        self.phone_label.pack(fill="x", pady=10)

        # Error box for when no student is found
        self.error_box = Frame(self, bg="white", padx=20, pady=20)
        self.error_label = Label(self.error_box, text="No student found.", font=("Arial", 16), anchor="w", 
                                 bg="white", fg="#e74c3c", wraplength=300, justify="left")
        self.error_label.pack(fill="x", pady=10)
        self.error_box.pack_forget()


        self.pack(fill="both", expand=True)

    def search_student(self):
        student_id = self.id_entry.get().strip()
        if not student_id:
            self.error_box.pack(fill="both", padx=30, pady=20)
            self.error_label.config(text=f"Please enter a student ID")
            return
        
        result = self.student_controller.fetch_student_by_id(student_id)

        # Reset profile and error sections
        self.name_label.config(text="")
        self.age_label.config(text="")
        self.id_label.config(text="")
        self.email_label.config(text="")
        self.phone_label.config(text="")
        self.profile_section.pack_forget()
        self.error_box.pack_forget()

        # Display result if found
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