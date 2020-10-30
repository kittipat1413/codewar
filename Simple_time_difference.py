#Simple time difference
def solve(arr):
    time = sorted(arr)
    minutes = []
    diff = []
    for i in time:
        x = i.split(":")
        minutes.append((int(x[0])*60)+int(x[1]))
    for i in range(len(minutes)-1):
        diff.append(minutes[i+1]-(minutes[i]+1))
    last_one = (1440-(minutes[-1]+1))+(minutes[0])
    diff.append(last_one)
    
    ans = max(diff)
    hour = ans / 60
    minute =  ans % 60
    ans = "%02d:%02d" % (hour, minute)
    return ans

    # print(time)
    # print(minutes)
    # print(diff)


    
print(solve(["23:00","04:22","18:05","06:24"]))# "11:40"
# solve(["14:51"]) = "23:59". If the alarm goes off now, it will not go off for another 23 hours and 59 minutes.
# solve(["23:00","04:22","18:05","06:24"]) == "11:40". The max interval that the alarm will not go off is 11 hours and 40 minutes.