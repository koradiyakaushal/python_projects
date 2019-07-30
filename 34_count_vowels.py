n = input("Enter String or Sentence: ")
count = 0
vowel = []
for i in n:
    if i in 'aeiouAEIOU':
        count += 1
        vowel.append(i)

print(count)
print(vowel)
