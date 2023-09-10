# Reverse a string without affecting special characters


def reverse_string(alphabets):
    index = -1
    for i in range(len(alphabets) - 1, int(len(alphabets) / 2), -1):

        if alphabets[i].isalpha():
            temp = alphabets[i]
            while True:
                index += 1
                if alphabets[index].isalpha():
                    alphabets[i] = alphabets[index]
                    alphabets[index] = temp
                    break
    return alphabets

string = "a!!!b.c.d,e'f,ghi"
print("Input string: ", string)
string = reverse_string(list(string))
print("Output string: ", "".join(string))

# This code is contributed by shiva9610
