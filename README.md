# DSA Practice (Python)

Pattern-based DSA practice repo. Problems are grouped by **technique**, not random order — so when you see a question, you know which folder (and mental model) to use.

## How to use

1. Open **[PROBLEMS.md](PROBLEMS.md)** — pick a problem, check it off when done.
2. Pick a topic from the roadmap below.
3. Open solved problems in that folder — read the header (`Pattern`, `When to use`).
4. Add your solution in the **same folder** using the file template.
5. Blind review: read only the problem statement, name the pattern, then check your solution.

Optional: add a `notes.md` inside any topic folder when you want to capture tricks or mistakes.

## Learning order

| Order | Folder | What you practice |
|-------|--------|-------------------|
| 1 | `basics/star_patterns` | Print shapes with `*` using nested loops |
| 2 | `basics/loops` | Loop patterns, conditions |
| 3 | `basics/math` | Basic math and number tricks |
| 4 | `arrays` | Array traversal, hashing |
| 5 | `two_pointers` | Left/right pointers on sorted or paired data |
| 6 | `sliding_window` | Contiguous subarray/substring windows |
| 7 | `stack` | LIFO, monotonic stack |
| 8 | `binary_search` | Search on sorted data or answer space |
| 9 | `linked_list` | Pointer manipulation on lists |
| 10 | `trees` | DFS, BFS on trees |
| 11 | `graphs` | Graph traversal, shortest path |
| 12 | `backtracking` | Try choices, undo (combinations, permutations) |
| 13 | `dynamic_programming` | Overlapping subproblems, optimal substructure |
| 14 | `greedy` | Local optimal choices |
| 15 | `math` | Advanced math / geometry |

## Pattern signals (starter cheat sheet)

Expand this table as you learn more patterns.

| If the problem mentions… | Think pattern | Folder |
|--------------------------|---------------|--------|
| print shape with stars, nested loops | star pattern | `basics/star_patterns` |
| count / find in array, need fast lookup | hashing | `arrays` |
| sorted array, pair or triplet sum | two pointers | `two_pointers` |
| palindrome check on string/array | two pointers | `two_pointers` |
| contiguous subarray, fixed size k | sliding window (fixed) | `sliding_window` |
| contiguous subarray, longest/shortest | sliding window (variable) | `sliding_window` |
| valid parentheses, next greater element | stack | `stack` |
| find in sorted array, O(log n) | binary search | `binary_search` |
| reverse list, cycle detection | linked list pointers | `linked_list` |
| tree paths, LCA, level order | tree DFS/BFS | `trees` |
| shortest path, connected components | graph BFS/DFS | `graphs` |
| all combinations / permutations | backtracking | `backtracking` |
| max/min with choices, reuse allowed | DP | `dynamic_programming` |
| intervals, schedule, pick locally best | greedy | `greedy` |

## Progress

- [ ] `basics/star_patterns`
- [ ] `basics/loops`
- [ ] `basics/math`
- [ ] `arrays`
- [ ] `two_pointers`
- [ ] `sliding_window`
- [ ] `stack`
- [ ] `binary_search`
- [ ] `linked_list`
- [ ] `trees`
- [ ] `graphs`
- [ ] `backtracking`
- [ ] `dynamic_programming`
- [ ] `greedy`
- [ ] `math`

## Problem file template

**Star patterns** (`basics/star_patterns/`):

```python
"""
Problem: Print a square of stars (n x n)
Topic: star_patterns
Example: n=3 → *** / *** / ***
"""

def print_square(n: int) -> None:
    ...

if __name__ == "__main__":
    print_square(3)
```

**Algorithm problems** (all other folders):

```python
"""
Problem: ...
Pattern: two_pointers
When to use: sorted array + pair sum
Link: https://leetcode.com/...
"""

def solve(...):
    ...

if __name__ == "__main__":
    assert solve(...) == ...
    print("ok")
```
