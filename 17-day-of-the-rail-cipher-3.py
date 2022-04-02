num, plain = input().split('|')
num = int(num)

rails = [['*' for _ in range(len(plain))] for r in range(num)]

r = num - 1
d = -1
for i, c in enumerate(plain):
    rails[r][i] = c
    r += d
    if r == 0 or r == num-1:
        d *= -1

out = ''
for r in rails:
    out += (''.join(r)).replace('*', '')
print(out)