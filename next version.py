def next_version(version):
    list_ver = list(version.split("."))
    list_ver = [int(i) for i in list_ver]

    done = False
    for i in range(len(list_ver)):
        if(done == False):
            if(list_ver[len(list_ver)-1 - i] == 9 and (len(list_ver)-1 - i) != 0 ):
                list_ver[len(list_ver)-1 - i] = 0
            else:
                list_ver[len(list_ver)-1 - i] +=  1
                done = True
    s = [str(i) for i in list_ver] 
    res = ".".join(s)
    print(res)
    return res


next_version("3.9.2")