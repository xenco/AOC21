n=[int(x) for x in open("input").read().split()]
print(sum([1 for i in range(1,len(n)) if (n[i]>n[i-1])]))