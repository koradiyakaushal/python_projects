from random import choice

l = ['Heads', 'Tails']
heads = 0
tails = 0

while True:
    n = input("one more flip(y/n)? ")
    if n.lower()[0] == 'y':
        # print(choice(l))
        if choice(l) == 'Heads':
            print("Heads")
            heads += 1
        else:
            print("Tails")
            tails += 1
        print("heads: ", heads)
        print("tails: ", tails)
    else:
        print("heads: ", heads)
        print("tails: ", tails)
        break
