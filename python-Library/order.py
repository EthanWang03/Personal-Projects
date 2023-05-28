from book import Book

class Order:
    def __init__(self, books=None):
        self.books = books or []
        self.total_cost = 0.0

    def add_book(self,book,quantity):
        # Add book to order 
        self.books.append((book,quantity))
        self.total_cost += book.price * quantity

    def add_book(self,book):
        # Add book to order 
        self.books.append((book,1))
        self.total_cost += book.price * 1

    def remove_book(self, book):
        # Remove the specified book from the order
        for item in self.books:
            if item[0] == book:
                self.total_cost -= item[0].price * item[1]
                self.books.remove(item)
                break

    def generate_confirmation(self):
        # Generate an order confirmation string
        confirmation = "Order Confirmation:\n"
        for book, quantity in self.books:
            confirmation += f"{book.title} x{quantity}\n"
        confirmation += f"Total cost: ${self.total_cost:.2f}\n"
        return confirmation