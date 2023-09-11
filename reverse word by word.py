# Reverse a String  Word by Word

string = " How are you"
# reversing words in a given string
word = string.split()[::-1]
a = []
for i in word:
    a.append(i)
print(" ".join(a))
