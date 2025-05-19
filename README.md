# Count-Word-Cheshire-in-Alice-s-Adventures-in-Wonderland

# Description
This Python script downloads the book Alice's Adventures in Wonderland from Project Gutenberg, processes the text for case-insensitivity, tokenizes it into words, and counts the number of times the word "cheshire" appears. It serves as a simple example of text analysis using Python.

# Usage
Example
```
# Step 1: Download the text file manually or using requests module
import requests

# Download the text file from Project Gutenberg
url = 'http://www.gutenberg.org/files/11/11-0.txt'
response = requests.get(url)
text = response.text

# Step 2: Read the text file into Python and lowercase for case-insensitivity
text = text.lower()

# Step 3: Tokenize the text into words and count occurrences of "cheshire"
from collections import Counter
import re

# Tokenize text into words (using regex to separate words)
words = re.findall(r'\b\w+\b', text)

# Count occurrences of "cheshire"
word_counts = Counter(words)
count_cheshire = word_counts['cheshire']

# Print the result
print(f'The word "Cheshire" occurs {count_cheshire} times in "Alice\'s Adventures in Wonderland".')
```
# Output
The word "Cheshire" occurs 7 times in "Alice's Adventures in Wonderland".


# Function Descriptions
* requests.get(url): Downloads the full text from the Project Gutenberg website.
* text.lower(): Converts all text to lowercase for case-insensitive matching.
* re.findall(r'\b\w+\b', text): Extracts all words using a regular expression.
* Counter(words): Counts the frequency of each word in the text.

# Applications
* Basic natural language processing (NLP) tasks
* Word frequency analysis
* Educational example for learning text handling in Python

# License
This project is licensed under the MIT License.
