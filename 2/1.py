h,v,dirs=0,0,[x.strip().split() for x in open("input").readlines()]

for d,x in dirs:
 if d=="forward": h+=int(x)
 if d=="up": v-=int(x)
 if d=="down": v+=int(x)

print(h*v)