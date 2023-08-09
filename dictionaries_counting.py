counts = dict()
names = ['han', 'ash', 'sar', 'jj', 'han' ]
for name in names :
    counts[name] = counts.get (name, 0) + 1
print(counts)

