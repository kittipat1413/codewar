def points(dice):
    list_points = list(map(int, dice))
    list_points = sorted(list_points)
    uniq = set(list_points)
    # print(list_points)
    # print(uniq)
    if(len(uniq)!=5):
        if(len(uniq)==1):
            return 50
        # CHECK POKER or FULLHOUSE   
        if(len(uniq)==2):    
            e = uniq.pop()
            count = list_points.count(e) 
            if(count==4 or count==1):
                return 40
            else:
                return 30

        else:
            return 0
    else:
        # CHECK STRAIGHT or NOTHING
        if(list_points[0] == 1):
            list_points.remove(1)   
        if(sum(list_points) == (len(list_points)/2)*(list_points[0]+list_points[-1])):
            return 20
        else:
            return 0

print(points("34561"))
