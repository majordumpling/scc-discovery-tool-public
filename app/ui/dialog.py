from tkinter import messagebox
from typing import Tuple
from app import logging_config

import tkinter as tk
import tkinter.simpledialog as simpledialog

logger = logging_config.get_logger(__name__)

def get_credentials() -> Tuple[str, str]:
    logger.info("Displaying credentials dialog")
    
    root = tk.Tk()
    root.withdraw()

    username: str = simpledialog.askstring("Login", "Enter username:", parent=root)
    password: str = simpledialog.askstring("Login", "Enter password:", parent=root, show='*')

    root.destroy()
    
    if username:
        logger.info(f"User entered username: {username}")
    else:
        logger.warning("No username provided")

    return username, password

def choose_environment() -> str:
    logger.info("Displaying environment selection dialog")
    
    def on_select():
        nonlocal choice
        choice = var.get()
        logger.info(f"User selected environment: {choice}")
        root.destroy()
        
    root = tk.Tk()
    root.title("Select Environment")
    
    choice = None
    var = tk.StringVar(value="Dev")
    tk.Label(root, text="Choose environment:").pack(padx=20, pady=10)
    for environment in ["Dev", "QA", "Prod"]:
        tk.Radiobutton(root, text=environment, variable=var, value=environment).pack(anchor='w', padx=20)
    tk.Button(root, text="OK", command=on_select).pack(pady=10)
    
    root.mainloop()
    return choice

def display_messagebox(message: str) -> None:
    logger.info(f"Displaying success message: {message}")
    messagebox.showinfo("Completed", f"Data successfully written to {message}")