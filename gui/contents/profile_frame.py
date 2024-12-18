from tkinter import Label, Frame
import customtkinter as ctk
# -----------------------------------------------------
#
# Profile Frame for displaying logged-in users information
#
#   **TODO FIX UI**
# -----------------------------------------------------

class ProfileFrame(ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent, fg_color="#010409")
        self.user = user

        # Profile data
        name = self.user.name.strip().lower()
        age = self.user.age
        user_id = self.user.id
        email = self.user.email
        phone = self.user.phone

        # Title Label
        title_label = ctk.CTkLabel(self, text="User Profile", font=("Arial", 30, "bold"), fg_color="#010409", text_color="white")
        title_label.pack(pady=40)

        # Profile Section
        profile_section = ctk.CTkFrame(self, fg_color="#010409")
        profile_section.pack(fill="both", padx=50, pady=60, expand=True)

        # Info Label Styling
        info_label_style = ("Arial", 16)
        label_style = {"anchor": "w", "fg_color": "#010409", "font": info_label_style, "text_color": "white"}

        # Adding the profile data labels
        ctk.CTkLabel(profile_section, text=f"Name: {name}", **label_style).pack(fill="x", pady=8)
        ctk.CTkLabel(profile_section, text=f"Age: {age}", **label_style).pack(fill="x", pady=8)
        ctk.CTkLabel(profile_section, text=f"ID: {user_id}", **label_style).pack(fill="x", pady=8)
        ctk.CTkLabel(profile_section, text=f"Email: {email}", **label_style).pack(fill="x", pady=8)
        ctk.CTkLabel(profile_section, text=f"Phone: {phone}", **label_style).pack(fill="x", pady=8)

        # Center the Profile Section on the screen
        self.pack(fill="both", expand=True)