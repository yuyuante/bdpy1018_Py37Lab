l1 = ()
l2 = []
l3 = {}
l4 = {'x'}
l5 = {'x': 500}
l6 = set()
print(type(l1), type(l2), type(l3), type(l4), type(l5), type(l6))
s1 = set(list('APPLE'))
print(s1)
s2 = set(list('PINEAPPLE'))
print(s2)
s3 = {'B', 'A', 'N', 'A', 'N', 'A'}
print(s3)
print(s1 | s3)
print(s1 & s3)
print(s1 ^ s3)
print(len(s1 | s3))
s3.add('X')
print(s3)
s3.add('X')
print(s3)
s3.add(('X', 'Y'))
print(s3)
s3.add(3.14159)
print(s3)
# s3.add(s1)