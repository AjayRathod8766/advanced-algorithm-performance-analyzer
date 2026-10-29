# Advanced Algorithm Performance Analyzer

A Python project for benchmarking and comparing common sorting algorithms on large datasets. It is designed to demonstrate algorithmic thinking, performance analysis, and clean benchmarking practices in a professional, easy-to-run project structure.

## Overview

This repository measures execution time for several sorting algorithms, including:
- Bubble Sort
- Insertion Sort
- Merge Sort
- Quick Sort

The project focuses on analyzing performance on datasets up to 100,000 elements and presenting the results in a clear benchmark table.

## Features

- Compares multiple sorting algorithms side by side
- Evaluates performance using real execution timing
- Maintains a modular separation between algorithm logic and benchmarking code
- Uses a simple CLI so the project can be run locally in seconds
- Suitable for algorithm studies, coursework, and technical portfolio demos

## Project Structure

```text
advanced-algorithm-performance-analyzer/
├── algorithms.py         # Sorting algorithm implementations
├── benchmark.py          # Benchmark runner and reporting logic
├── README.md             # Project-specific documentation
├── .gitignore            # Python project hygiene
├── LICENSE               # MIT license
├── pyproject.toml        # Python project metadata
└── CONTRIBUTING.md       # Contribution guidelines
```

## Installation

```bash
git clone https://github.com/AjayRathod8766/advanced-algorithm-performance-analyzer.git
cd advanced-algorithm-performance-analyzer
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
python benchmark.py
```

## Usage

Run the benchmark directly:

```bash
python benchmark.py
```

Optional arguments are supported for custom dataset size and value range:

```bash
python benchmark.py --size 200000 --min-value 1 --max-value 100000
```

## Example Output

```text
Algorithm Performance Benchmark (Dataset size: 100,000)
-------------------------------------------------------
Bubble Sort (sample: 1000)    0.0412 seconds
Insertion Sort (sample: 1000) 0.0298 seconds
Merge Sort                   0.0165 seconds
Quick Sort                   0.0112 seconds
```

## Time Complexity

| Algorithm | Best Case | Average Case | Worst Case |
| --- | --- | --- | --- |
| Bubble Sort | O(n) | O(n²) | O(n²) |
| Insertion Sort | O(n) | O(n²) | O(n²) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) |

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing

Contributions are welcome. Please read CONTRIBUTING.md before submitting changes.
