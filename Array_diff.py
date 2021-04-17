def array_diff(a, b):
    for i in b:
        while i in a: 
            a.remove(i)
    return a

print(array_diff([1,2,2],[2]))
