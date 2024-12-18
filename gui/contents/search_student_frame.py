import customtkinter as ctk
from CTkTable import *
# -----------------------------------------------------
#
# Search Student Frame for fetching a student based on the ID
#
# -----------------------------------------------------

class SearchStudentFrame(ctk.CTkFrame):
    def __init__(self, parent, student_controller):
        super().__init__(parent, bg_color="#010409", fg_color="#010409")
        self.student_controller = student_controller

        # Title label
        title_label = ctk.CTkLabel(self, text="Search for a Student", font=("Helvetica", 18, "bold"), fg_color="#010409", text_color="white")
        title_label.pack(pady=15)

        self.center = ctk.CTkFrame(self, fg_color="transparent")
        self.center.pack(padx=20, pady=20, expand=True, fill="both")

        self.search_bar_section = ctk.CTkFrame(
            self.center,
            fg_color="#151B23",
            border_color="#313840",
            border_width=1,
        )
        self.search_bar_section.pack(padx=(10,10), expand=True, fill="x")

        # Student ID entry field
        self.id_entry = ctk.CTkEntry(
            self.search_bar_section, 
            font=("Helvetica", 14), 
            justify="center",
            placeholder_text="ID",
            width=400,
        )
        self.id_entry.pack(pady=(20,0), padx=20)

        self.error = ctk.CTkLabel(
            self.search_bar_section,
            text="",
            text_color="#e84343",
        )
        self.error.pack(pady=(5,5))
        
        # Search button
        ctk.CTkButton(
            self.search_bar_section, 
            text="Search", 
            font=("Helvetica", 14), 
            command=self.search_student,
            fg_color="#010409", 
            text_color="white", 
            width=20
        ).pack(pady=(0, 20))
        
        self.table_frame = ctk.CTkScrollableFrame(self, bg_color="#010409", fg_color="#010409")
        self.table_frame.pack(expand=True, fill="both")

    def search_student(self):
        for widget in self.table_frame.winfo_children():
            widget.destroy()

        self.error.configure(text="")
        student_id = self.id_entry.get().strip()

        if not student_id:
            self.error.configure(text="Please input an ID")
            return

        result = self.student_controller.fetch_student_by_id(student_id)

        if not result:
            self.error.configure(text="Student not found")
            return
        
        data_table = []
        headers = ["ID", "Name", "Age", "Email", "Phone"]
        data_table.append(headers)
        data_table.append(result.get_data())
        
        self.table = CTkTable(
            self.table_frame, 
            row=len(data_table),
            column=len(data_table[0]), 
            values=data_table,
            bg_color="#010409",
        )

        self.table.pack(expand=True, fill="both", padx=20, pady=20)