sample1_data = open('Sample-1.txt')
sample2_data = open('Sample-2.txt')

str = ''

sample1_lis1 = []
sample1_lis2 = []
sample2_lis1 = []
sample2_lis2 = []


for word in sample1_data:
    word = word.strip()
    x = word.split('.')
    for i in x:
        if i is not str:
            sample1_lis1.append(i)

for i in sample1_lis1:
    y = i.split()
    for j in y:
        sample1_lis2.append(j)

#print(sample1_lis2)

dic1 = {}

for word in sample1_lis2:
    dic1[word] = dic1.get(word, 0) + 1

print(dic1)

keys1_count = len(dic1.keys())
print(keys1_count)
print('-------------------------------------------------')
for word in sample2_data:
    word = word.strip()
    x = word.split('.')
    for i in x:
        if i is not str:
            sample2_lis1.append(i)

for i in sample2_lis1:
    y = i.split()
    for j in y:
        sample2_lis2.append(j)

#print(sample2_lis2)

dic2 = {}

for word in sample2_lis2:
    dic2[word] = dic2.get(word, 0) + 1

print(dic2)

keys2_count = len(dic2.keys())
print(keys2_count)
print('---------------------------------------------------')

key = max(keys1_count, keys2_count)
print(key)
