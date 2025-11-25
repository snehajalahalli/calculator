import tkinter as tk

# Function to update the expression in the display
def button_click(value):
    current = entry_var.get()
    entry_var.set(current + value)

# Function to clear the display
def clear_display():
    entry_var.set("")

# Function to calculate the result
def calculate():
    try:
        result = eval(entry_var.get())
        entry_var.set(str(result))
    except:
        entry_var.set("Error")

# Main window
root = tk.Tk()
root.title("Android Calculator")
root.geometry("320x420")
root.resizable(False, False)

entry_var = tk.StringVar()

# Display screen
entry = tk.Entry(root, textvariable=entry_var, font=("Arial", 24), bd=10, relief=tk.RIDGE, justify="right")
entry.grid(row=0, column=0, columnspan=4, ipadx=10, ipady=20)

# Button layout similar to Android calculator
buttons = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3)
]

# Create buttons
for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18),
                        command=calculate, bg="#4CAF50", fg="white")
    else:
        btn = tk.Button(root, text=text, width=5, height=2, font=("Arial", 18),
                        command=lambda t=text: button_click(t))
    
    btn.grid(row=row, column=col, padx=5, pady=5)

# Clear button (Android style)
clear_btn = tk.Button(root, text="C", width=22, height=2, font=("Arial", 18),
                      command=clear_display, bg="#F44336", fg="white")
clear_btn.grid(row=5, column=0, columnspan=4, padx=5, pady=10)

root.mainloop()
