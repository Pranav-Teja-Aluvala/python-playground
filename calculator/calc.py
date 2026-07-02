# A simple calculator program in Python that performs basic arithmetic operations and power calculation.

class Calculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
    
    def subtract(self):
        return self.a - self.b
    
    def multiply(self):
        return self.a * self.b
    
    def divide(self):
        if self.b == 0:
            print("Error: Cannot divide with zero!")
        else:
            return self.a / self.b 

    def power(self):
        return self.a ** self.b 

a = float(input("Enter First Number: "))
op = input("Enter the operator(+,-,*,/,**): ")
b = float(input("Enter Second Number: "))
cal = Calculator(a,b)

if op == '+':
    print("Result: ",cal.add())
elif op == '-':
    print("Result: ",cal.subtract())
elif op == '*':
    print("Result: ",cal.multiply())
elif op == '/':
    print("Result: ",cal.divide())
elif op == '**':
    print("Result: ",cal.power())
else:
    print("Please select from the given operators.")

choice = input("see all the other results? (y/n): ").lower()
if choice == 'y':
    print(f'-----------------------------------\
          \nAddition: {cal.add()}\nsubtraction: {cal.subtract()}\nMultiplication: {cal.multiply()}\nDivision: {cal.divide()}\nPower: {cal.power()}\
          \n-------------------------------------')
else:
    print("***")
