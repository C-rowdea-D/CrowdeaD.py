odds = {1 ,3 ,5 ,7 ,9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7, 11}
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9,}
setB = {10, 11, 12, 13}
setC = {17, 18, 19}
u = odds.union(evens)
print(u)

i = u.intersection(primes)
print(i)

i1 = odds.intersection(evens)
print(i1)

diff = odds.difference(primes)
print(diff)

diff1 = primes.difference(odds)
print(diff1)

sym = odds.symmetric_difference(setA)
print(sym)

odds.update(evens)
print(odds)

odds.intersection_update(evens)
print(odds)

odds.difference_update(evens)
print(odds)

print(odds.issubset(setA)) #have all odds in set A

print(setA.issuperset(odds))  #set A contains all odds in self

print(setA.isdisjoint(evens)) # not included elements

setD = setA.copy()
setD.add(20)
print(setD)
print(setA)

h = frozenset([1,8,9]) #you can't do anything on frozenset
h.add(3)
print(h)