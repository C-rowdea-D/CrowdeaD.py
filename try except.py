try :
     number = int(input("Enter a number :"))
     print(number)
except ValueError :
    print("That's not a number!")

try :
    division = 10/0
    print(num)
except ZeroDivisionError as err :
    print(err)
