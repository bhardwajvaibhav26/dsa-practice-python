# DSA Practice (Python)

Practice repo for learning DSA by **pattern** — each folder is one technique. When you see a problem, you should know which folder (and approach) to use.

Problem list with links: **[PROBLEMS.md](PROBLEMS.md)** (NeetCode 250 + basics)

## How to use

1. Open `PROBLEMS.md`, pick a problem, read it on LeetCode
2. Name the pattern before you code
3. Save your solution in the matching folder as `problem_name.py`
4. Check off the problem in `PROBLEMS.md`

## Folders

| Folder | Pattern |
|--------|---------|
| `basics/star_patterns` | Print `*` shapes with nested loops |
| `basics/loops` | Loop and condition warm-ups |
| `basics/math` | Basic number/math problems |
| `arrays` | Hashing, arrays, prefix sums |
| `two_pointers` | Sorted array pairs, palindromes |
| `sliding_window` | Contiguous subarray / substring |
| `stack` | Parentheses, monotonic stack |
| `binary_search` | Search sorted data |
| `linked_list` | Reverse, merge, cycle |
| `trees` | DFS, BFS, BST, tries |
| `graphs` | BFS, DFS, shortest path |
| `backtracking` | Subsets, permutations, combinations |
| `dynamic_programming` | 1-D and 2-D DP |
| `greedy` | Greedy, intervals, heap |
| `math` | Geometry, bit manipulation |

## Solution file format

```python
"""
Problem: Two Sum
Pattern: arrays / hashing
Link: https://leetcode.com/problems/two-sum/
"""

def two_sum(nums: list[int], target: int) -> list[int]:
    ...

if __name__ == "__main__":
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
```

For star patterns, use `Topic: star_patterns` instead of `Pattern:` and skip the LeetCode link if there isn't one.
