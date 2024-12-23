def max_heapify(arr, n, i):
    """
    Ensures the heap property for the subtree rooted at index i.
    """
    largest = i 
    left = 2 * i + 1 
    right = 2 * i + 2  
    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

def build_max_heap(arr):
    """
    Builds a max-heap from the input array.
    """
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)

def heap_sort(arr):
    """
    Sorts an array using the Heap-Sort algorithm.
    """
    n = len(arr)
    build_max_heap(arr)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        max_heapify(arr, i, 0)

# Example Usage
numbers = [4, 10, 3, 5, 1]
print("Original Array:", numbers)
heap_sort(numbers)
print("Sorted Array:", numbers)
