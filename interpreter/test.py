import re

text = "This is a 'test string' with multiple words."

# Use regular expressions to find all words and quoted substrings
words = re.findall(r"[\w']+|[\"][\w\s]+[\"]", text)

# Print the resulting array
print(words)