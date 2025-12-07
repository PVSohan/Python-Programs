import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def measure_time(func, arr):
    start_time = time.time()
    func(arr)
    end_time = time.time()
    return end_time - start_time

# Original array
arr = [23, 45, 89, 44, 12, 87, 90, 65, 54, 75, 10, 32]

# Iterate through elements in `arr` and measure time for sorting a reversed list of that size
for array_size in arr:
    test_arr = list(range(array_size, 0, -1))
    duration = measure_time(bubble_sort, test_arr)
    sort_order = bubble_sort(test_arr)
    print(f"Time taken to sort an array of size {array_size}: {duration:.5f} seconds")
