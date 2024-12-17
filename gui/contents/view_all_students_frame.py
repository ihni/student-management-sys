from CTkTable import *
import customtkinter as ctk

# -----------------------------------------------------
#
# View All Students Frame displaying a table for all users in the system
#
# -----------------------------------------------------

class ViewAllStudentsFrame(ctk.CTkFrame):
    def __init__(self, parent, student_controller):
        self.student_controller = student_controller
        super().__init__(parent, fg_color="#010409")

        # Title
        self.header = ctk.CTkLabel(
            self, 
            text=f"Students: {len(self.student_controller.fetch_all_students())}", 
            font=("Helvetica", 18),
            fg_color="#010409",
        )

        self.header.pack(pady=20, anchor="w")

        self.table_frame = ctk.CTkScrollableFrame(self, bg_color="#010409", fg_color="#010409")

        self.update_view()

        self.table_frame.pack(expand=True, fill="both")

    def update_view(self):
        for widget in self.table_frame.winfo_children():
            widget.destroy()

        self.header.configure(text=f"Students: {len(self.student_controller.fetch_all_students())}")
        
        # Fetch all students
        students = self.student_controller.fetch_all_students()

        # Define headers
        data_table = []
        headers = ["ID", "Name", "Age", "Email", "Phone"]
        data_table.append(headers)

        for student in students:
            id, name, age, email, phone = student.get_data()
            row = [id, name, age, email, phone]
            data_table.append(row)
        
        self.table = CTkTable(
            self.table_frame, 
            row=len(data_table),
            column=len(data_table[1]), 
            values=data_table,
            bg_color="#010409",
        )

        self.table.pack(expand=True, fill="both", padx=20, pady=20)