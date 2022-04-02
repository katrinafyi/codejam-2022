lines = [x.split(',') for x in input().split(';')]

total = int(lines[0][1])

items = [(x[0], int(x[1])) for x in lines[1:]]

#print(total, items)

from collections import defaultdict
cost_to_items = defaultdict(list)

for i, c in items:
    cost_to_items[c].append(i)
    
out = set()
for c in cost_to_items.keys():
    for i in cost_to_items[c]:
        c2 = total-c
        if c2 in cost_to_items:
            for i2 in cost_to_items[c2]:
                if i == i2: continue
                if c < c2:
                    out.add((i, i2))
                else:
                    out.add((i2, i))
                    
out = list(out)
out.sort()
print(*(x[0] + ',' + x[1] for x in out), sep=';')
