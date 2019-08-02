from stack import Stack

class BalancedParanthesis(object):
    def __init__(self, paranthesis: str):
        self.__paranthesis = paranthesis
        self.__master_data = {
            "[": "]",
            "{": "}",
            "(": ")"
        }

    def is_matching_open_and_close_parantehsis(self, open_bracket: str, close_bracket: str):
        return self.__master_data[open_bracket] == close_bracket

    def is_balanced(self):
        stack = Stack()
        is_paranthesis_balanced = True
        for bracket in self.__paranthesis:
            if not is_paranthesis_balanced:
                break

            if bracket in self.__master_data.keys():
                stack.push(bracket)
            elif bracket in self.__master_data.values():
                if stack.is_empty():
                    is_paranthesis_balanced = False
                else:
                    open_bracket = stack.pop()
                    if not self.is_matching_open_and_close_parantehsis(open_bracket, bracket):
                        is_paranthesis_balanced = False                

        if not stack.is_empty():
            is_paranthesis_balanced = False    
            
        return is_paranthesis_balanced


if __name__ == "__main__":
    
    balanced_parantesis = BalancedParanthesis("[[[]]][[({[]})]]")
    print(balanced_parantesis.is_balanced())