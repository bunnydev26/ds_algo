# Rotate one by one
# Program for array rotation
# Write a function rotate(ar[], d, n) that rotates arr[] of size n by d elements


def leftRotateByOne(arr, n):
    temp = arr[0]
    for index in range(n-1):
        arr[index] = arr[index+1]
    arr[n-1] = temp

def leftRotate(arr, n, d):
    for _ in range(d):
        leftRotateByOne(arr, n)


def main():
    arr = [1, 2, 3, 4, 5, 6, 7]
    d = 2
    n = len(arr)
    print(arr)
    leftRotate(arr, n, d)
    print(arr)

if __name__ == "__main__":
    main()