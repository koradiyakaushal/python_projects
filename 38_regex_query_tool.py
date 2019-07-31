import re
n = input("Enter String or Sentence: ")
r = input("Enter RegEx: ")

print(re.findall(r, n))

# ^The.*Spain$
# The rain in Spain
