a = float(input("Type first number: "))
b = float(input("Type second number: "))

operator = input("Choose your operator: - + / * ...")

if operator == "+":
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "/":
    print(a/b)
elif operator == "*":
    print(a * b)

else:
    print("Error...")