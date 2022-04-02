m = {'Y': 1, 'B': 0}

rows = [[m[y] for y in x.split(',')] for x in input().split(';')]

sums = [[0]*len(r) for r in rows]

#print(rows)
#print(sums)
for r, row in enumerate(rows):
    for c, x in enumerate(row):
        val = rows[r][c]
        if c-1 >= 0:
            val += sums[r][c-1]
        if r-1 >= 0:
            val += sums[r-1][c]
        if c-1 >= 0 and r-1 >= 0:
            val -= sums[r-1][c-1]
        sums[r][c] = val
    
    
def rect(r,c,h,w):
    h -= 1
    w -= 1
    y = sums[r+h][c+w]
    if r-1 >= 0:
        y -= sums[r-1][c+w]
    if c-1 >= 0:
        y -= sums[r+h][c-1]
    if r-1 >= 0 and c-1 >= 0:
        y += sums[r-1][c-1]
    return (y, (h+1)*(w+1))
        
    
def go(h, w):
    yellows = []
    
    y, a = rect(0, 0, h, 15)
    if y > a-y:
        yellows.append(a)
    
    y, a = rect(h, 0, 15-h, w)
    if y > a-y:
        yellows.append(a)
        
    y, a = rect(h, w, 15-h, 15-w)
    if y > a-y:
        yellows.append(a)
    
    if len(yellows) != 2:
        return None
    return sum(yellows)
        
m = 0
M = None
for h in range(4, 12):
    for w in range(4, 12):
        g = go(h,w)
        if g is None: continue
        if g > m:
            m = g
            M = h,w
            
#print(g, M)
#[[(0, 0), (9, 14)], [(10, 0), (14, 10)], [(10, 11), (14, 14)]]

h,w = M

out = [
    [(0, 0), (h-1, 14)], 
    [(h, 0), (14, w-1)], 
    [(h, w), (14, 14)]
]

print(out)