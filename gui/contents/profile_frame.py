from tkinter import Label, Frame

# -----------------------------------------------------
#
# Profile Frame for displaying logged-in users information
#
# -----------------------------------------------------

class ProfileFrame(Frame):
    def __init__(self, parent, user):
        super().__init__(parent, bg="white")
        self.user = user
        
        # Profile data
        name = self.user.name
        age = self.user.age
        user_id = self.user.id
        email = self.user.email
        phone = self.user.phone

        # Title Label
        title_label = Label(self, text="User Profile", font=("Arial", 30, "bold"), bg="white", fg="#2c3e50")
        title_label.pack(pady=40)

        # Profile Section (Centered)
        profile_section = Frame(self, bg="white", padx=40, pady=40)
        profile_section.pack(fill="both", padx=50, pady=60, expand=True)

        # Info Label Styling
        info_label_style = ("Arial", 16)
        label_style = {"anchor": "w", "bg": "white", "font": info_label_style, "fg": "#34495e"}

        # Adding the profile data labels
        Label(profile_section, text=f"Name: {name}", **label_style).pack(fill="x", pady=8)
        Label(profile_section, text=f"Age: {age}", **label_style).pack(fill="x", pady=8)
        Label(profile_section, text=f"ID: {user_id}", **label_style).pack(fill="x", pady=8)
        Label(profile_section, text=f"Email: {email}", **label_style).pack(fill="x", pady=8)
        Label(profile_section, text=f"Phone: {phone}", **label_style).pack(fill="x", pady=8)

        # Center the Profile Section on the screen
        self.pack(fill="both", expand=True)