def string_length(str):
    count = 0
    for char in str:
        count += 1
    return count

# Taking input
str = input("Enter text: ")

# Calling function
length = string_length(str)

print(f"Length of '{str}' is: {length}")
