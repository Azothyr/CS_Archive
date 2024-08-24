doctor_called = ("The doctor called today to see if I had any problems getting my medication and if my condition had improved with the medication since I took it.")

def find_longest_string_and_freq(string):
  words = string.split()

  longest_word = ""
  longest_word_freq = 0

  word_freq = {}
  for word in words:
    if len(word) > len(longest_word):
      longest_word = word
  longest_word_freq = words.count(longest_word)
  return (longest_word, longest_word_freq)

print(find_longest_string_and_freq(doctor_called))
"""
Same result as above
"""
def find_longest_string_and_freq(data):
  data_split = data.split(" ")
  longest_string = max(data_split, key = len)
  longest_string_freq = data_split.count(longest_string)
  return(longest_string, longest_string_freq)
"""
-------------------------------------------------------------------
"""
