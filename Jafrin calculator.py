import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

# Create main application window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x400")
root.resizable(False, False)

# Entry widget for input and output
entry = tk.Entry(root, font="Arial 25", bg="white", fg="black", justify=tk.RIGHT)
entry.grid(row=0, column=0, columnspan=4, padx=12, pady=12)

# Button design properties
button_config = {
    "font": ("Arial", 17),
    "bg": "white",
    "fg": "black",
    "width": 5,
    "height": 2,
    "relief": tk.RAISED
}

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Add buttons to the window
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, **button_config)
    button.grid(row=row, column=col, padx=5, pady=5)
    button.bind("<Button-1>", click)

# Start the GUI event loop
root.mainloop()
