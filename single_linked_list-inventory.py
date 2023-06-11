
class Product:
    def __init__(self, name, code, stock):
        self.name = name
        self.code = code
        self.stock = stock
        self.next = None

class InventoryManagement:
    def __init__(self):
        self.head = None

    def add_product(self, name, code, stock):
        new_product = Product(name, code, stock)
        if self.head is None:
            self.head = new_product
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_product

    def remove_product(self, code):
        if self.head is None:
            print("Inventory is empty.")
            return
        if self.head.code == code:
            self.head = self.head.next
            print(f"Removed product with code: {code}")
            return
        current = self.head
        prev = None
        while current and current.code != code:
            prev = current
            current = current.next
        if current:
            prev.next = current.next
            print(f"Removed product with code: {code}")
        else:
            print(f"Product with code {code} not found in inventory.")

    def print_inventory(self):
        if self.head is None:
            print("Inventory is empty.")
        else:
            current = self.head
            while current:
                print("Product:", current.name)
                print("Code:", current.code)
                print("Stock:", current.stock)
                print("----------------------")
                current = current.next

inventory = InventoryManagement()

inventory.add_product("Keyboard", "KB001", 10)
inventory.add_product("Mouse", "MS001", 20)
inventory.add_product("Monitor", "MN001", 5)
inventory.add_product("Printer", "PR001", 3)

inventory.print_inventory()

inventory.remove_product("MN001")

inventory.print_inventory()