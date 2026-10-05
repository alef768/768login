import tkinter as tk
from PIL import Image, ImageTk


class Application:
    def __init__(self, root):
        self.root = root
        root.title("768chat")
        root.geometry("280x180")
        root.resizable(False, False)

        # bg
        image = Image.open(
            "tkinter_bg.jpg"
        ).resize((280, 180))

        # icon
        icon = Image.open(
            "icon.png"
        )
        
        # set images
        self.bg_image = ImageTk.PhotoImage(image)
        self.icon = ImageTk.PhotoImage(icon)
        root.iconphoto(False, self.icon)
        
        self.canvas = tk.Canvas(
            root,
            width=280,
            height=180,
            highlightthickness=0,
            bd=0
        )
        self.canvas.pack()

        # bg canvas
        self.canvas.create_image(
            0, 0,
            image=self.bg_image,
            anchor="nw"
        )

        # user label
        self.canvas.create_text(
            20, 35,
            text="User:",
            fill="white",
            font=("Arial", 10, "bold"),
            anchor="w"
        )
        
        # password label
        self.canvas.create_text(
            20, 75,
            text="Key:",
            fill="white",
            font=("Arial", 10, "bold"),
            anchor="w"
        )

        # entries
        self.entry_user = tk.Entry(
            root,
            bg="white",
            fg="black",
            relief="flat"
        )
        self.entry_user.place(
            x=100,
            y=20,
            width=160,
            height=30
        )

        self.entry_password = tk.Entry(
            root,
            show="*",
            bg="white",
            fg="black",
            relief="flat"
        )
        self.entry_password.place(
            x=100,
            y=60,
            width=160,
            height=30
        )

        # register
        self.register_text = self.canvas.create_text(
            70, 135,
            text="Register",
            fill="white",
            font=("Arial", 10, "bold"),
            anchor="center"
        )

        # login
        self.login_text = self.canvas.create_text(
            210, 135,
            text="Initialize",
            fill="white",
            font=("Arial", 10, "bold"),
            anchor="center"
        )

        # clickables
        self.canvas.tag_bind(
            self.register_text,
            "<Button-1>",
            lambda event: self.on_register()
        )

        self.canvas.tag_bind(
            self.login_text,
            "<Button-1>",
            lambda event: self.on_login()
        )

        # hovers
        self.canvas.tag_bind(
            self.register_text,
            "<Enter>",
            lambda event: self.canvas.itemconfig(
                self.register_text,
                fill="#00ffff"
            )
        )

        self.canvas.tag_bind(
            self.register_text,
            "<Leave>",
            lambda event: self.canvas.itemconfig(
                self.register_text,
                fill="white"
            )
        )

        self.canvas.tag_bind(
            self.login_text,
            "<Enter>",
            lambda event: self.canvas.itemconfig(
                self.login_text,
                fill="#00ffff"
            )
        )

        self.canvas.tag_bind(
            self.login_text,
            "<Leave>",
            lambda event: self.canvas.itemconfig(
                self.login_text,
                fill="white"
            )
        )
    
    # onclick funcs
    def on_login(self):
        username = self.entry_user.get()
        password = self.entry_password.get()

        print(f"Login: {username}; {password}")

    def on_register(self):
        username = self.entry_user.get()
        password = self.entry_password.get()
        
        print(f"Register: {username}; {password}")

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    root.mainloop()
