bhumi = input("enter word: ")
rev = ""

for char in bhumi:
    rev = char + rev

if bhumi == rev:
    print("palindrome")
else:
    print("not palindrome")