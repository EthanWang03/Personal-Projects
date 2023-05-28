from book import Book

class ShoppingCart:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def calculate_total_price(self):
        total_price = 0.0
        for book in self.books:
            total_price += book.price
        return total_price

    def display_contents(self):
        confirmation = ""
        if not self.books:
            confirmation += "The shopping cart is empty."
        else:
            total_price = 0.0
            confirmation += "Shopping Cart Contents:\n"
            for book in self.books:
                confirmation += f"- {book}\n"
                total_price += book.price
            confirmation += f"Total cost: ${total_price:.2f}\n"
        return confirmation
            

    def empty_cart(self):
        self.books = []
