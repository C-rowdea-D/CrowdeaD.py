smallest = None
for value in [9, 13 , 41 , 5, 22, 67]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value )
