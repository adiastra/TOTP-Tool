import tkinter as tk
import pyotp
import base64

class TOTPGenerator:
    def __init__(self, master):
        self.master = master
        master.title("TOTP Token Generator")

        # Create the input label and entry box for the secret key
        self.secret_label = tk.Label(master, text="Enter a secret key (leave blank to generate a new one):")
        self.secret_label.pack()
        self.secret_entry = tk.Entry(master)
        self.secret_entry.pack()

        # Create the "Generate TOTP" button
        self.generate_button = tk.Button(master, text="Generate TOTP", command=self.generate_totp)
        self.generate_button.pack()

        # Create the output label for the TOTP token
        self.totp_label = tk.Label(master, text="TOTP Token:")
        self.totp_label.pack()

        # Create the output entry boxes for the secret key in Base32 and hexadecimal formats
        self.base32_secret_label = tk.Label(master, text="Secret (Base32):")
        self.base32_secret_label.pack()
        self.base32_secret_entry = tk.Entry(master)
        self.base32_secret_entry.pack()

        self.hex_secret_label = tk.Label(master, text="Secret (Hexadecimal):")
        self.hex_secret_label.pack()
        self.hex_secret_entry = tk.Entry(master)
        self.hex_secret_entry.pack()

    def generate_totp(self):
        # Get the TOTP secret from the input box or generate a new one
        user_input = self.secret_entry.get().strip()
        if user_input:
            secret = user_input
        else:
            secret = pyotp.random_base32()

        # Create a TOTP object with the secret
        totp = pyotp.TOTP(secret)

        # Get the secret in Base32 and hexadecimal formats
        base32_secret = totp.secret
        hex_secret = base64.b32decode(base32_secret, casefold=True).hex()

        # Update the output label and entry boxes with the current TOTP token and the secret in both formats
        self.totp_label.config(text=f"TOTP Token: {totp.now()}")
        self.base32_secret_entry.delete(0, tk.END)
        self.base32_secret_entry.insert(0, base32_secret)
        self.hex_secret_entry.delete(0, tk.END)
        self.hex_secret_entry.insert(0, hex_secret)

if __name__ == '__main__':
    root = tk.Tk()
    app = TOTPGenerator(root)
    root.mainloop()
