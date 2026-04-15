def main():
    arr = [10, 15, 5, 20, 0]
    insertion_sort(arr)
    print(arr)

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def insert(arr, i):
    for j in range(i, 0, -1):
        if arr[j-1]  > arr[j]:
            swap(arr, j-1,j)
        else:
            break

def insertion_sort(arr):
    for j in range(len(arr)):
        insert(arr,j)



if __name__ == "__main__":
    main()