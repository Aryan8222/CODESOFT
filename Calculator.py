import tkinter as tk

# Function to update the expression when a button is clicked
def button_click(event):
    current = entry.get()
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = str(eval(current))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x500")

# Entry field for displaying the expression
entry = tk.Entry(root, font=("Arial", 24))
entry.pack(fill=tk.BOTH, expand=True)

# Create a frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(fill=tk.BOTH, expand=True)

# Define button labels
button_labels = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", "C", "=", "+",
]

# Create and display buttons
row, col = 0, 0
for label in button_labels:
    button = tk.Button(
        button_frame,
        text=label,
        font=("Arial", 20),
        relief=tk.RIDGE,
        width=4,
        height=2,
    )
    button.grid(row=row, column=col, padx=5, pady=5)
    button.bind("<Button-1>", button_click)  # Bind click event to the button_click function
    col += 1
    if col > 3:
        col = 0
        row += 1

# Run the application
root.mainloop()
