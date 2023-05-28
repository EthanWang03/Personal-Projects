from book import Book
from order import Order
from shoppingCart import ShoppingCart

# Create book instances
book1 = Book("Python Crash Course", "Eric Matthes", "Programming", 29.99)
book2 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction", 14.99)
book3 = Book("Data Science for Beginners", "John Smith", "Data Science", 39.99)

# Create an order instance
order = Order()
order.add_book(book1)
order.add_book(book2)
order.remove_book(book1)

# Create a shopping cart instance
cart = ShoppingCart()
cart.add_book(book2)
cart.add_book(book3)

# Display order confirmation
print(order.generate_confirmation())

# Display shopping cart contents
cart.display_contents()
print(f"Total Price: ${cart.calculate_total_price():.2f}\n")
