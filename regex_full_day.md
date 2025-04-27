
# 📚 Full-Day Course: Regular Expressions in Python

## 🕒 Course Duration: 3 Hours

---

## Part 1: Regex Basics (45 minutes)

### Topics
- What is a regular expression?
- Why regex? (text cleaning, validation, extraction)
- Raw strings (`r"..."`) in Python
- Basic syntax:
  - `.` any character
  - `\d` digit, `\D` non-digit
  - `\w` word character, `\W` non-word
  - `\s` whitespace, `\S` non-whitespace
  - Quantifiers: `*`, `+`, `?`, `{n}`, `{n,m}`
  - Anchors: `^` start of string, `$` end of string

### Example Code
```python
import re

text = "The price is 45 dollars."

# Find digits
re.findall(r"\d+", text)

# Match start
re.match(r"The", text)

# Check end
re.search(r"dollars\.$", text)
```

### 📝 Exercise 1
- Find all numbers in `"I have 2 apples and 12 bananas."`
- Check if a string starts with a capital letter.

---

## Part 2: Grouping, Capturing, and Replacing (45 minutes)

### Topics
- Grouping with `()`
- Capturing subpatterns
- Named groups `(?P<name>...)`
- `re.sub()` for substitution
- Greedy vs. lazy matching (`*?`, `+?`)

### Example Code
```python
# Capture first and last names
name = "John Doe"
match = re.match(r"(\w+)\s(\w+)", name)
print(match.groups())

# Named groups
match = re.match(r"(?P<first>\w+)\s(?P<last>\w+)", name)
print(match.group('first'))

# Replace all digits
text = "Call 123-456-7890"
re.sub(r"\d", "X", text)
```

### 📝 Exercise 2
- Extract first and last names from a list of names.
- Replace all email domains with `"example.com"`.

---

## Part 3: Practical Patterns (1 hour)

### Topics
- Email matching
- Phone number matching
- Date matching
- HTML/XML tag extraction
- Greedy vs. lazy pitfalls

### Example Code
```python
# Email extraction
emails = re.findall(r"\b[\w.-]+@[\w.-]+\.\w+\b", "Contact: a@a.com, b.b@bb.org")

# Date extraction
dates = re.findall(r"\d{2}/\d{2}/\d{4}", "Today is 01/04/2025")

# HTML tag extraction
tags = re.findall(r"<.*?>", "<div><p>Hello</p></div>")
```

### 📝 Exercise 3
- Extract all emails from text.
- Find all valid dates.
- Extract all HTML tags.

---

## Part 4: Mini-Project (30 minutes)

### 🚀 Mini-Project: Text Analysis from *Pride and Prejudice*

#### Scenario
- Input: Full text of *Pride and Prejudice* (.txt file).
- Tasks:
  1. Extract all character mentions like "Mr. Darcy", "Elizabeth", etc.
  2. Extract all direct quotes from the novel.
  3. Save character mention counts to a CSV.
  4. Save extracted quotes to a TXT.

#### Example Code Snippet
```python
import re

# Find titled names
names = re.findall(r"(Mr|Mrs|Miss)\. \w+", text)

# Find quotes
quotes = re.findall(r'"(.*?)"', text, re.DOTALL)
```

#### Bonus Challenges
- Build a character network (who appears with whom).
- Find the character who speaks the most.

---

## 📋 Summary Table

| Part | Content | Time |
|:---|:---|:---|
| Part 1 | Regex basics and syntax | 45 min |
| Part 2 | Grouping, replacing, greedy/lazy | 45 min |
| Part 3 | Practical real-world patterns | 60 min |
| Part 4 | Mini-project: Text analysis | 30 min |

