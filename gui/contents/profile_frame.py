from tkinter import Label, Frame
from ..config.color import *

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
        title_label = Label(self, text="User Profile Information", font=("Arial", 20, "bold"), bg="white", fg="darkblue")
        title_label.pack(pady=20)

        # Profile Section
        profile_section = Frame(self, bg="lightgray", padx=20, pady=20)
        profile_section.pack(fill="both", padx=30, pady=20)

        # Display User Information
        info_label_style = ("Arial", 14)
        Label(profile_section, text=f"Name: {name}", font=info_label_style, anchor="w", bg="lightgray").pack(fill="x", pady=5)
        Label(profile_section, text=f"Age: {age}", font=info_label_style, anchor="w", bg="lightgray").pack(fill="x", pady=5)
        Label(profile_section, text=f"ID: {user_id}", font=info_label_style, anchor="w", bg="lightgray").pack(fill="x", pady=5)
        Label(profile_section, text=f"Email: {email}", font=info_label_style, anchor="w", bg="lightgray").pack(fill="x", pady=5)
        Label(profile_section, text=f"Phone: {phone}", font=info_label_style, anchor="w", bg="lightgray").pack(fill="x", pady=5)
