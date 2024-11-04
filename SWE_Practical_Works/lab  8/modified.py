import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Generator-based Quick Sort for Visualization
def quick_sort_visual(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        pivot_index = partition(arr, low, high)
        yield arr
        yield from quick_sort_visual(arr, low, pivot_index - 1)
        yield from quick_sort_visual(arr, pivot_index + 1, high)

# Partition function for Quick Sort
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Generator-based Hybrid Quick Sort for Visualization
def hybrid_quick_sort_visual(arr, low=0, high=None, threshold=10):
    if high is None:
        high = len(arr) - 1

    while low < high:
        if high - low < threshold:
            yield from insertion_sort_visual(arr, low, high)
            break
        else:
            pivot_index = partition(arr, low, high)
            yield arr
            if pivot_index - low < high - pivot_index:
                yield from hybrid_quick_sort_visual(arr, low, pivot_index - 1, threshold)
                low = pivot_index + 1
            else:
                yield from hybrid_quick_sort_visual(arr, pivot_index + 1, high, threshold)
                high = pivot_index - 1

# Insertion Sort for Hybrid Quick Sort Visualization
def insertion_sort_visual(arr, low, high):
    for i in range(low + 1, high + 1):
        key = arr[i]
        j = i - 1
        while j >= low and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        yield arr

# Visualization function
def visualize_sort(arr, sort_func):
    fig, ax = plt.subplots()
    ax.set_title(f"{sort_func.__name__} Visualization")
    bar_rects = ax.bar(range(len(arr)), arr, align="edge")

    def update_graph(arr, rects):
        for rect, val in zip(rects, arr):
            rect.set_height(val)

    def generator():
        for step in sort_func(arr.copy()):
            yield step

    ani = animation.FuncAnimation(fig, func=update_graph, fargs=(bar_rects,),
                                  frames=generator, repeat=False)
    plt.show()

# Visualizing Bubble Sort
def bubble_sort_visual(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                yield arr
        if not swapped:
            break

# Example usage
test_arr = [64, 34, 25, 12, 22, 11, 90]
visualize_sort(test_arr, bubble_sort_visual)  # Can change this to quick_sort_visual or hybrid_quick_sort_visual
