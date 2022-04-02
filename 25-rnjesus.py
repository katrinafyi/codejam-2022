x0, minn, maxx, n = input().split()
x0 = float(x0)
minn = int(minn)
maxx = int(maxx)
n = int(n)

r = r = 3.7783


x=x0
for i in range(n):
    x = r * x * (1-x)
    
    print((maxx - minn) * x + minn)