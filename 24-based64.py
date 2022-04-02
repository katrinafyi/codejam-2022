mapping = ['A','B','C',':D','E','F','G','>:DD','I','J','K',':33','M','N','O','P','Q',';)','S','T','U',':oo','W','X','Y','Z','a','b','c','d','-.-','f','g',":'((",'i','j','k','l',':cc','n','o','p','q',':?','s','t','u','v','w','@.@','y','z','0','1',':L','3','4','5','8==D','7','8','9','69','M.M']

line = input().encode()
padded = line
if len(line) % 3 != 0:
    padded += b'\x00' * (3-len(line) % 3)
    
#print(line)
#print(padded)

i = 0
while i < len(line):
    #print(padded[i:i+3])
    x = int.from_bytes(padded[i:i+3], 'big')
    d = x & 0b111111
    x >>= 6
    c = x & 0b111111
    x >>= 6
    b = x & 0b111111
    x >>= 6
    a = x & 0b111111
    
    a = mapping[a]
    b = mapping[b]
    c = mapping[c]
    d = mapping[d]
    pad = 'O.O'
    
    
    i += 3
    if not i < len(line):
        last = len(line) % 3
        if last == 1:
            c = d = pad
        elif last == 2:
            d = pad
    
    print(a+b+c+d, end='')