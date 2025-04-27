
# 📚 Python Sessions and Exercises

## Day 1: Python Fundamentals for Data Science and NLP

### Session 1: Python Basics
**Keywords:** if, else, elif, for, while, break, continue, list, tuple, dict, set, print, input

**Examples:**
```python
x = 10
if x > 5:
    print("Big")
else:
    print("Small")

names = ["Jack", "Anna", "Tom"]
for name in names:
    print(name)

ages = {"Alice": 24, "Bob": 30}
print(ages["Bob"])
```

**Exercise:**  
Loop through a list of ages and print 'child', 'adult', or 'senior'.

---

### Session 2: Functions and Modules
**Keywords:** def, return, import, from, as, *args, **kwargs

**Examples:**
```python
def greet(name):
    return f"Hello, {name}!"

import math
print(math.sqrt(16))

def describe_person(name, *hobbies, **info):
    print(name, hobbies, info)
```

**Exercise:**  
Write describe_passenger(name, *hobbies, **info).

---

### Session 3: Data Structures and Comprehensions
**Keywords:** [], {}, :, list comprehension, dictionary comprehension

**Examples:**
```python
squares = [x**2 for x in range(5)]
word_lengths = {word: len(word) for word in ["cat", "dog", "elephant"]}
```

**Exercise:**  
Build a dict mapping name -> word length, only for names longer than 3 letters.

---

### Session 4: Regular Expressions
**Keywords:** import re, re.search, re.findall, re.sub, raw strings

**Examples:**
```python
import re
emails = re.findall(r"\b[\w.-]+@[\w.-]+\.\w+\b", text)
new_text = re.sub(r"\s", "_", "Hello World")
```

**Exercise:**  
Extract the title (Mr, Mrs, Miss, etc.) from Titanic names.

## Day 2: Python for Data Science and NLP

### Session 5: Loading and Managing Files
**Keywords:** import os, import glob, open(), with

**Examples:**
```python
import glob
texts = []
for filename in glob.glob('folder/*.txt'):
    with open(filename, 'r', encoding='utf-8') as f:
        texts.append(f.read())
```

**Exercise:**  
Load all .txt files and count total number of words.

---

### Session 6: numpy Essentials
**Keywords:** import numpy as np, arrays, slicing, vectorization

**Examples:**
```python
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr * 2)
print(arr[arr > 2])
```

**Exercise:**  
Select ages >60 or <15 from a numpy array.

---

### Session 7: pandas for Data Wrangling
**Keywords:** import pandas as pd, DataFrame, Series, read_csv, loc[], iloc[]

**Examples:**
```python
import pandas as pd
df = pd.read_csv("titanic.csv")
print(df.head())
old = df[df['Age'] > 60]
```

**Exercise:**  
Select passengers older than 60 and younger than 15. Add an 'age_group' column.

---

### Session 8: Grouping, Aggregating, and Plotting
**Keywords:** groupby, agg(), pivot_table(), plot()

**Examples:**
```python
survival_rates = df.groupby('Pclass')['Survived'].mean()
survival_rates.plot(kind='bar')
import matplotlib.pyplot as plt
plt.show()
```

**Exercise:**  
Group by 'Sex' and 'Pclass', calculate survival rates, and plot grouped bars.
