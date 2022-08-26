x = 'abc a bCd bC AbC BC BCD bcd ABC'
x = x.lower().split(' ')
count = 0
z = {}
for i in range(len(x)):
    z[x[i]] = x.count(x[i])

#for i,j in z.items():
    #print(z)


print(*z)

'''x=list('Arbuz')
print(x)
print('\n'.join(x))

x = [3, 6, 8]
y = itertools.permutations(x)

print(list(y))
y = itertools.permutations(x)
print(len(list(y)))'''

'''def truncate(text, number):
    new = text[:number]
    return (new+'...')

x = truncate("If your site is an independent project,"
             " you can create a new repository to store"
             " your site's source code. If your site is "
             "associated with an existing project, you can a", 10)

print(x)'''

