word=input(str("Enter a word"))
l=list(word)
rev=l[::-1]
if(''.join(rev)==word):
    print("Palindrome")
else:
    print("Not")
