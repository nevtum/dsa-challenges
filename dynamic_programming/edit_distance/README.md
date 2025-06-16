# Edit Distance (Levenshtein Distance)

## Problem Description
Given two strings, find the minimum number of operations required to transform one string into another.

## Operations Allowed
- Insert a character
- Delete a character
- Replace a character

## Example: Transforming "horse" to "ros"

### Transformation Matrix
```
    ø   r   o   s
ø   0   1   2   3
h   1   1   2   3
o   2   2   1   2
r   3   2   2   2
s   4   3   3   2
e   5   4   4   3
```

### Matrix Calculation Rules
- First row/column represent edit distances for empty string transformations
- Each cell represents minimum operations to convert substring up to that point
- Bottom-right cell gives total minimum edit distance

### Operation Strategy
- If characters match: take diagonal top-left value
- If characters differ: 1 + minimum of (left, top, diagonal top-left)

### Transforming "horse" to "ros"
1. Replace 'h' with 'r' (1 operation)
2. Delete 'r' (1 operation)
3. Delete 'e' (1 operation)
**Total: 3 operations**

## Complexity
- Time Complexity: O(m*n)
- Space Complexity: O(m*n)