import requests

url = 'http://www.gutenberg.org/files/11/11-0.txt'
response = requests.get(url)
text = response.text

text = text.lower()

from collections import Counter
import re

words = re.findall(r'\b\w+\b', text)

word_counts = Counter(words)
count_cheshire = word_counts['cheshire']

print(f'The word "Cheshire" occurs {count_cheshire} times in "Alice\'s Adventures in Wonderland".')
