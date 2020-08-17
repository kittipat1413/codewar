
def sum_of_intervals(intervals):
    check = True
    ans = 0
    intervals.sort()
    intervals = [list(ele) for ele in intervals] 

    while(check):
        intervals,check = append_intervals(intervals)
    
    print(intervals)
    
    for i in range(len(intervals)):
        ans = (intervals[i][1]-intervals[i][0])+ans
    
    print(ans)
        
def append_intervals(intervals):
    for i in range(len(intervals)):
        for j in range(i+1,len(intervals)):
            if(intervals[i][1]>intervals[j][0]):
                if(intervals[j][1]>intervals[i][1]):
                    intervals[i][1] = intervals[j][1]
                    del intervals[j]
                else:
                    del intervals[j]

                return(intervals,True)
    return(intervals,False)

sum_of_intervals([(1, 4), (7, 10), (3, 5)])