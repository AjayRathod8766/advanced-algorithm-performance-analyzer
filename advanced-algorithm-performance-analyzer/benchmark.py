import time
import random
from algorithms import bubble_sort, insertion_sort, merge_sort, quick_sort

def benchmark():
    size = 100000
    data = [random.randint(1, 100000) for _ in range(size)]

    algorithms = {
        "Bubble Sort (1k sample)": lambda arr: bubble_sort(arr[:1000]),
        "Insertion Sort (1k sample)": lambda arr: insertion_sort(arr[:1000]),
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort,
    }

    results = {}

    for name, func in algorithms.items():
        arr_copy = data.copy()
        start = time.time()
        func(arr_copy)
        duration = round(time.time() - start, 4)
        results[name] = duration

    print("\nAlgorithm Performance Benchmark (Dataset size: 100,000)")
    print("-" * 55)
    for name, time_taken in results.items():
        print(f"{name:<30} {time_taken} seconds")

if __name__ == "__main__":
    benchmark()
