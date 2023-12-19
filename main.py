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
  tuple_list = sorted(answer.items(), key=lambda x: x[1], reverse=True)
  for item in tuple_list:
    print(f"The '{item[0]}' character was found {item[1]} times")


with open("books/frankenstein.txt") as f:
  file_contents = f.read()
  print(count_letter_occurrence(file_contents))