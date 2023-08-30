import tkinter as tk
import random
import string


def generate_password():
    try:
        length = int(length_entry.get())
        if length < 8:
            result_label.config(text="Password length must be at least 8 characters.")
            return

        characters = string.ascii_letters
        if include_digits.get():
            characters += string.digits
        if include_symbols.get():
            characters += string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))
        result_label.config(text="Generated Password: " + password)

    except ValueError:
        result_label.config(text="Please enter a valid number for password length.")


def reset_password():
    length_entry.delete(0, tk.END)
    include_digits.set(False)
    include_symbols.set(False)
    result_label.config(text="")


# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")

# Create and pack widgets
length_label = tk.Label(root, text="Password Length:")
length_label.pack(pady=10)

length_entry = tk.Entry(root)
length_entry.pack()

include_digits = tk.BooleanVar()
digits_checkbox = tk.Checkbutton(root, text="Include Digits (0-9)", variable=include_digits)
digits_checkbox.pack()

include_symbols = tk.BooleanVar()
symbols_checkbox = tk.Checkbutton(root, text="Include Symbols (!@#$, etc.)", variable=include_symbols)
symbols_checkbox.pack()

generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

result_label = tk.Label(root, text="", wraplength=300)
result_label.pack()


reset_button = tk.Button(root, text="Reset", command=reset_password)
reset_button.pack()

# Run the application
root.mainloop()
