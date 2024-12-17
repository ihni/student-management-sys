import customtkinter as ctk
# -----------------------------------------------------
#
# Search Student Frame for fetching a student based on the ID
#
#   **TODO FIX UI**
# -----------------------------------------------------

class SearchStudentFrame(ctk.CTkFrame):
    def __init__(self, parent, student_controller):
        super().__init__(parent, bg_color="#010409", fg_color="#010409")
        self.student_controller = student_controller

        # Title label
        title_label = ctk.CTkLabel(self, text="Search for a Student", font=("Helvetica", 18, "bold"), fg_color="#010409", text_color="white")
        title_label.pack(pady=15)

        self.center = ctk.CTkFrame(self, fg_color="transparent")
        self.center.pack(padx=20, pady=20, expand=True)


        self.search_bar_frame = ctk.CTkFrame(
            self.center,
            fg_color="#151B23",
            border_color="#313840",
            border_width=1,
        )
        self.search_bar_frame.pack(padx=(10,10))

        # Student ID entry field
        self.id_entry = ctk.CTkEntry(
            self.search_bar_frame, 
            font=("Helvetica", 14), 
            justify="center",
            width=180,
        )
        self.id_entry.pack(pady=20, padx=20)
        
        # Search button
        ctk.CTkButton(
            self.search_bar_frame, 
            text="Search", 
            font=("Helvetica", 14), 
            command=self.search_student,
            fg_color="#010409", 
            text_color="white", 
            width=20
        ).pack(pady=20)
        

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
        self.status_message.pack()


        self.profile_section = ctk.CTkFrame(self, fg_color="#010409")
        self.labels = {}

        self.info_keys = ["Name", "Age", "ID", "Email", "Phone"]
        for key in self.info_keys:
            label = ctk.CTkLabel(
                self.profile_section, font=("Helvetica", 14),
                anchor="w", fg_color="#010409", text_color="white")
            label.pack(fill="x", pady=10)
            self.labels[key] = label

    def search_student(self):
        student_id = self.id_entry.get().strip()

        # Reset previous status and profile
        self.status_box.pack_forget()
        self.profile_section.pack_forget()

        if not student_id:
            self.display_status("Please enter a student ID")
            return

        # Fetch student
        result = self.student_controller.fetch_student_by_id(student_id)

        if result:
            self.display_profile(result)
            self.status_box.pack_forget()
        else:
            self.display_status(f"No student found with ID: {student_id}")

    def display_status(self, message):
        self.status_message.configure(text=message)
        self.status_box.pack(fill="both", padx=30, pady=20)

    def display_profile(self, student):
        student_data = {
            "Name": student.name,
            "Age": student.age,
            "ID": student.id,
            "Email": student.email,
            "Phone": student.phone
        }
        for key, label in self.labels.items():
            label.configure(text=f"{key}: {student_data[key]}")

        self.profile_section.pack(fill="both", padx=30, pady=20)