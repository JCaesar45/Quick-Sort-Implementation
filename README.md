```markdown
# Quick Sort Implementation

## Overview
This project implements the Quick Sort algorithm in Python. Quick Sort is a highly efficient sorting algorithm that uses the divide-and-conquer approach to sort a list of integers. It recursively partitions the list into sublists based on a pivot element, then combines the sorted sublists to produce a fully sorted list.

## Features
- Sorts a list of integers from least to greatest
- Does not modify the original input list
- Uses recursion for sorting sublists
- Does not rely on Python's built-in sorting functions

## How It Works
1. **Choose a Pivot:** The algorithm selects the last element of the list as the pivot.
2. **Partition:** The list is partitioned into three sublists:
   - Elements less than the pivot
   - Elements equal to the pivot
   - Elements greater than the pivot
3. **Recursion:** The 'less' and 'greater' sublists are sorted recursively using the same process.
4. **Concatenate:** The sorted sublists are concatenated to form the final sorted list.

## Usage
To use the `quick_sort` function, simply pass a list of integers as an argument:

```python
unsorted_list = [20, 3, 14, 1, 5]
sorted_list = quick_sort(unsorted_list)
print(sorted_list)  # Output: [1, 3, 5, 14, 20]
``

## Example
```python
print(quick_sort([83, 4, 24, 2]))
# Output: [2, 4, 24, 83]
``

## Requirements
- Python 3.x

## Notes
- The function returns a new sorted list and leaves the original list unchanged.
- The implementation avoids using Python's built-in `sorted()` or `sort()` functions to meet project constraints.

## License
This project is open-source and free to use.
