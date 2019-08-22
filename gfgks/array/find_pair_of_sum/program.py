# This program will give a pair of two numbers which will total to the sum.

import sys

def sum_pair_brute_force_method(arr, element):
    for index, first_item in enumerate(arr):
        for second_item in arr[index:]:
            if (first_item + second_item) == element:
                print(first_item, second_item)
                return True
    return False

def sum_pair_using_hash_table(arr, element):
    hash_table = {}
    for item in arr:
        if item in hash_table:
            print(hash_table[item], item)
            return True
        hash_table[element-item] = item
    return False

def sum_pair(arr, element):
    length = len(arr) - 1
    index = 0
    while(index < length):
        if (arr[index] + arr[length]) == element:
            print(arr[index], arr[length])
            return True
        elif ((arr[index] + arr[length]) < element):
            index += 1
        else:
            length -= 1

    return False

def main():
    element = int(sys.argv[1])
    arr = [-2, 3, 4 , 7, 8, 10, 13, 15]
    n = len(arr)
    
    # print(sum_pair_brute_force_method(arr, element))
    # print(sum_pair_using_hash_table(arr, element))
    print(sum_pair(arr, element))
    
if __name__ == "__main__":
    main()