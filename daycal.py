import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta

# Function to calculate the difference in days
def calculate_days():
    try:
        date_1 = datetime.strptime(entry_date1.get(), "%d-%m-%Y")
        date_2 = datetime.strptime(entry_date2.get(), "%d-%m-%Y")
        days_difference = (date_2 - date_1).days
        result_label.config(text=f"Days Difference: {days_difference}")
    except ValueError:
        result_label.config(text="Error: Please enter valid dates (DD-MM-YYYY).")

# Function to calculate the future date
def calculate_future_date():
    try:
        # Retrieve input date and days to add
        date_1 = datetime.strptime(entry_date.get(), "%d-%m-%Y")
        days_to_add = int(entry_days.get())
        # Calculate future date
        future_date = date_1 + timedelta(days=days_to_add)
        future_date_label.config(text=f"Future Date: {future_date.strftime('%d-%m-%Y')}")
    except ValueError:
        future_date_label.config(text="Error: Please enter valid input.")

# Function to clear the Days Difference inputs and result
def clear_days_inputs():
    entry_date1.delete(0, tk.END)
    entry_date2.delete(0, tk.END)
    result_label.config(text="")

# Function to clear the Future Date inputs and result
def clear_future_inputs():
    entry_date.delete(0, tk.END)
    entry_days.delete(0, tk.END)
    future_date_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("Date Calculator")
root.geometry("400x550")
root.configure(bg="#1e1e1e")  # Dark background

# Set dark mode styling
style = ttk.Style()
style.theme_use("clam")
style.configure(
    "TLabel", background="#1e1e1e", foreground="white", font=("Arial", 10)
)
style.configure(
    "TButton", background="#2d2d2d", foreground="white", font=("Arial", 10)
)
style.configure(
    "TEntry", fieldbackground="#2d2d2d", foreground="white", insertcolor="white"
)

# Title Label
title_label = ttk.Label(root, text="Date Calculator", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Days Difference Section
frame1 = tk.Frame(root, bg="#1e1e1e")
frame1.pack(pady=10)

ttk.Label(frame1, text="Start Date (DD-MM-YYYY):").grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_date1 = ttk.Entry(frame1, width=20)
entry_date1.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame1, text="End Date (DD-MM-YYYY):").grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_date2 = ttk.Entry(frame1, width=20)
entry_date2.grid(row=1, column=1, padx=5, pady=5)

# Calculate Days Difference Button
calculate_button = ttk.Button(root, text="Calculate Days Difference", command=calculate_days)
calculate_button.pack(pady=10)

# Result Label for Days Difference
result_label = ttk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Clear Days Difference Button
clear_button1 = ttk.Button(root, text="Clear", command=clear_days_inputs)
clear_button1.pack(pady=5)

# Future Date Section
frame2 = tk.Frame(root, bg="#1e1e1e")
frame2.pack(pady=10)

ttk.Label(frame2, text="Start Date (DD-MM-YYYY):").grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_date = ttk.Entry(frame2, width=20)
entry_date.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame2, text="Days to Add:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_days = ttk.Entry(frame2, width=20)
entry_days.grid(row=1, column=1, padx=5, pady=5)

# Calculate Future Date Button
future_date_button = ttk.Button(root, text="Calculate Future Date", command=calculate_future_date)
future_date_button.pack(pady=10)

# Result Label for Future Date
future_date_label = ttk.Label(root, text="", font=("Arial", 12))
future_date_label.pack(pady=10)

# Clear Future Date Button
clear_button2 = ttk.Button(root, text="Clear", command=clear_future_inputs)
clear_button2.pack(pady=5)

# About Section
about_label = ttk.Label(root, text="Created by Raymond C. Turner - v0.1.4", font=("Arial", 8))
about_label.pack(side="bottom", pady=10)

# Run the application
root.mainloop()
