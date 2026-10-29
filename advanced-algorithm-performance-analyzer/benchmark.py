"""Benchmark runner for comparing sorting algorithm performance."""

from __future__ import annotations

import argparse
import random
import time
from typing import Callable

from algorithms import bubble_sort, insertion_sort, merge_sort, quick_sort


def generate_dataset(size: int, minimum: int, maximum: int) -> list[int]:
    """Generate a random integer dataset within a bounded range."""
    return [random.randint(minimum, maximum) for _ in range(size)]


def benchmark_algorithm(name: str, func: Callable[[list[int]], list[int]], data: list[int]) -> tuple[str, float, int]:
    """Measure and return execution time for a given sorting function."""
    start = time.perf_counter()
    sorted_data = func(data.copy())
    elapsed = time.perf_counter() - start

    if sorted_data != sorted(data):
        raise ValueError(f"{name} did not sort the dataset correctly.")

    return name, elapsed, len(data)


def run_benchmark(size: int = 100_000, minimum: int = 1, maximum: int = 100_000) -> list[tuple[str, float, int]]:
    """Run the benchmark suite for all sorting algorithms."""
    dataset = generate_dataset(size, minimum, maximum)

    algorithms = [
        ("Bubble Sort", bubble_sort, min(size, 1_000)),
        ("Insertion Sort", insertion_sort, min(size, 1_000)),
        ("Merge Sort", merge_sort, size),
        ("Quick Sort", quick_sort, size),
    ]

    results = []
    for name, func, sample_size in algorithms:
        sample = dataset[:sample_size]
        results.append(benchmark_algorithm(name, func, sample))

    return sorted(results, key=lambda item: item[1])


def main() -> None:
    """CLI entry point for the benchmark tool."""
    parser = argparse.ArgumentParser(description="Benchmark sorting algorithm performance.")
    parser.add_argument("--size", type=int, default=100_000, help="Dataset size to test.")
    parser.add_argument("--min-value", type=int, default=1, help="Minimum random value.")
    parser.add_argument("--max-value", type=int, default=100_000, help="Maximum random value.")
    args = parser.parse_args()

    results = run_benchmark(args.size, args.min_value, args.max_value)

    print(f"\nAlgorithm Performance Benchmark (Dataset size: {args.size:,})")
    print("-" * 60)
    for name, duration, sample_size in results:
        label = f"{name} (sample: {sample_size:,})" if sample_size < args.size else name
        print(f"{label:<30} {duration:.6f} seconds")


if __name__ == "__main__":
    main()
