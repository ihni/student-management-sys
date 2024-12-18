import customtkinter as ctk
from PIL import Image, ImageOps, ImageDraw
import random
# -----------------------------------------------------
#
# Profile Frame for displaying logged-in users information
#
#   **TODO FIX UI**
# -----------------------------------------------------

class ProfileFrame(ctk.CTkFrame):
    PROFILE_ICON_SIZE = (200,200) # width x height
    NUMBER_OF_PROFILES = 5        # This must be matched with number of images

    def __init__(self, parent, user):
        super().__init__(parent, fg_color="#010409")
        self.user = user

        self.center = ctk.CTkFrame(
            self,
            fg_color="#010409",
            bg_color="#010409",
        )
        self.center.pack(expand=True, padx=20, pady=20)

        # Profile data
        name = self.user.name.strip().lower()
        age = self.user.age
        user_id = self.user.id
        email = self.user.email
        phone = self.user.phone

        # Header
        ctk.CTkLabel(
            self.center,
            text="User Profile",
            font=("Arial", 30, "bold"),
            fg_color="#010409",
            text_color="white"
        ).pack(pady=40)


        # Profile Section
        profile_section = ctk.CTkFrame(self.center, fg_color="#010409")
        profile_section.pack(fill="both", padx=50, pady=60, expand=True)
        
        # Profile Picture
        ctk.CTkButton(
            profile_section,
            text="", 
            bg_color="transparent", 
            fg_color="transparent",
            hover_color="#010409",
            corner_radius=300,
            image=random.choice(profile_icons := self.generate_profile_icons())
        ).pack()

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

    def generate_profile_icons(self) -> list[object]:
        '''Returns a list of circular icons'''
        icons = []
        for i in range(1, self.NUMBER_OF_PROFILES+1):
            icons.append(ctk.CTkImage(
                light_image=self.make_image_circular(f"gui/images/profile-icons/{i}.png"),
                size=self.PROFILE_ICON_SIZE)
            )
        return icons
            

    def make_image_circular(self, image_path: str):
        '''
        From stack overflow
        https://stackoverflow.com/questions/890051/how-do-i-generate-circular-thumbnails-with-pil

        Thanks to DRC!
        '''
        mask = Image.new('L', self.PROFILE_ICON_SIZE, 0)
        draw = ImageDraw.Draw(mask) 
        draw.ellipse((0, 0) + self.PROFILE_ICON_SIZE, fill=255)

        im = Image.open(image_path)

        output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
        output.putalpha(mask)

        return output