  
def solution(array_a, array_b):
    ans = 0
    print(type(ans))
    for i in range(len(array_a)):
        ans = ans + pow(array_a[i]-array_b[i],2)
        print(ans)
    mean = ans/len(array_a)
    print(mean)


a1 = [1,2,3]
a2 = [4,5,6]
solution(a1,a2)