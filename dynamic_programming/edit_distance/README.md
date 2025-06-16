# Edit Distance (Levenshtein Distance)

## Problem Description
Given two strings, find the minimum number of operations required to transform one string into another.

## Operations Allowed
- Insert a character
- Delete a character
- Replace a character

## Recursive Problem Decomposition

### Base Cases
Understanding base cases is crucial:
- `word1=""` and `word2="abc"`: Requires inserting all characters from word2
- `word1="abc"` and `word2=""`: Requires deleting all characters from word1

### Recursive Strategy
The recursive solution breaks down into three key operations:

#### Insert Operation
- `min_distance("", "abc")` = 1 edit + `min_distance("a", "abc")`
- Then recursively: 1 edit + `min_distance("", "bc")`
- Handles inserting characters from the target string

#### Deletion Operation
- `min_distance("abc", "")` = 1 edit + `min_distance("bc", "")`
- Handles removing characters from the source string

#### Replacement Operation
- `min_distance("xxx", "abc")` = 1 edit + `min_distance("xx", "bc")`
- Handles replacing characters when they don't match

### Recursive Decomposition Pattern
1. If strings match at current index: No operation, move to next characters
2. If strings differ: Try three recursive paths
   - Insert a character
   - Delete a character
   - Replace a character
3. Choose path with minimum total edits

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

### Transforming "horse" to "ros"
1. Replace 'h' with 'r' (1 operation)
2. Delete 'r' (1 operation)
3. Delete 'e' (1 operation)
**Total: 3 operations**

## Complexity
- Time Complexity: O(m*n)
- Space Complexity: O(m*n)

## Implementation Techniques
- Recursive solution with memoization
- Bottom-up dynamic programming
- Minimize recursive calls using caching

## Key Insights
- Problem can be solved top-down or bottom-up
- Memoization crucial for performance
- Base cases define recursive termination