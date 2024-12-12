from tkinter import Frame, Label, Entry, Button, messagebox

class LoginView(Frame):
    def __init__(self, master, auth, student_controller):
        super().__init__(master.root)
        self.master = master
        self.auth = auth
        self.student_controller = student_controller

        self.create_widgets()

    def create_widgets(self):
        self.label_id = Label(self, text="ID:")
        self.label_id.grid(row=0, column=0, padx=10, pady=10)
        self.entry_id = Entry(self)
        self.entry_id.grid(row=0, column=1, padx=10, pady=10)

        self.button_login = Button(self, text="Login", command=self.login)
        self.button_login.grid(row=2, columnspan=2, pady=20)
        self.pack()

    def login(self):
        id = self.entry_id.get()

        result = self.auth.login(id)

        if result == "Login successful":
            messagebox.showinfo("Success", "Login successful!")
            self.master.switch_view('dashboard')
        else:
            messagebox.showerror("Login Failed", result)