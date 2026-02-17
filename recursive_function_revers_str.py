def reverse_string(str):
    if str == "":
        return str
    return reverse_string(str[1:]) + str[0]

text = input("Enter text: ")
print(f"Reversed string is: {reverse_string(text)}")
