from stack import Stack

class DecimalToBinary(object):
    def __init__(self, decimal_number):
        self.__decimal_number: int = decimal_number
        self.__binary_number: str = ""

        self.__convert_decimal_to_binary()
    
    def __convert_decimal_to_binary(self):
        stack: Stack = Stack()
        decimal_number = self.__decimal_number

        while decimal_number > 0:
            # getting the remainder to add to binary result
            remainder = decimal_number % 2
            # Pushing the result to the stack
            stack.push(remainder)
            # divide the number as we have already got the binary value for that digit
            decimal_number = decimal_number // 2
        
        # constructing the binary result
        while not stack.is_empty():
            self.__binary_number += str(stack.pop())

    def __str__(self):
        return self.__binary_number

if __name__ == "__main__":
    print(DecimalToBinary(251))

    print(DecimalToBinary(5))