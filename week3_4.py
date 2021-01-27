def alleen(a):
    newlist=list(set(filter (lambda x: x, a)))
    return newlist

print(alleen([1,2,3,3,3,3,4,5,5]))
