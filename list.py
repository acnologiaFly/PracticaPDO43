list1 = [1,4,6]
list2 = [11,33,22]
a = list(set(list2))
a.sort()
res = []
for z in a:
    for v in range(0, len(list2)):
        if(list2[v] == z):
            res.append(list1[v])
print(res)