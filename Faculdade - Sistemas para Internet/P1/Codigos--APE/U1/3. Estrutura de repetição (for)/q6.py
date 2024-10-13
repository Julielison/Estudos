print('Digite 3 números inteiros:\n', end='')
n = int(input('N: '))
x = int(input('X: '))
y = int(input('Y: '))
for i in range(x, y+1, n):
    print(i)