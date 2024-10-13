# 
#feita: ok
#corrigida: 

verbo = input().lower()

if 'a' in verbo[-2]:
    verbo = verbo.replace('ar','')
    sem = i = vogal = 'a'
elif 'e' in verbo[-2]:
    verbo = verbo.replace('er','')
    sem = i = vogal = 'e'
else:
    verbo = verbo.replace('ir','')
    vogal = 'e'
    i = 'i'
    sem = ''

print(f'''\
Eu {verbo}o
Tu {verbo}{vogal}s
Ele {verbo}{vogal}
Nós {verbo}{i}mos
Vós {verbo}{sem}is
Eles {verbo}{vogal}m''')