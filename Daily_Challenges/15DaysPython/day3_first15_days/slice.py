text = "ABCDEFGHIJKLMN"
fragment = text[2:8:2]
print(fragment)


xab = 'If the implementation is hard to explain, it might be a bad idea.'
y = xab.replace('hard', 'easy' )
s = y.replace('bad','good')
print(s)


xab = 'If the implementation is hard to explain,\n it might be a bad idea.'
y = xab.replace('hard', 'easy' ).replace('bad','good')
print(y)

fruit = ['apples', 'oranges', 'watermelon', 'oranges', 'apples']
y = fruit.count('oranges')
print(fruit)
print (y)