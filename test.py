import linecache

FILE = 'input.txt'
f = open(FILE, 'r')

list1 = {}
list2 = []

lastrow = sum(1 for i in open(FILE))  # ファイル内の最終行の番号を取得
lastrow_sen = int(linecache.getline(FILE, lastrow))

for i in range(1, lastrow):
    a, b = linecache.getline(FILE, i).split(':')
    if not lastrow_sen % int(a):
        list2.append(int(a))
        list1[a] = b.rstrip('\n')

if list2:
    for i in sorted(list2):
        print(list1[str(i)], end="")
else:
    print(lastrow_sen)

f.close()