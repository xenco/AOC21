n=[int(x) for x in open("input").read().split()]
print(sum([1 for i in range(1,len(n)) if (sum(n[i:i+3])>sum(n[i-1:i+2]))]))