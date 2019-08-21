import math
import sys

def jump_search(arr, element):
    length = len(arr)
    # print(length)
    # finding the block size to jump
    step = int(math.sqrt(length))
    # print(step)
    prev = 0

    while (arr[min(step, length) - 1] < element):
        prev = step
        step += int(math.sqrt(length))

        # there are no elements remaining to check for.
        if(prev >= length):
            return -1

    while(element < arr[step-1]):
        step -= 1
        if step == prev:
            return -1
    
    if(element == arr[step-1]):
        return step - 1
        
    return -1

def main():
    element = int(sys.argv[1])
    arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ] 

    for a in arr:
        print(jump_search(arr, a))

    # print(jump_search(arr, element))

if __name__ == "__main__":
    main()