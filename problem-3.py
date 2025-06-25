a = int(input("Enter a number: "))
if a % 2 == 0:
    a = a - 1
a = a * 2
for i in range(a):
    if i % 2 != 0:
        print(i)