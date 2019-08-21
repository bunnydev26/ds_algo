# Program for array rotation
# Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements

def shitArray(arr, d, n):
    # storing the first d elements
    temp = arr[:d]
    print(temp)

    for index in range(d, n):
        arr[index-d] = arr[index]
    
    for index in range(d):
        arr[n-d+index] = temp[index]


def main():
    arr = [1, 2, 3, 4, 5, 6, 7]
    d = 2
    n = len(arr)
    print(arr)
    shitArray(arr, d, n)
    print(arr)

if __name__ == "__main__":
    main()