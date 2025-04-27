
# ✨ Mini-Project: Titanic Text Analysis Challenge

## Goal
- Load Titanic dataset.
- Extract and clean titles (Mr, Mrs, Miss, etc.) from passenger names using regular expressions.
- Count title frequencies.
- Plot the result.

## Keywords
`pandas`, `re`, `apply`, `value_counts`, `plot`, `regex`, `replace`, `groupby`

## Examples
```python
import pandas as pd
import re

# Load data
df = pd.read_csv('titanic.csv')

# Extract title using regex
def extract_title(name):
    match = re.search(r", (\w+)\.", name)
    if match:
        return match.group(1)
    return None

df['Title'] = df['Name'].apply(extract_title)
```

## Task
1. **Load the Titanic dataset** (`titanic.csv`) into a pandas DataFrame.
2. **Extract titles** (`Mr`, `Mrs`, `Miss`, etc.) from the `Name` column using a **regular expression**.
3. **Create a new column** called `Title` based on the extracted data.
4. **Group rare titles** like `Capt`, `Dr`, `Rev`, etc. into a new category called `"Rare"`.
5. **Count the frequency** of each title.
6. **Plot a bar chart** showing the frequency of each title.

## Bonus Challenge
- Calculate **survival rates** for each title (`groupby Title, mean Survived`).
- Which titles had the highest survival rate?
