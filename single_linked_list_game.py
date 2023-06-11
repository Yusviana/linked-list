class Item:
    def __init__(self, name, importance):
        self.name = name
        self.importance = importance
        self.next = None

class PlayerInventory:
    def __init__(self):
        self.head = None

    def add_item(self, name, importance):
        new_item = Item(name, importance)
        if self.head is None:
            self.head = new_item
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_item

    def remove_item(self, name):
        if self.head is None:
            print("Inventory is empty.")
            return
        if self.head.name == name:
            self.head = self.head.next
            print(f"Removed item: {name}")
            return
        current = self.head
        prev = None
        while current and current.name != name:
            prev = current
            current = current.next
        if current:
            prev.next = current.next
            print(f"Removed item: {name}")
        else:
            print(f"Item {name} not found in inventory.")

    def print_inventory(self):
        if self.head is None:
            print("Inventory is empty.")
        else:
            current = self.head
            while current:
                print("Item:", current.name)
                print("Importance:", current.importance)
                print("----------------------")
                current = current.next

inventory = PlayerInventory()

inventory.add_item("Sword", 5)
inventory.add_item("Potion", 3)
inventory.add_item("Shield", 7)
inventory.add_item("Key", 2)

inventory.print_inventory()

inventory.remove_item("Potion")

inventory.print_inventory()