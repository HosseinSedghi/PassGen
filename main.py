import string
import customtkinter as ctk
from generator import Generator

# theme initialize
ctk.set_appearance_mode("System")  # other options : "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # other options : "blue", "green", "dark-blue"

class PasswordGeneratorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.password = Generator()

        # window settings
        self.title("PassGen - Password Generator")
        self.geometry("420x240")
        self.resizable(False, False)
        self.iconbitmap("images/key-icon.ico")

        # top page title
        self.title_label = ctk.CTkLabel(self, text="Password Generator", font=("Consolas", 19, "bold"))
        self.title_label.pack(pady=(20, 10))

        # card password with copy btn
        self.result_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.result_frame.pack(pady=10, padx=20, fill="x")

        self.password_entry = ctk.CTkEntry(
            self.result_frame, 
            placeholder_text="Your password ... ",
            font=("Consolas", 14),
            height=40
        )
        self.password_entry.pack(side="left", expand=True, fill="x", padx=(0, 10))

        # copy btn
        self.copy_btn = ctk.CTkButton(
            self.result_frame, 
            text="Copy", 
            font=("Consolas", 15),
            width=80, 
            height=40,
            command=self.copy_password,
            fg_color="#2b8a3e", hover_color="#2b7536"
        )
        self.copy_btn.pack(side="right")

        # Generate btn
        self.generate_btn = ctk.CTkButton(
            self, 
            text="Generate", 
            font=("Consolas", 16, "bold"),
            height=45,
            command=self.generate_password
        )
        self.generate_btn.pack(pady=15, padx=20, fill="x")

        # status label ( for errors or etc. )
        self.status_label = ctk.CTkLabel(self, text="", font=("Consolas", 13), text_color="gray")
        self.status_label.pack(pady=(0, 10))

    def generate_password(self):
        password = self.password.generate()
        
        # show password
        self.password_entry.delete(0, "end")
        self.password_entry.insert(0, password)
        self.status_label.configure(text="Password generated!", text_color="#2b8a3e")

    def copy_password(self):
        password = self.password.copy_password()
        if password:
            self.clipboard_clear()
            self.clipboard_append(password)
            self.status_label.configure(text="The password copied!", text_color="#1971c2")
        else:
            self.status_label.configure(text="At first, generate a new password!", text_color="#c92a2a")

if __name__ == "__main__":
    app = PasswordGeneratorApp()
    app.mainloop()
