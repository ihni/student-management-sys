from .config.attributes import *
from tkinter import Frame, Label, Button, Entry

class LoginFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent, bg = LOGIN_FRAME_BACKGROUND)
        
        # Introduction label
        self.label = Label(self, text=LOGIN_LABEL, font=LOGIN_LABEL_FONT)
        self.label.pack(pady=LOGIN_LABEL_PADY)

        # Error box
        self.error_message = Label(self, text="", fg=LOGIN_ERROR_FG, font=LOGIN_ERROR_FONT)
        self.error_message.pack(pady=LOGIN_ERROR_PADY)

        # ID Entry and Label
        self.id_label = Label(self, text=LOGIN_ID_LABEL, font=LOGIN_ID_LABEL_FONT)
        self.id_label.pack(pady=LOGIN_ID_LABEL_PADY)

        self.id_entry = Entry(self, font=LOGIN_ID_ENTRY_FONT)
        self.id_entry.pack(pady=LOGIN_ID_ENTRY_PADY)

        # Login button
        self.login_button = Button(self, text=LOGIN_BUTTON_TEXT, font=LOGIN_BUTTON_FONT)
        self.login_button.pack(pady=LOGIN_BUTTON_PADY)