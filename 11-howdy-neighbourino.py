import string


word_chars = string.ascii_letters + "'"
word_chars = set(word_chars)

line = input()


out = ''

def process(o):
    
    up = o[0] == o[0].upper()
    o = o.lower()
    w = o
    if w[-1] == 'h':
        w += 'aroo'
    if len(o) >= 5 and o[-1] == 'r':
        w += 'ino'
    if o != 'and' and o[-1] == 'd':
        w += 'ily-doodily'
    if o.endswith('es'):
        w += 'ies'
    if o[0] == 'd':
        w = 'diddly ding dong ' + w
    if o[0] == 'n':
        w = 'noodly-' + w
    if o[0] == 'r':
        w = 'riddly-' + w
    if o == 'man':
        w = 'fella'
    if o == 'man\'s':
        w = 'fella\'s'
    if o == 'hello':
        w = 'howdy'
        
    if up:
        w = w[0].upper() + w[1:]
        
    return w

w = ''
for c in line:
    if c in word_chars:
        w += c
    else:
        if w:
            out += process(w)
            w = ''
        out += c
print(out)