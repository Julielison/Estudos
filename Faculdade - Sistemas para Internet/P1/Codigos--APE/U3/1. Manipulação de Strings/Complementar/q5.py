# 
#feita: ok
#corrigida: 

frase = input().upper()
count = 0
for i in range(len(frase)):
    print(f'{frase[i]*(i+1)}')

for j in range(len(frase)-2,-1,-1):
    print(f'{frase[j]*(j+1)}')