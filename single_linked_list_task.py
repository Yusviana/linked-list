class Node:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_task(self, description, priority):
        new_node = Node(description, priority)
        if self.head is None:
            self.head = new_node
        else:
            if priority > self.head.priority:
                new_node.next = self.head
                self.head = new_node
            else:
                current = self.head
                while current.next is not None and priority <= current.next.priority:
                    current = current.next
                new_node.next = current.next
                current.next = new_node

    def remove_task(self, description):
        if self.head is None:
            print("Daftar tugas kosong.")
            return

        if self.head.description == description:
            self.head = self.head.next
            print("Tugas '" + description + "' dihapus.")
            return

        current = self.head
        while current.next is not None and current.next.description != description:
            current = current.next

        if current.next is None:
            print("Tugas tidak ditemukan.")
        else:
            current.next = current.next.next
            print("Tugas '" + description + "' dihapus.")

    def print_tasks(self):
        if self.head is None:
            print("Daftar tugas kosong.")
            return

        current = self.head
        print("Daftar tugas:")
        while current is not None:
            print("Deskripsi:", current.description)
            print("Prioritas:", current.priority)
            print("-------------------------")
            current = current.next


# Contoh penggunaan program

# Membuat objek linked list
task_list = LinkedList()

# Menambahkan tugas baru
task_list.add_task("Mengerjakan laporan", 2)
task_list.add_task("Membayar tagihan", 1)
task_list.add_task("Membeli bahan makanan", 3)
task_list.add_task("Menyapu rumah", 2)

# Mencetak daftar tugas
task_list.print_tasks()

# Menghapus tugas
task_list.remove_task("Membayar tagihan")

# Mencetak daftar tugas setelah penghapusan
task_list.print_tasks()