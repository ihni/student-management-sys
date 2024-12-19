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

        self.header = ctk.CTkLabel(
            self, 
            text=f"Students: {len(self.student_controller.fetch_all_students())}", 
            font=("Helvetica", 18),
            fg_color="#010409",
        )
        self.header.pack(pady=20, anchor="w")

        self.table_frame = ctk.CTkScrollableFrame(self, bg_color="#010409", fg_color="#010409")
        self.table_frame.pack(expand=True, fill="both")
        self.update_view()

    def update_view(self):
        for widget in self.table_frame.winfo_children():
            widget.destroy()

        self.header.configure(text=f"Students: {len(self.student_controller.fetch_all_students())}")
        

        data_table = []
        headers = ["ID", "Name", "Age", "Email", "Phone"]
        data_table.append(headers)

        students = self.student_controller.fetch_all_students()
        for student in students:
            name, age, id, email, phone = student.get_data()
            row = [id, name, age, email, phone]
            data_table.append(row)
        
        CTkTable(
            self.table_frame, 
            row=len(data_table),
            column=len(headers), 
            values=data_table,
            bg_color="#010409",
            fg_color="#010409",
            header_color="#0a0c10",
            colors=["#0b0f14", "#151B23"],
            justify="left",
            orientation="horizontal",
            corner_radius=7,
        ).pack(expand=True, fill="both", padx=20, pady=20)