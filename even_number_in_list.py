
n = int(input("Enter size of list: "))

numbers = []


for i in range(n):
    num = int(input("Enter element: "))
    numbers.append(num)

count = 0

for num in numbers:
    if num % 2 == 0:
        count = count + 1

print("Number of even numbers in the list:", count)
