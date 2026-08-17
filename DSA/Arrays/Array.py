Yes. Since you are already in:

```text
E:\Users\Ganesh.MS\Documents\AIML-Practice
```

use this **single PowerShell command**. It will automatically create `DSA\Arrays\README.md` with your complete Arrays notes.

````powershell
@'
# DSA - Arrays

## 1. What is an Array?

An array is a data structure used to store multiple values in an ordered way.

In Python, we commonly use a list as an array.

```python
numbers = [10, 20, 30, 40, 50]
print(numbers[2])
# Output: 30
````

Python uses zero-based indexing.

---

## 2. Time Complexity

Time complexity describes how the running time of an algorithm changes when the input size increases.

### O(1) - Constant Time

The operation does not depend on the number of elements.

```python
numbers = [10, 20, 30, 40, 50]
print(numbers[2])
```

Time: `O(1)`

### O(n) - Linear Time

The algorithm processes each element one by one.

```python
for number in numbers:
    print(number)
```

Time: `O(n)`

### O(n²) - Quadratic Time

Usually occurs when one loop is inside another loop.

```python
for i in numbers:
    for j in numbers:
        print(i, j)
```

Time: `O(n²)`

### O(log n) - Logarithmic Time

The search space is repeatedly divided, usually by 2.

Binary Search is the common example.

Time: `O(log n)`

### O(n log n)

Approximately:

```text
number of elements × number of levels
```

Many efficient sorting algorithms use `O(n log n)`.

---

## 3. Space Complexity

Space complexity describes the extra memory used by an algorithm.

Using only a fixed number of variables:

```python
total = 0

for number in numbers:
    total += number
```

Space: `O(1)`

Creating a result list that grows with input:

```python
result = []

for number in numbers:
    result.append(number * 2)
```

Space: `O(n)`

---

## 4. Linear Search

Linear Search checks elements one by one.

```python
numbers = [10, 20, 30, 40, 50]
target = 40

for number in numbers:
    if number == target:
        print("Found")
        break
```

Worst-case Time: `O(n)`

It does not require sorted data.

---

## 5. Binary Search

Binary Search repeatedly divides a sorted array into two halves.

Example:

```text
[10, 20, 30, 40, 50, 60, 70]

Search: 60

Middle = 40

60 > 40
→ Search right side

[50, 60, 70]

Find 60
```

Time: `O(log n)`

Important:

```text
Binary Search requires sorted data.
```

Basic variables:

```python
left = 0
right = len(numbers) - 1
mid = (left + right) // 2
```

`left` represents the beginning of the current search range.

`right` represents the end of the current search range.

---

## 6. Prefix Sum

Prefix Sum stores cumulative sums.

Example:

```text
Original:
[10, 20, 30, 40]

Prefix:
[10, 30, 60, 100]
```

Calculation:

```text
10
10 + 20 = 30
10 + 20 + 30 = 60
10 + 20 + 30 + 40 = 100
```

Useful for repeated range-sum queries.

Build Time: `O(n)`

Space: `O(n)`

---

## 7. Difference Array

A Difference Array is useful when performing multiple range updates.

For an update from index `L` to `R` by `value`:

```python
diff[L] += value
diff[R + 1] -= value
```

Where:

```text
L     = starting index
R     = ending index
value = value to add
```

After applying all updates, cumulative sums reconstruct the final array.

---

## 8. Two Pointer Technique

Two Pointer uses two indexes to process an array efficiently.

Usually:

```text
left  → starts from beginning
right → starts from end
```

Example:

```python
numbers = [10, 20, 30, 40, 50]
target = 70

left = 0
right = len(numbers) - 1

while left < right:

    total = numbers[left] + numbers[right]

    if total == target:
        print("Pair found")
        break

    elif total < target:
        left += 1

    else:
        right -= 1
```

Rules:

```text
sum < target
→ left moves right

sum > target
→ right moves left

sum == target
→ pair found
```

For a sorted array:

Time: `O(n)`

Space: `O(1)`

---

## 9. Sliding Window

Sliding Window is used for continuous sections of an array.

Example:

```text
numbers = [10, 20, 30, 40, 50]
k = 3
```

Windows:

```text
[10, 20, 30] = 60
[20, 30, 40] = 90
[30, 40, 50] = 120
```

Instead of recalculating the entire window:

```text
Old sum = 60

Remove 10
Add 40

60 - 10 + 40 = 90
```

Python:

```python
numbers = [10, 20, 30, 40, 50]
k = 3

window_sum = sum(numbers[:k])
maximum = window_sum

for i in range(k, len(numbers)):
    window_sum = window_sum - numbers[i - k] + numbers[i]
    maximum = max(maximum, window_sum)

print(maximum)
```

Time: `O(n)`

Space: `O(1)`

---

## 10. Kadane's Algorithm

Kadane's Algorithm finds the maximum sum of a contiguous subarray.

Example:

```python
numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
```

Best subarray:

```text
[4, -1, 2, 1]
```

Sum:

```text
4 + (-1) + 2 + 1 = 6
```

At every element:

```text
Continue the current subarray
OR
Start a new subarray
```

Python:

```python
numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

current_sum = numbers[0]
maximum_sum = numbers[0]

for number in numbers[1:]:

    current_sum = max(
        number,
        current_sum + number
    )

    maximum_sum = max(
        maximum_sum,
        current_sum
    )

print(maximum_sum)
```

Output:

```text
6
```

Time: `O(n)`

Space: `O(1)`

---

## 11. Array Rotation

Array rotation moves elements from one side to another.

### Left Rotation

```text
Original:
[1, 2, 3, 4, 5]

Left rotate by 1:
[2, 3, 4, 5, 1]
```

### Right Rotation

```text
Original:
[1, 2, 3, 4, 5]

Right rotate by 1:
[5, 1, 2, 3, 4]

Right rotate by 2:
[4, 5, 1, 2, 3]
```

Python:

```python
numbers = [1, 2, 3, 4, 5]
k = 2

k = k % len(numbers)

rotated = numbers[-k:] + numbers[:-k]

print(rotated)
```

Output:

```text
[4, 5, 1, 2, 3]
```

Why use `%`?

```text
k = 7
length = 5

7 % 5 = 2
```

Therefore:

```text
7 rotations = 2 effective rotations
```

---

## 12. 2D Arrays / Matrix

A matrix contains rows and columns.

Example:

```python
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]
```

Rows:

```python
len(matrix)
# 3
```

Columns:

```python
len(matrix[0])
# 3
```

---

## 13. Matrix Element Access

Syntax:

```python
matrix[row][column]
```

Example:

```python
matrix[1][2]
```

Output:

```text
60
```

Because:

```text
row = 1
column = 2
```

Remember:

```text
Row 0 → first row
Row 1 → second row
Row 2 → third row
```

---

## 14. Matrix Traversal

Use nested loops to visit every element.

```python
matrix = [
    [1, 2],
    [3, 4]
]

for row in matrix:
    for value in row:
        print(value)
```

Output:

```text
1
2
3
4
```

Why two loops?

```text
Outer loop
→ processes rows

Inner loop
→ processes values inside each row
```

Time:

`O(R × C)`

Where:

```text
R = number of rows
C = number of columns
```

---

## 15. Matrix Column Access

Example:

```python
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

for row in matrix:
    print(row[2])
```

Output:

```text
30
60
90
```

`row[2]` means the third column.

---

## 16. Matrix Sum

```python
matrix = [
    [10, 20],
    [30, 40]
]

total = 0

for row in matrix:
    for value in row:
        total += value

print(total)
```

Output:

```text
100
```

Calculation:

```text
10 + 20 + 30 + 40 = 100
```

---

## 17. Matrix Search

Search for a value:

```python
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == 60:
            print("Found at:", i, j)
```

Output:

```text
Found at: 1 2
```

Here:

```text
i = row index
j = column index
```

---

## 18. Matrix Rotation

For 90-degree clockwise rotation:

```text
Step 1 → Transpose
Step 2 → Reverse every row
```

Original:

```text
1 2
3 4
```

Transpose:

```text
1 3
2 4
```

Reverse every row:

```text
3 1
4 2
```

Final:

```text
3 1
4 2
```

---

# Complexity Summary

| Topic              |     Time | Space |
| ------------------ | -------: | ----: |
| Index Access       |     O(1) |  O(1) |
| Linear Search      |     O(n) |  O(1) |
| Binary Search      | O(log n) |  O(1) |
| Prefix Sum         |     O(n) |  O(n) |
| Difference Array   | O(n + q) |  O(n) |
| Two Pointer        |     O(n) |  O(1) |
| Sliding Window     |     O(n) |  O(1) |
| Kadane's Algorithm |     O(n) |  O(1) |
| Array Rotation     |     O(n) |  O(n) |
| Matrix Traversal   | O(R × C) |  O(1) |

---

