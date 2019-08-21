from stack import Stack

def print_nge(numbers_list):
    s = Stack()
    s.push(numbers_list[0])

    for i in range(1, len(numbers_list)):
        print(numbers_list[i], end=" ")


if __name__ == "__main__":
    a = [12, 8, 15, 6, 20, 4]
    print(a)
    print_nge(a)
    print()