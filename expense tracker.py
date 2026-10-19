
import tkinter as tk
from tkinter import messagebox

total = 0
expenses = []

# Function to add expense
def add_expense():
    global total

    expense = entry.get()

    if expense == "":
        messagebox.showwarning("Warning", "Please enter an expense!")
    else:
        try:
            expense = float(expense)

            if expense < 0:
                messagebox.showwarning("Warning", "Enter a positive amount!")
            else:
                expenses.append(expense)
                total = total + expense

                expense_list.insert(
                    tk.END, "Rs. " + str(expense)
                )

                total_label.config(
                    text="Total Spent: Rs. " + str(round(total, 2))
                )

                entry.delete(0, tk.END)

        except ValueError:
            messagebox.showerror(
                "Error", "Please enter a valid number!"
            )


# Function to finish tracking
def finish():
    messagebox.showinfo(
        "Final Total",
        "Your Total Spent is Rs. " + str(round(total, 2))
    )


# Create GUI window
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("400x500")
root.config(bg="lightblue")

# Heading
heading = tk.Label(
    root,
    text="EXPENSE TRACKER",
    font=("Arial", 20, "bold"),
    bg="lightblue"
)
heading.pack(pady=20)

# Input label
label = tk.Label(
    root,
    text="Enter Expense Amount (Rs.):",
    font=("Arial", 12),
    bg="lightblue"
)
label.pack()

# Input box
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

# Add Expense button
add_button = tk.Button(
    root,
    text="Add Expense",
    font=("Arial", 12, "bold"),
    bg="green",
    fg="white",
    command=add_expense
)
add_button.pack(pady=10)

# Expense list
expense_list = tk.Listbox(root, font=("Arial", 12), height=8)
expense_list.pack(pady=10, padx=20, fill="x")

# Total label
total_label = tk.Label(
    root,
    text="Total Spent: Rs. 0",
    font=("Arial", 14, "bold"),
    bg="lightblue"
)
total_label.pack(pady=10)

# Finish button
finish_button = tk.Button(
    root,
    text="Finish",
    font=("Arial", 12, "bold"),
    bg="red",
    fg="white",
    command=finish
)
finish_button.pack(pady=10)

# Run GUI
root.mainloop()
