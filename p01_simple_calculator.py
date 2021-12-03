print("select any operation")
print("1. addition")
print("2. substraction")
print("3. multiplication")
print("4. division")

operation = int(input())
if operation == 1:
    num1 = int(input('enter first number '))
    num2 = int(input('enter second number '))
    print(num1 + num2)
elif operation == 2:
    num1 = int(input('enter first number '))
    num2 = int(input('enter second number '))
    print(num1 - num2)
elif operation == 3:
    num1 = int(input('enter first number '))
    num2 = int(input('enter second number '))
    print(num1 * num2)
elif operation == 4:
    num1 = int(input('enter first number '))
    num2 = int(input('enter second number '))
    print(num1 / num2)
else: print('invalid syntex')