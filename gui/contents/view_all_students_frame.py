from tkinter import Frame, Label
from ..config.color import *

# -----------------------------------------------------
#
# View All Students Frame displaying a table for all users in the system
#
# -----------------------------------------------------

class ViewAllStudentsFrame(Frame):
    def __init__(self, parent, student_controller):
        self.student_controller = student_controller
        super().__init__(parent, bg="white")
        
        Label(self, text="View all students", font=("Arial", 16)).grid(row=0, column=0, pady=20, columnspan=5)
        print(f"{CYAN}Initializing View All Students frame...{RESET}")

        # Call update_view initially to display the students
        self.update_view()

    def update_view(self):
        # Clear previous student labels
        for widget in self.winfo_children():
            widget.grid_forget()

        Label(self, text="View all students", font=("Arial", 16)).grid(row=0, column=0, pady=20, columnspan=5)

        students = self.student_controller.fetch_all_students()
        print(f"{YELLOW}Fetched {len(students)} students from the database.{RESET}")

        headers = ["ID", "Name", "Age", "Email", "Phone"]
        
        # Display header row
        for col, header in enumerate(headers):
            Label(self, text=header, font=("Arial", 12, "bold"), bg="lightgray", relief="solid", width=20, anchor="center").grid(row=1, column=col, sticky="nsew")

        # Display student data
        for row, student in enumerate(students, start=2):
            Label(self, text=student.id, font=("Arial", 12), relief="solid", width=20, anchor="center").grid(row=row, column=0, sticky="nsew")
            Label(self, text=student.name, font=("Arial", 12), relief="solid", width=20, anchor="center").grid(row=row, column=1, sticky="nsew")
            Label(self, text=student.age, font=("Arial", 12), relief="solid", width=20, anchor="center").grid(row=row, column=2, sticky="nsew")
            Label(self, text=student.email, font=("Arial", 12), relief="solid", width=20, anchor="center").grid(row=row, column=3, sticky="nsew")
            Label(self, text=student.phone, font=("Arial", 12), relief="solid", width=20, anchor="center").grid(row=row, column=4, sticky="nsew")
            print(f"{GREEN}Displayed student {student.name} (ID: {student.id}) at row {row}{RESET}")

        # Configure columns for equal width
        for col in range(len(headers)):
            self.grid_columnconfigure(col, weight=1, uniform="equal")