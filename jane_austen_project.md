
# 📚 Mini-Project: Regex on Jane Austen's *Pride and Prejudice*

## Project: Extract Character Mentions and Quotes

### Scenario
You are given the full text of *Pride and Prejudice* by Jane Austen. Your job is to use regex to:

- Find all character mentions (e.g., "Mr. Darcy", "Elizabeth", "Miss Bennet", etc.).
- Extract all direct quotes (things inside quotation marks).

Analyze the text:
- Which characters are most mentioned?
- How often characters are speaking?

### Input
- A `.txt` file of **Pride and Prejudice**.

### Steps
1. **Load the novel text** into Python.
2. **Find all character mentions**:
   - Patterns: `Mr. X`, `Mrs. Y`, `Miss Z`, names like "Elizabeth", "Darcy".
3. **Find all quotes**:
   - Capture text inside quotation marks (`"` or `“ ”`).
4. **Count mentions**.
5. **Save results**:
   - Mentions into a CSV.
   - Quotes into a TXT.

### Example Outputs
#### Character Mentions (CSV)
| Character | Mentions |
|:----------|---------:|
| Mr. Darcy | 310 |
| Elizabeth | 270 |
| Mr. Bingley | 120 |

#### Quotes (TXT)
```
"It is a truth universally acknowledged, that a single man in possession of a good fortune, must be in want of a wife."
"She is tolerable; but not handsome enough to tempt me."
```

### Hints
- Regex for titled names: `(Mr|Mrs|Miss)\. \w+`
- Regex for quotes: `"(.*?)"` (use lazy matching)
- Normalize extracted names.

### Bonus Challenges
- Build a small network graph of characters appearing in the same sentence.
- Find the character who speaks the most.

### Example Code Snippet
```python
import re

# Find titled names
names = re.findall(r"(Mr|Mrs|Miss)\. \w+", text)

# Find quotes
quotes = re.findall(r'"(.*?)"', text, re.DOTALL)
```
