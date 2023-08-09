Num1 = float(input("enter your first number :"))
op = input("your operator :")
Num2 = float(input("enter your second number :"))
if op == "+" :
    print(Num1 + Num2)
elif op == "-" :
    print(Num1 - Num2)
elif op == "*" :
    print(Num1 * Num2)
elif op == "/" :
    print(Num1 / Num2)
else:
    print("make a right operator")