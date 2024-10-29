import time
import math

# 1. Modified Linear Search to return all indices
def linear_search_all_indices(arr, target):
    indices = []
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            indices.append(i)
    return indices, comparisons  # Return all indices where target is found, and the number of comparisons

# 2. Binary Search to find insertion point
def binary_search_insertion_point(arr, target):
    left, right = 0, len(arr) - 1
    comparisons = 0
    
    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    # If target is not found, left is the insertion point
    return left, comparisons

# 3. Count comparisons in linear, binary, and jump searches
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    comparisons = 0
    
    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1, comparisons

# 4. Implement Jump Search
def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    comparisons = 0
    
    prev, current = 0, 0
    while current < n and arr[current] < target:
        comparisons += 1
        prev = current
        current += step
    
    # Linear search within block
    for i in range(prev, min(current, n)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
    return -1, comparisons

# Compare performance of all searches
def compare_search_algorithms(arr, target):
    # Linear Search
    start_time = time.time()
    linear_result, linear_comparisons = linear_search_all_indices(arr, target)
    linear_time = time.time() - start_time
    
    # Binary Search (on sorted array)
    arr_sorted = sorted(arr)
    start_time = time.time()
    binary_result, binary_comparisons = binary_search(arr_sorted, target)
    binary_time = time.time() - start_time
    
    # Jump Search (on sorted array)
    start_time = time.time()
    jump_result, jump_comparisons = jump_search(arr_sorted, target)
    jump_time = time.time() - start_time
    
    print(f"Linear Search: Found at indices {linear_result}, Comparisons: {linear_comparisons}, Time: {linear_time:.6f} seconds")
    print(f"Binary Search: Found at index {binary_result}, Comparisons: {binary_comparisons}, Time: {binary_time:.6f} seconds")
    print(f"Jump Search: Found at index {jump_result}, Comparisons: {jump_comparisons}, Time: {jump_time:.6f} seconds")

# Test with a sample list
test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_test_list = sorted(test_list)
target = 5

# Test Linear Search (modified)
indices, comparisons = linear_search_all_indices(test_list, target)
print(f"Modified Linear Search: Indices of {target} are {indices}, Comparisons: {comparisons}")

# Test Binary Search Insertion Point
insertion_point, comparisons = binary_search_insertion_point(sorted_test_list, 7)
print(f"Binary Search Insertion Point for 7: {insertion_point}, Comparisons: {comparisons}")

# Performance comparison
print("\nPerformance Comparison on Larger List:")
large_list = list(range(10000))
compare_search_algorithms(large_list, 8888)
