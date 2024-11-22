import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta

# Function to calculate the future date
def calculate_future_date():
    try:
        # Retrieve input date and days to add
        date_1 = datetime.strptime(entry_date.get(), "%d-%m-%Y")
        days_to_add = int(entry_days.get())
        # Calculate future date
        future_date = date_1 + timedelta(days=days_to_add)
        result_label.config(text=f"Future Date: {future_date.strftime('%d-%m-%Y')}")
    except ValueError:
        result_label.config(text="Error: Please enter valid input.")

# Create the main window
root = tk.Tk()
root.title("Future Date Calculator")
root.geometry("400x300")
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
title_label = ttk.Label(root, text="Future Date Calculator", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Input fields
frame = tk.Frame(root, bg="#1e1e1e")
frame.pack(pady=10)

# Start date input
ttk.Label(frame, text="Start Date (DD-MM-YYYY):").grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_date = ttk.Entry(frame, width=20)
entry_date.grid(row=0, column=1, padx=5, pady=5)

# Days to add input
ttk.Label(frame, text="Days to Add:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_days = ttk.Entry(frame, width=20)
entry_days.grid(row=1, column=1, padx=5, pady=5)

# Calculate Future Date Button
calculate_button = ttk.Button(root, text="Calculate Future Date", command=calculate_future_date)
calculate_button.pack(pady=10)

# Result Label
result_label = ttk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# About Section
about_label = ttk.Label(root, text="Created by: Raymond C. Turner", font=("Arial", 8))
about_label.pack(side="bottom", pady=10)

# Run the application
root.mainloop()
