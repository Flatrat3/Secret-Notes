import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet
import base64
import hashlib

#Windows setting
window = tk.Tk()
window.title("Secret Notes")
window.geometry("400x400")




#Functions

def generate_key(password: str) -> bytes:
    digest = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(digest)

print(generate_key("Asim"))

def save_encrypt():
    title = title_entry.get()
    secret = secret_text.get("1.0", tk.END).strip()
    master_key=key_entry.get()

#control
    if not title or not secret or not master_key:
        tk.messagebox.showerror("Error", "All fields are required")
    return


def decrypt():
    pass




# Top secret logo
logo=tk.Label(window,text="🔒 TOP SECRET 🔒", font=("Arial", 16, "bold"))
logo.pack()


# Title
logo=tk.Label(window,text="Enter your title",)
logo.pack()
title_entry = tk.Entry(window, width=40)
title_entry.pack(pady=5)

# Secret text
tk.Label(window, text="Enter your secret").pack()
secret_text = tk.Text(window, width=40, height=10)
secret_text.pack(pady=5)

# Master key
tk.Label(window, text="Enter master key").pack()
key_entry = tk.Entry(window, width=40, show="*")
key_entry.pack(pady=5)

# Buttons
btn_frame = tk.Frame(window)
btn_frame.pack(pady=5)

save_btn=tk.Button(btn_frame, text="Save & Encrypt", command=save_encrypt)
save_btn.grid(row=0, column=0, padx=5, pady=5)

decrypt_btn=tk.Button(btn_frame, text="Decrypt", command=decrypt)
decrypt_btn.grid(row=0, column=1, padx=5, pady=5)

window.mainloop()