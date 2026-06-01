# Task 09: Mini Inventory System (OOP + File I/O)
# Combines OOP and CSV file I/O to manage a product inventory with persistence.

import csv
from typing import Optional


class Product:
    """Represents a single product with a name, price, and quantity."""

    def __init__(self, name: str, price: float, quantity: int):
        self.name     = name
        self.price    = price
        self.quantity = quantity

    def __str__(self) -> str:
        return f"{self.name:<20} | Price: ₹{self.price:>8.2f} | Qty: {self.quantity}"


class Inventory:
    """Manages a collection of Product objects with CSV persistence."""

    def __init__(self):
        self.products: list[Product] = []

    def add_product(self, product: Product) -> None:
        """Adds a Product object to the inventory list."""
        self.products.append(product)
        print(f"Added: {product.name}")

    def total_value(self) -> float:
        """Returns the total inventory value — sum of (price × quantity) for all products."""
        return sum(p.price * p.quantity for p in self.products)

    def find_product(self, name: str) -> Optional[Product]:
        """Case-insensitive search — returns the Product if found, else None."""
        for p in self.products:
            if p.name.lower() == name.lower():
                return p
        return None

    def save_to_csv(self, filename: str) -> None:
        """Writes all products to a CSV file using DictWriter."""
        with open(filename, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["name", "price", "quantity"])
            writer.writeheader()
            for p in self.products:
                writer.writerow({"name": p.name, "price": p.price, "quantity": p.quantity})
        print(f"Inventory saved to '{filename}'.")

    @staticmethod
    def load_from_csv(filename: str) -> "Inventory":
        """
        Reads products from a CSV file and returns a populated Inventory object.
        """
        inventory = Inventory()
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                inventory.add_product(Product(row["name"], float(row["price"]), int(row["quantity"])))
        print(f"Inventory loaded from '{filename}'.")
        return inventory


# Test the inventory system 
if __name__ == "__main__":
    inv = Inventory()

    inv.add_product(Product("Laptop",       75000.00, 10))
    inv.add_product(Product("Wireless Mouse",  999.00, 50))
    inv.add_product(Product("USB-C Hub",      2499.00, 30))
    inv.add_product(Product("Keyboard",       4500.00, 20))
    inv.add_product(Product("Webcam",         3200.00, 15))

    print("\n Current Inventory ")
    for p in inv.products:
        print(p)

    print(f"\n Total Inventory Value: ₹{inv.total_value():,.2f}")

    print("\n Search Test ")
    found = inv.find_product("webcam")       # lowercase — tests case-insensitive search
    print(f"Found: {found}" if found else "Not found.")

    not_found = inv.find_product("Tablet")
    print(f"Found: {not_found}" if not_found else "'Tablet' not found — returns None ")

    print("\n Save & Reload ")
    inv.save_to_csv("inventory.csv")

    inv2 = Inventory.load_from_csv("inventory.csv")
    print(f"\n Total Inventory Value: ₹{inv2.total_value():,.2f}")

    ''' EXPLORE — @staticmethod vs @classmethod:
        - @staticmethod: belongs to the class but receives NO implicit first argument.
                         Used here because load_from_csv creates a brand-new Inventory
                         object itself — it doesn't need access to 'self' or 'cls'.
        - @classmethod:  receives 'cls' as the first argument (the class itself).
                         Useful when you want subclasses to return their own type,
                         e.g. SubInventory.load_from_csv() would still return SubInventory.
        For this use case, @staticmethod is clean and sufficient.'''