s,t,b = map(int,input().split())
c = 2 * s * t * b * 512
kb = 1024
op = c // 1024
opt = str(op)+"KB"
print(opt)