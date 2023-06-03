import tkinter as tk
from book import Book
from order import Order
from shoppingCart import ShoppingCart
from tkinter import messagebox

# Create book instances
book1 = Book("Python Crash Course", "Eric Matthes", "Programming", 29.99)
book2 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 14.99)
book3 = Book("Data Science for Beginners", "John Smith", "Data Science", 39.99)

# Create a shopping cart instance
cart = ShoppingCart()

def add_to_cart(book):
    cart.add_book(book)
    update_cart_label()

def remove_from_cart(book):
    cart.remove_book(book)
    update_cart_label()

def place_order():
    order = Order()
    for book in cart.books:
        order.add_book(book)
    order_confirmation = order.generate_confirmation()
    messagebox.showinfo("Order Confirmation", order_confirmation)
    cart.empty_cart()
    update_cart_label()

def show_cart_contents():
    contents = cart.display_contents()
    if not contents:
        contents = "The cart is empty."
    messagebox.showinfo("Shopping Cart", contents)

def update_cart_label():
    cart_label.config(text=f"Shopping Cart ({len(cart.books)} items)")

def clear_cart():
    cart.empty_cart()
    update_cart_label()

# Create the main window
window = tk.Tk()
window.title("Online Bookstore")
window.geometry("400x400")

# Create and configure UI elements
title_label = tk.Label(window, text="Welcome to the Online Bookstore", font=("Arial", 16))
title_label.pack(pady=10)

# Create book frames
book_frame = tk.Frame(window)
book_frame.pack(pady=10)

book1_label = tk.Label(book_frame, text=book1.title, font=("Arial", 12))
book1_label.grid(row=0, column=0, padx=10)
book1_button = tk.Button(book_frame, text="Add to Cart", command=lambda: add_to_cart(book1))
book1_button.grid(row=0, column=1, padx=10)

book2_label = tk.Label(book_frame, text=book2.title, font=("Arial", 12))
book2_label.grid(row=1, column=0, padx=10)
book2_button = tk.Button(book_frame, text="Add to Cart", command=lambda: add_to_cart(book2))
book2_button.grid(row=1, column=1, padx=10)

book3_label = tk.Label(book_frame, text=book3.title, font=("Arial", 12))
book3_label.grid(row=2, column=0, padx=10)
book3_button = tk.Button(book_frame, text="Add to Cart", command=lambda: add_to_cart(book3))
book3_button.grid(row=2, column=1, padx=10)

# Create shopping cart frame
cart_frame = tk.Frame(window)
cart_frame.pack(pady=10)

cart_label = tk.Label(cart_frame, text="Shopping Cart", font=("Arial", 14, "bold"))
cart_label.grid(row=0, column=0, columnspan=2, pady=5)

cart_items_label = tk.Label(cart_frame, text="", font=("Arial", 12))
cart_items_label.grid(row=1, column=0, columnspan=2, pady=5)

show_cart_button = tk.Button(cart_frame, text="Show Cart", command=show_cart_contents)
show_cart_button.grid(row=2, column=0, pady=5)

order_button = tk.Button(cart_frame, text="Place Order", command=place_order)
order_button.grid(row=2, column=1, pady=5)

clear_button = tk.Button(cart_frame, text="Clear Cart", command=clear_cart)
clear_button.grid(row=3, column=0, columnspan=2, pady=5)

# Update the cart label initially
update_cart_label()

# Start the main event loop
window.mainloop()


