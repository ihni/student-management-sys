from tkinter import *
from tkinter import messagebox

class DashboardView(Frame):
    def __init__(self, master, auth, student_controller):
        super().__init__(master)
        self.master = master
        self.auth = auth
        self.student_controller = student_controller
        
        self.create_widgets()

    def create_widgets(self):
        self.label_welcome = Label(self, text="Welcome to the Student Management System")
        self.label_welcome.grid(row=0, column=0, columnspan=2, pady=20)
        
        self.button_view_students = Button(self, text="View All Students", command=self.view_all_students)
        self.button_view_students.grid(row=1,columnspan=2, pady=10)

        self.button_view_my_info = Button(self, text="View My Information", command=self.view_my_information)
        self.button_view_my_info.grid(row=2, columnspan=2, pady=10)

        self.button_add_student = Button(self, text="Add Student", command=self.add_student)
        self.button_add_student.grid(row=3, columnspan=2, pady=10)

        self.button_logout = Button(self, text="Logout", command=self.logout)
        self.button_logout.grid(row=4, columnspan=2, pady=20)

        self.pack()

    def view_all_students(self):
        students = self.student_contrller.fetch_all_students()
        display_txt = ""

        for student in students:
            name, age, id, email, phone = student.get_data()
            display_txt += f"{name} {age} {id} {email} {phone}\n"
        messagebox.showinfo("All Students", display_txt)

    def view_my_information(self):
        user = self.auth.get_user()
        if user:
            student_info = f"Name: {user.name}\nID {user.id}\nAge: {user.age}\nEmail: {user.email}\nPhone Number: {user.phone}"
            messagebox.showinfo("My Information", student_info)

    def add_student(self):
        self.master.switch_view('add_student')

    def logout(self):
        if self.auth.logout():
            self.master.switch_view('login')
        else:
            messagebox.showerror("Lougout Failed", "No user is currently logged in")
