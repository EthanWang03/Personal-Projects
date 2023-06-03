<<<<<<< HEAD
class Book:
    def __init__(self,title,author,genre,price):
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price

    def title(self):
        return self.title
    
    def author(self):
        return self.author
    
    def genre(self):
        return self.genre
    
    def price(self):
        return self.price

    def __str__(self):
=======
class Book:
    def __init__(self,title,author,genre,price):
        self.title = title
        self.author = author
        self.genre = genre
        self.price = price

    def title(self):
        return self.title
    
    def author(self):
        return self.author
    
    def genre(self):
        return self.genre
    
    def price(self):
        return self.price

    def __str__(self):
>>>>>>> 792524879c874e809fa7c08a6cc1769418bc7759
        return f"{self.title} by {self.author}"