import tkinter as tk
from tkinter import ttk
from datetime import datetime

# Function to calculate the difference in days
def calculate_days():
    try:
        date_1 = datetime.strptime(entry_date1.get(), "%Y-%m-%d")
        date_2 = datetime.strptime(entry_date2.get(), "%Y-%m-%d")
        days_difference = (date_2 - date_1).days
        result_label.config(text=f"Days Difference: {days_difference}")
    except ValueError:
        result_label.config(text="Error: Please enter valid dates (YYYY-MM-DD).")

# Create the main window
root = tk.Tk()
root.title("Days Difference Calculator")
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
title_label = ttk.Label(root, text="Days Difference Calculator", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Input fields
frame = tk.Frame(root, bg="#1e1e1e")
frame.pack(pady=10)

ttk.Label(frame, text="Start Date (YYYY-MM-DD):").grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_date1 = ttk.Entry(frame, width=20)
entry_date1.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame, text="End Date (YYYY-MM-DD):").grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_date2 = ttk.Entry(frame, width=20)
entry_date2.grid(row=1, column=1, padx=5, pady=5)

# Calculate Button
calculate_button = ttk.Button(root, text="Calculate", command=calculate_days)
calculate_button.pack(pady=10)

# Result Label
result_label = ttk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# About Section
about_label = ttk.Label(root, text="About: Created by Ray C. Turner", font=("Arial", 8))
about_label.pack(side="bottom", pady=10)

# Run the application
root.mainloop()
