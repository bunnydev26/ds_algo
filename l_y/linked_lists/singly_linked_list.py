class Node:
    """
    This holds an individual Node of the list
    data: Stores the content
    next: Stores the Next node in the list
    """
    def __init__(self, data):
        self.data = data
        self.next: Node = None

    def __str__(self):
        return self.data

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

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node is not there")
            return
        
        new_node = Node(data)
        curr_node = self.__head
        
        while curr_node and curr_node.data != prev_node.data:
            curr_node = curr_node.next
            continue
        
        new_node.next = curr_node.next
        curr_node.next = new_node

    def delete_node(self, key):

        curr_node = self.__head
        # Case 1 when the head node is to be deleted.
        if not self.is_list_empty() and self.__head.data == key:
            self.__head = curr_node.next
            del curr_node
            return

        # Case 2 when the node to be deleted is not head.
        prev_node = None
        curr_node = self.__head

        # As long as we have a node and we do not find a match. 
        while curr_node and curr_node.data != key:
            prev_node = curr_node
            curr_node = curr_node.next
       
        # We did not find the elemnt if the prev.next is not empty
        if curr_node is None:
            print(f"Did not find any node having data {key}")
            return

        # Assigining the previous node reverence to the next node of current. 
        prev_node.next = curr_node.next

        del curr_node

    def delete_node_at_position(self, position):
        # If the list is empty we cannot perform any deletion.
        if self.is_list_empty():
            print("List is empty cannot perform deletion")
        
        # Case 1 delete the head element at the head position
        curr_node = self.__head
        if position == 0:
            self.__head = curr_node.next
            del curr_node
            return

        # Case 2 any other postion.
        prev_node = None
        index = 0
        while curr_node and index != position:
            # print(curr_node.data)
            prev_node = curr_node
            curr_node = curr_node.next
            index += 1

        if curr_node is None:
            print(f"There is no node at the position {position}")
        prev_node.next = curr_node.next
        del curr_node

    def len_iterative(self):
        count = 0
        curr_node = self.__head
        while curr_node:
            curr_node = curr_node.next
            count += 1

        return count

    def len_recursive(self, curr_node):
        """
        Calculate the length of the linked list via recurisve method
        """

        # base condition for the recurssion.
        if curr_node is None:
            return   0
        # Calculating the length.
        return self.len_recursive(curr_node.next) + 1

    def __get_node(self, key):
        curr_node = self.__head
        prev_node = None
        while curr_node and curr_node.data != key:
            prev_node = curr_node
            curr_node = curr_node.next
        
        return prev_node, curr_node

    def swap_two_nodes(self, key1, key2):
        if key1 == key2:
            return
        
        prev_node_with_key1, curr_node_with_key1 = self.__get_node(key1)
        prev_node_with_key2, curr_node_with_key2 = self.__get_node(key2)
        
        if curr_node_with_key1 is None or curr_node_with_key2 is None:
            return

        # if curr_node_with_key1 is not a head
        if prev_node_with_key1:
            prev_node_with_key1.next = curr_node_with_key2
        else:
            self.__head = curr_node_with_key2

        # if curr_node_with_key2 is not a head
        if prev_node_with_key2:
            prev_node_with_key2.next = curr_node_with_key1
        else:
            self.__head = curr_node_with_key1

        curr_node_with_key1.next, curr_node_with_key2.next = curr_node_with_key2.next, curr_node_with_key1.next

    def reverse_list(self):
        prev_node, curr_node = None, self.__head
        while curr_node:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        
        self.__head = prev_node

    def reverse_list_recursive(self):
        # method internally.
        def _reverse_list_recurisve(curr, prev):
            if curr is None:
                return prev
            # store the next node of the current
            next_node = curr.next
            # Point the current node to the previous node
            curr.next = prev
            # Make the current node as prev
            prev = curr
            # make the current node as the next node
            curr = next_node
            # return the reverse list
            return _reverse_list_recurisve(curr, prev)
            

        self.__head = _reverse_list_recurisve(self.head, prev=None)


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.append("A")
    linked_list.append("B")
    linked_list.append("C")
    linked_list.print_list()

    linked_list.prepend("D")
    
    linked_list.print_list()
    linked_list.insert_after_node(Node("B"), "E")

    linked_list.print_list()

    print(linked_list.len_iterative())

    print(linked_list.len_recursive(linked_list.head))

    linked_list.swap_two_nodes("D", "B")
    linked_list.print_list()
    print("Reversing..")
    linked_list.reverse_list()
    linked_list.print_list()
    linked_list.reverse_list_recursive()
    linked_list.print_list()
    # linked_list.delete_node("E")
    # linked_list.print_list()
    # linked_list.delete_node("D")
    # linked_list.print_list()
    
    # linked_list.delete_node_at_position(1)
    # linked_list.print_list()


    # linked_list.delete_node_at_position(0)
    # linked_list.print_list()
    