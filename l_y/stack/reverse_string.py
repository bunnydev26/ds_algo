from stack import Stack

def reverse_string(some_string):
    """
    This method will reverse the string
    ::: param some_string
    :: return Reversed string
    """

    reverse_string: str = ""
    stack = Stack()
    # Traverse through every letter in the word and push it to the stack
    for string in some_string:
        stack.push(string)
    
    # Pop the every element and append it to the string.
    while not stack.is_empty():
        reverse_string += stack.pop()
    
    return reverse_string

if __name__ == "__main__":
    print(reverse_string("amit"))
    print(reverse_string("tanishka"))