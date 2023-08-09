numbers = [ 1,8 ,5 ,7, 6, 3, 2]
names = ['ash' ,'rez' , 'hichkas' ,'gholi' , 'ali']
numbers2 = numbers.copy()
names.insert(3, 'molla')
names.append('ali')
numbers.extend(names)
names.remove('rez')
numbers2.sort()
print(numbers2)
print(numbers)
print(names)
print(names.count('ali'))
print(names.index('gholi'))
