from random import shuffle

# l = []
with open('quiz.txt', 'r') as f:
    l = (f.readlines())
    k = l
    shuffle(l)
# print(l)
ans_key = {'1. who is PM of India?     a)modi      b)Rahul\n': 'a', '2. who is CM of Gujarat?   a)nitin     ''b)rupani\n': 'b', '3. where is Eden Garden?   a)bangalore b)kolkata\n': 'b', '4. When is a Republic Day? a)15 Aug    b)26 jan\n': 'a', "5. how much it cost's PG?  a)5500      b)4500": 'a'}

quiz_key = {}
for i in l:
    print(i)
    quiz_key[i] = input("enter ans: ")
print(quiz_key)
right_ans = 0
for i in k:
    if ans_key[i] == quiz_key[i]:
        right_ans += 1
print("correct answers are: ", right_ans)
