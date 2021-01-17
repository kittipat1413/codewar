#https://www.codewars.com/kata/52597aa56021e91c93000cb0

def move_zeros(array):
    count = 0
    indexes = []
    for i in range(len(array)):
        if not isinstance(array[i], bool) and array[i] == 0:
             count+=1
             indexes.append(i)
             
    print(indexes)
    for index in sorted(indexes, reverse=True):
        del array[index]
    listOfZero = [0] * count
    array.extend(listOfZero)
    return array


print(move_zeros([0,1,None,2,False,1,0]))
