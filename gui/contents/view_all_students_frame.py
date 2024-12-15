from tkinter import Frame, Label

class ViewAllStudentsFrame(Frame):
    def __init__(self, parent, student_controller):
        self.student_controller = student_controller
        super().__init__(parent, bg="white")
        Label(self, text="View all students", font=("Arial", 16)).pack(pady=20)