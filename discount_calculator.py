import tkinter as tk
from tkinter import messagebox


def calculate_discount():
    try:
        price = float(price_entry.get())
        discount = float(discount_entry.get())
        quantity = int(quantity_entry.get())

        if price < 0:
            messagebox.showerror("Invalid Input", "Price cannot be negative.")
            return

        if discount < 0 or discount > 100:
            messagebox.showerror(
                "Invalid Input",
                "Discount must be between 0 and 100."
            )
            return

        if quantity <= 0:
            messagebox.showerror(
                "Invalid Input",
                "Quantity must be greater than 0."
            )
            return

        subtotal = price * quantity
        discount_amount = subtotal * (discount / 100)
        final_price = subtotal - discount_amount

        result_label.config(
            text=f"Final Price: Rp {final_price:,.2f}"
        )

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter valid numbers."
        )


# Main window
root = tk.Tk()
root.title("Discount Calculator")
root.geometry("500x450")
root.resizable(False, False)

# Title
title_label = tk.Label(
    root,
    text="Discount Calculator",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=25)

# Original Price
tk.Label(
    root,
    text="Original Price:",
    font=("Arial", 12)
).pack()

price_entry = tk.Entry(
    root,
    width=25,
    font=("Arial", 12)
)
price_entry.pack(pady=5)

# Discount
tk.Label(
    root,
    text="Discount (%):",
    font=("Arial", 12)
).pack(pady=(10, 0))

discount_entry = tk.Entry(
    root,
    width=25,
    font=("Arial", 12)
)
discount_entry.pack(pady=5)

# Quantity
tk.Label(
    root,
    text="Quantity:",
    font=("Arial", 12)
).pack(pady=(10, 0))

quantity_entry = tk.Entry(
    root,
    width=25,
    font=("Arial", 12)
)
quantity_entry.pack(pady=5)

# Calculate button
calculate_button = tk.Button(
    root,
    text="Calculate",
    command=calculate_discount,
    font=("Arial", 12),
    padx=20,
    pady=5
)
calculate_button.pack(pady=20)

# Result
result_label = tk.Label(
    root,
    text="Final Price: Rp 0.00",
    font=("Arial", 14, "bold")
)
result_label.pack(pady=10)

root.mainloop()