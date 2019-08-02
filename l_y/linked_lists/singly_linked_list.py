class Node:
    """
    This holds an individual Node of the list
    data: Stores the content
    next: Stores the Next node in the list
    """
    def __init__(self, data):
        self.data = data
        self.next: Node = None

class LinkedList:
    def __init__(self):
        self.__head: Node = None

    @property
    def head(self):
        return self.__head

    def is_list_empty(self):
        """
        Returns true if the list is empty.
        """
        return self.__head is None

    def append(self, data):
        """
        Appends a node in to the linked list at the end of the linked list
        """

        # Create the new node to be inserted
        node: Node = Node(data)

        if self.is_list_empty():
            self.__head = node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        
        last_node.next = node

    def prepend(self, data):
        """
        Prepends the node at the head
        """

        # Create the new node to be inserted
        node: Node = Node(data)
        # Make the new node point at the head
        node.next = self.__head
        # Make the new node as the head.
        self.__head = node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(f"{current_node.data} -> ", end=" ")
            current_node = current_node.next
        print("null")

if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append("A")
    linked_list.append("B")
    linked_list.append("C")
    linked_list.print_list()

    linked_list.prepend("D")
    
    linked_list.print_list()