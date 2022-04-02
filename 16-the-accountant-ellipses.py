def go():
    print(input())
    print(input())
    
    x = 0
    
    while True:
        l = input()
        if not l:
            break
        name, cost = l.split('$')
        x += int(cost)
        name = name.replace('.', '')

        print(name, '.' * (50 - len(name) - len(cost) - 1), '$' + cost, sep='')
        
    print()
    return x
    
rev = go()
exp = go()

input()
print('Cost')
print(input())
print(f'${rev - exp}'.rjust(50))    