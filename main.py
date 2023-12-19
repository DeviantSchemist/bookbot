def count_words(text):
  words = text.split()
  print(len(words))
  return len(words)

def count_letter_occurrence(text):
  answer = {}
  for char in text.lower():
    if not char.isalpha() or char in answer:
      continue
    answer[char] = text.lower().count(char)
  return answer

with open("books/frankenstein.txt") as f:
  file_contents = f.read()
  print(count_letter_occurrence(file_contents))