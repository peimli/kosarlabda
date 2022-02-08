l = [s.strip().split(';') for s in open('eredmenyek.txt','r',encoding='latin2')]
l.remove(l[0])

#3.feladat: Real Madrid, hazai, idegen

hazai = [i[0] for i in l if i[0] == 'Real Madrid']
idegen = [i[1] for i in l if i[1] == 'Real Madrid']
print(f'3.feladat: Real Madrid: hazai: {len(hazai)} ,idegen: {len(idegen)}')

#4.feladat:dontetlen volt-e
'''
volt = 'volt'
for sor in l:
    if sor[2] == sor[3]:
        volt = 'igen'
    if sor[2] != sor[3]:
        volt = 'nem'
       
print(f'4.feladat: Volt döntetlen? {volt}')
'''
#5.feladat:barcelona

barcelona = [sor[0] for sor in l if 'Barcelona' in sor[0]]
print(f'A barcelonai csapat neve: {barcelona[0]}')

#6.feladat:

print(f'6.feladat')
csapatok = [sor for sor in l if '2004-11-21' in sor[-1]]
for i in csapatok:
    csapat1 = i[0]
    csapat2 = i[1]
    pontszam1 = i[2]
    pontszam2 = i[3]
    print(f'           {csapat1}-{csapat2} ({pontszam1}:{pontszam2})')


#7.feladat:
stat = dict()
for sor in l:
    helyszin = sor[4]
    stat[helyszin] = stat.get(helyszin,0) + 1

print(    f'7.feladat:')

for sor in stat.items():
    if sor[1] > 20:
        print(f'      {sor[0]}: {sor[1]} ')





