# Recursive approach
# Program for array rotation
# Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements

def reverseArray(arr, start_index, end_index):
    while(start_index < end_index):
        print(start_index, end_index)
        arr[start_index], arr[end_index] = arr[end_index], arr[start_index]
        start_index += 1
        end_index -= 1

def shiftArray(arr, n, d):
    """
    This method will shift the array with a given d count.
    """
    # Reverse the First Array 
    reverseArray(arr, 0, d-1)
    print(arr[:d])
    # Reverse the second half of the array
    reverseArray(arr, d, n-1)
    print(arr[d:])
    # Reverse the whole array.
    reverseArray(arr, 0, n-1)

def main():
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    d = 2
    n = len(arr)
    print(arr)
    shiftArray(arr, n, d)
    print(arr)

if __name__ == "__main__":
    main()