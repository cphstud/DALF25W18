
# 📚 Session: Advanced Data Transformations with List Comprehensions, Lambda, and Map

## ⏰ Time: 45 minutes

---

## 📋 Topics

- List comprehensions revisited (nested conditions, transformations)
- Anonymous functions with `lambda`
- Applying functions over lists with `map`
- Combining `map` with `lambda`
- When to prefer list comprehensions vs map

---

## 🧩 Examples

### ✅ List Comprehension
```python
# Basic
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]

# With condition
evens = [x for x in range(10) if x % 2 == 0]  # [0, 2, 4, 6, 8]
```

### ✅ Lambda Functions
```python
# Define anonymous function
add = lambda x, y: x + y
print(add(2, 3))  # 5

# One-line simple operations
triple = lambda x: x * 3
print(triple(4))  # 12
```

### ✅ Map Function
```python
# Apply a function to each item
nums = [1, 2, 3, 4]
tripled = list(map(lambda x: x * 3, nums))
print(tripled)  # [3, 6, 9, 12]
```

### ✅ List Comprehension vs Map+Lambda
```python
# List comprehension
[x**2 for x in range(5)]

# Same with map + lambda
list(map(lambda x: x**2, range(5)))
```

---

## 📝 Exercises

### Exercise 1
- Use list comprehension to create a list of the **lengths** of all words in a sentence, ignoring words shorter than 3 letters.

### Exercise 2
- Write a lambda function that takes a string and returns it **lowercased and reversed**.
- Apply it to a list of words using map.

```python
# Input
words = ["Hello", "World", "AI"]

# Expected Output
['olleh', 'dlrow', 'ia']
```

---

## 🎯 Mini-Challenge (Optional)

- Given a list of numbers, create a new list where:
  - Even numbers are squared
  - Odd numbers are cubed

➡️ Solve it once with **list comprehension**, and once with **map+lambda**.

---

## ✨ Summary Table

| Concept | Quick Example |
|:--------|:--------------|
| List Comprehension | `[x*2 for x in range(5)]` |
| Lambda Function | `lambda x: x + 1` |
| Map + Lambda | `list(map(lambda x: x*2, [1,2,3]))` |

---
