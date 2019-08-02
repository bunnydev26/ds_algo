class Stack(object):
    def __init__(self) -> None:
        self.__items: list = []

    def push(self, item) -> None:
        """
        Push the item to the stack
        """
        self.__items.append(item)

    def is_empty(self) -> bool:
        """
        Returns true if the stack is empty and has no elements
        """
        return self.__items == []

    def pop(self):
        """
        Removes the element from the top of the stack and returns if it has an element
        """
        if not self.is_empty():
            return self.__items.pop()

    def peek(self):
        if not self.is_empty():
            return self.__items[-1]

    def show_items(self):
        return self.__items

if __name__ == "__main__":
    stack = Stack()
    stack.push("A")
    stack.push("B")
    stack.push("C")
    stack.push("D")
    print(stack.show_items())
    stack.pop()
    print(stack.show_items())