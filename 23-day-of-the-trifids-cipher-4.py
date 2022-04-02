key = input()
message = input().replace(' ', '')

cube = [[[None]*3 for _ in range(3)] for _ in range(3)]

#print(cube)

letters = {}

for i, k in enumerate(key):
    j = i // 9
    r = ((i%9) // 3)
    c = i % 3
    #print(j,r,c,k)
    cube[j][r][c] = k
    letters[k] = (j,r,c)
    
#print(cube)
#print(letters)

mat = []
for m in message:
    mat.append(list(letters[m]))
    
def transpose(m):
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]

def chunks(mat, n):
    i = 0
    while i < len(mat):
        yield mat[i:i+n]
        i += n
        
def flatten(t):
    return [item for sublist in t for item in sublist]

chunked = list(chunks(mat, 5))
#print(chunked)
trans = ([flatten(transpose(x)) for x in chunked])

o = ''
for t in trans:
    for chun in chunks(t, 3):
        j,r,c = chun
        o += cube[j][r][c]
    o += ' '
o = o[:-1]
print(o)
