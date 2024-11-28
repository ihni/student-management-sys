# src/gui/add_student_view.py
from tkinter import *
from tkinter import messagebox

class AddStudentView(Frame):
    def __init__(self, master, auth, student_controller):
        super().__init__(master)
        self.master = master
        self.auth = auth
        self.student_controller = student_controller
        self.create_widgets()

    def create_widgets(self):
        """Create widgets for adding a new student."""
        self.label_name = Label(self, text="Name:")
        self.label_name.grid(row=0, column=0, padx=10, pady=10)
        self.entry_name = Entry(self)
        self.entry_name.grid(row=0, column=1, padx=10, pady=10)

        self.label_age = Label(self, text="Age:")
        self.label_age.grid(row=1, column=0, padx=10, pady=10)
        self.entry_age = Entry(self)
        self.entry_age.grid(row=1, column=1, padx=10, pady=10)

        self.label_id = Label(self, text="ID:")
        self.label_id.grid(row=2, column=0, padx=10, pady=10)
        self.entry_id = Entry(self)
        self.entry_id.grid(row=2, column=1, padx=10, pady=10)

        self.label_email = Label(self, text="Email:")
        self.label_email.grid(row=3, column=0, padx=10, pady=10)
        self.entry_email = Entry(self)
        self.entry_email.grid(row=3, column=1, padx=10, pady=10)

        self.label_phone = Label(self, text="Phone:")
        self.label_phone.grid(row=4, column=0, padx=10, pady=10)
        self.entry_phone = Entry(self)
        self.entry_phone.grid(row=4, column=1, padx=10, pady=10)

        self.button_add = Button(self, text="Add Student", command=self.add_student)
        self.button_add.grid(row=5, columnspan=2, pady=20)

        self.button_cancel = Button(self, text="Cancel", command=self.cancel)
        self.button_cancel.grid(row=6, columnspan=2, pady=10)

        self.pack()

    def add_student(self):
        """Add the student using the StudentController."""
        name = self.entry_name.get()
        age = self.entry_age.get()
        student_id = self.entry_id.get()
        email = self.entry_email.get()
        phone = self.entry_phone.get()

        errors = self.student_controller.add_student(name, age, student_id, email, phone)
        
        if errors:
            error_message = "\n".join([f"{key}: {msg}" for key, msg in errors.items()])
            messagebox.showerror("Error", error_message)
        else:
            messagebox.showinfo("Success", "Student added successfully!")
            self.master.switch_view('dashboard')

    def cancel(self):
        """Cancel and return to the dashboard."""
        self.master.switch_view('dashboard')
