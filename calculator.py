num1 = float(input("Enter num1: "))
operator = input("Choose your oprator (+ - * /): ")
num2 = float(input("Enter num2: "))


if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("Invalid operator")

    