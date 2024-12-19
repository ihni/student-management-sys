import customtkinter as ctk
from PIL import Image, ImageOps, ImageDraw
from ..packages.CTkCodeBox import *
import random
# -----------------------------------------------------
#
# Profile Frame for displaying logged-in users information
#
# -----------------------------------------------------

class ProfileFrame(ctk.CTkFrame):
    PROFILE_ICON_SIZE = (200,200) # width x height
    NUMBER_OF_PROFILES = 5        # This must be matched with number of images

    def __init__(self, parent, user):
        super().__init__(parent, fg_color="#010409")
        self.user = user

        self.center = ctk.CTkFrame(
            self,
            fg_color="transparent",
        )
        self.center.pack(expand=True, fill="both")

        # Header
        ctk.CTkLabel(
            self.center,
            text="Student Profile",
            font=("Helvetica", 18, "bold"),
            fg_color="#010409",
            text_color="white"
        ).pack()


        # Profile Section
        profile_section = ctk.CTkFrame(
            self.center, 
            fg_color="#151B23",
            border_color="#313840",
            border_width=1,
        )
        profile_section.pack(expand=True, fill="x", padx=20, pady=(20, 80))
        
        # Profile Picture
        ctk.CTkButton(
            profile_section,
            text="", 
            bg_color="transparent", 
            fg_color="transparent",
            hover_color="#151B23",
            image=random.choice(profile_icons := self.generate_profile_icons()),
        ).pack(side="left", padx=(20,40))

        # Code Box for displaying student info
        codebox = CTkCodeBox(
            profile_section,
            language="rust",
            theme="github-dark",
            fg_color="#1D2331",
            menu=False,
            font=("Consolas", 14),
            wrap=True,
        )
        codebox.pack(padx=(5,20), pady=10, expand=True,fill="both")

        # Profile data
        name    = self.user.name.capitalize()
        age     = self.user.age
        user_id = self.user.id
        email   = self.user.email
        phone   = self.user.phone

        #
        # Section for displaying student information in code format
        #

        display_code = """
fn main() {
    // About me
    println!("Welcome to your profile!");\n
    let name:  &str = \"""" + name + """\";
    let age:    i32 =  """ + str(age) + """;
    let id:    &str = \"""" + user_id + """\";
    let email: &str = \"""" + email + """\";
    let phone:  i32 =  """ + str(phone) + """;
}
"""
        codebox.insert("1.0", display_code)
        codebox.configure(state="disabled")

        #
        # End of section
        #

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
        mask = Image.new('L', (1000,1000), 0)
        draw = ImageDraw.Draw(mask) 
        draw.ellipse((0, 0) + (1000,1000), fill=255)

        im = Image.open(image_path)

        output = ImageOps.fit(im, mask.size, centering=(0.5, 0.5))
        output.putalpha(mask)

        return output