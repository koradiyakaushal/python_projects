i = input("Enter String to check palindrome: ")

if i == i[::-1]:
    print("palindrome.")
else:
    print("Not palindrome.")