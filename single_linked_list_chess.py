class Participant:
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating
        self.next = None

class Tournament:
    def __init__(self):
        self.head = None

    def register_participant(self, name, rating):
        new_participant = Participant(name, rating)
        if self.head is None:
            self.head = new_participant
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_participant

    def eliminate_participant(self, name):
        if self.head is None:
            print("No participants registered.")
            return
        if self.head.name == name:
            self.head = self.head.next
            print(f"Eliminated participant: {name}")
            return
        current = self.head
        prev = None
        while current and current.name != name:
            prev = current
            current = current.next
        if current:
            prev.next = current.next
            print(f"Eliminated participant: {name}")
        else:
            print(f"Participant {name} not found.")

    def print_participants(self):
        if self.head is None:
            print("No participants registered.")
        else:
            current = self.head
            while current:
                print("Participant:", current.name)
                print("Rating:", current.rating)
                print("----------------------")
                current = current.next

tournament = Tournament()

tournament.register_participant("Alice", 1500)
tournament.register_participant("Bob", 1800)
tournament.register_participant("Carol", 1650)
tournament.register_participant("Dave", 1550)

tournament.print_participants()

tournament.eliminate_participant("Carol")

tournament.print_participants()