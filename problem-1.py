class Calculator:
    def addition(self,a,b):
        sum = a + b
        print(sum)
    def subtraction(self,a,b):
        diff = a - b
        print(diff)
    def multiplication(self,a,b):
        pro = a * b
        print(pro)
    def division(self,a,b):
        quo = a / b
        print(quo)

C1 = Calculator()

a = float(input("Enter a: "))
b = float(input("Enter b: "))
choice = input("Enter your choice: ")
if choice == '+':
    C1.addition(a,b)
elif choice == '-':
    C1.subtraction(a,b)
elif choice == '*':
    C1.multiplication(a,b)
elif choice == '/':
    C1.division(a,b)
else:
    print("Invalid Choice!!!")