walls = set()


for c in range(20):
    row = (input().split(','))
    for r, x in enumerate(row):
        if x == '1':
            start = (r,c)
        elif x == '2':
            end = (r,c)
        elif x == '-':
            walls.add((r,c))
    
shifts = [(0,1), (0,-1),(1,0),(-1,0)]
def adjs(pos):
    r,c = pos
    for dr,dc in shifts:
        r2 = r+dr
        c2 = c+dc
        if 0 <= r2 < 20 and 0 <= c2 < 20 and (r2,c2) not in walls:
            yield (r2,c2)

import heapq
from collections import defaultdict
dist = defaultdict(lambda: float('inf'))
parent = {}
dist[start] = 0
pq = [(0, start)]
while True:
    _, pos = heapq.heappop(pq)
    if pos == end:
        break
    
    r,c = pos
    for adj in adjs(pos):
        r2,c2 = adj
        h = ((r-r2)**2 + (c-c2)**2)**0.5
        d = dist[pos] + 1
        #print(adj, d)
        if d < dist[adj]:
            dist[adj] = d
            parent[adj] = pos
            heapq.heappush(pq, (d+h, adj))

#print(walls, start, end)
path = []
x = end
while True:
    path.append(x)
    if x not in parent:
        break
    x = parent[x]
for x in reversed(path):
    print(f'({x[0]},{x[1]})', end='')
    if x != end:
        print(',', end='')