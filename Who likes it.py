
# --------------------------question----------------------------------
# likes [] // must be "no one likes this"
# likes ["Peter"] // must be "Peter likes this"
# likes ["Jacob", "Alex"] // must be "Jacob and Alex like this"
# likes ["Max", "John", "Mark"] // must be "Max, John and Mark like this"
# likes ["Alex", "Jacob", "Mark", "Max"] // must be "Alex, Jacob and 2 others like this"
# -------------------------------------------------------------------
def likes(names):
    #your code here
    print(*names)
    if len(names) == 0:
        print("no one likes this")
        return "no one likes this"
    else:
            if len(names) == 1:
                print(names[0]+" likes this")
                return names[0]+" likes this";
            elif len(names) == 2:
                print(names[0]+" and "+names[1]+" like this")
                return names[0]+" and "+names[1]+" like this";
            elif len(names) == 3:
                print(names[0]+", "+names[1]+" and "+names[2]+" like this")
                return names[0]+", "+names[1]+" and "+names[2]+" like this";
            else:
                print(names[0]+", "+names[1]+" and "+str(len(names)-2)+" others like this")
                return names[0]+", "+names[1]+" and "+str(len(names)-2)+" others like this";
# ------------------------------------- better way-------------------------------------------------
    # formats = {
    #     0: "no one likes this",
    #     1: "{} likes this",
    #     2: "{} and {} like this",
    #     3: "{}, {} and {} like this",
    #     4: "{}, {} and {others} others like this"
    # }
    # n = len(names)
    # return formats[min(n,4)].format(*names, others=n-2)
# ------------------------------------------------------------------------------------------------

likes(["Alex", "Jacob", "Mark", "Max"])
