# Topic 14 Collaborative Assignment
# Your Name:Troy Post
# Date: 7/26/2026

# --- PROVIDED CODE: Do not modify this section ---
class LibraryItem:
    """Base class for all items in the library catalog."""
    def __init__(self, title, year):
        self.title = title
        self.year = year

    def describe(self):
        return f"{self.title} ({self.year})"

    def item_type(self):
        return "Library Item"

class Book(LibraryItem):
    """A book in the library catalog."""
    def __init__(self, title, year, author):
        super().__init__(title, year)
        self.author = author

    def describe(self):
        return f"{self.title} by {self.author} ({self.year})"

    def item_type(self):
        return "Book"

def count_items(catalog, index=0):
    """Recursively count items in a catalog list."""
    if index == len(catalog):
        return 0
    return 1 + count_items(catalog, index + 1)

# --- Sample usage of provided code ---
book1 = Book("The Pragmatic Programmer", 1999, "Hunt & Thomas")
print(book1.describe())
print("Type:", book1.item_type())
catalog = [book1]
print("Items in catalog:", count_items(catalog))

# --- YOUR CODE BELOW THIS LINE ---

# DVD subclass inheriting from LibraryItem
class DVD(LibraryItem):
    def __init__(self, title, year, director, runtime):
        super().__init__(title, year)
        self.director = director
        self.runtime = runtime

    def describe(self):
        return f"{self.title} directed by {self.director} ({self.year}) - {self.runtime} mins"

    def item_type(self):
        return "DVD"


# Magazine subclass inheriting from LibraryItem
class Magazine(LibraryItem):
    def __init__(self, title, year, issue_number):
        super().__init__(title, year)
        self.issue_number = issue_number

    def describe(self):
        return f"{self.title} - Issue #{self.issue_number} ({self.year})"

    def item_type(self):
        return "Magazine"


# Create new items
movie = DVD("Inception", 2010, "Christopher Nolan", 148)
mag = Magazine("National Geographic", 2023, 512)

# Add them to catalog
catalog.append(movie)
catalog.append(mag)

print("\n--- Updated Catalog ---")

# Demonstrating polymorphism
for item in catalog:
    print(item.item_type() + ": " + item.describe())

# Call count_items again to check total
print("\nTotal items now:", count_items(catalog))
