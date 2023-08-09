weight = int(input('Your weight : '))
unit = input('(K)g or (L)bs: ')
if unit.upper() == "L":
  converted = weight * 0.45
  print(f"You are {converted} kilos ")
elif unit.upper() == "k":
 converted = weight / 0.45
 print(f"You are {converted} pounds ")
else:
  print("You hame to write K or L for the unit")




