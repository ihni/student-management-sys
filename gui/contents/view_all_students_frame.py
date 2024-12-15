from tkinter import Frame, Label

# -----------------------------------------------------
#
# View All Students Frame displaying a table for all users in the system
#
# -----------------------------------------------------

class ViewAllStudentsFrame(Frame):
    def __init__(self, parent, student_controller):
        self.student_controller = student_controller
        super().__init__(parent, bg="white")

        # Title
        self.header = Label(self, 
                            text=f"Students: {len(self.student_controller.fetch_all_students())}", 
                            font=("Segoe UI", 18, "bold"), 
                            bg="white", fg="black"
        )
        self.header.pack(pady=20)

        # Table container
        self.table_frame = Frame(self, bg="white")
        self.table_frame.pack(fill="both", expand=True, padx=20, pady=10)

        self.update_view()

    def update_view(self):
        # Clear any existing widgets in the table frame
        for widget in self.table_frame.winfo_children():
            widget.destroy()

        self.header.config(text=f"Students: {len(self.student_controller.fetch_all_students())}")
        
        # Fetch all students
        students = self.student_controller.fetch_all_students()

        # Define headers
        headers = ["ID", "Name", "Age", "Email", "Phone"]
        header_bg = "#3b3636"
        header_fg = "white"
        row_colors = ["#ededed", "#FFFFFF"]

        # Top border
        top_border = Frame(self.table_frame, bg="white", highlightbackground="#D5D8DC", highlightthickness=1)
        top_border.grid(row=0, column=0, columnspan=len(headers), sticky="ew", pady=(0, 10))

        # Add headers
        for col, header in enumerate(headers):
            Label(self.table_frame, text=header, font=("Segoe UI", 12, "bold"), bg=header_bg, fg=header_fg,
                  padx=10, pady=5, anchor="w").grid(row=1, column=col, sticky="nsew")

        # Add data rows
        for row, student in enumerate(students, start=2):
            bg_color = row_colors[row % 2]  # Alternate row colors
            data = [student.id, student.name, student.age, student.email, student.phone]
            for col, value in enumerate(data):
                Label(self.table_frame, text=value, font=("Segoe UI", 12), bg=bg_color, fg="#34495E",
                      padx=10, pady=5, anchor="w").grid(row=row, column=col, sticky="nsew")

        # Bottom border
        bottom_border = Frame(self.table_frame, bg="white", highlightbackground="#D5D8DC", highlightthickness=1)
        bottom_border.grid(row=len(students) + 2, column=0, columnspan=len(headers), sticky="ew", pady=(10, 0))

        for col in range(len(headers)):
            if col == 2:  # The 'Age' column
                self.table_frame.grid_columnconfigure(col, weight=0, minsize=50)
            else:
                self.table_frame.grid_columnconfigure(col, weight=1, uniform="equal")