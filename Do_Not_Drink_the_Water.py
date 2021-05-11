# ======================
# |   Density Chart    |
# ======================
# | Honey   | H | 1.36 |
# | Water   | W | 1.00 |
# | Alcohol | A | 0.87 |
# | Oil     | O | 0.80 |
# ----------------------

# [                            [
#  ['H', 'H', 'W', 'O'],        ['O','O','O','O']
#  ['W', 'W', 'O', 'W'],  =>    ['W','W','W','W']
#  ['H', 'H', 'O', 'O']         ['H','H','H','H']
#  ]                           ]

def number_replace(var):
    if var=='H': 
        return 1.36
    elif var=='W': 
        return 1.00 
    elif var=='A': 
        return 0.87
    else: 
        return 0.80

def char_replace(var):
    if var==1.36: 
        return 'H'
    elif var==1.00: 
        return 'W' 
    elif var==0.87: 
        return 'A'
    else: 
        return 'O'

def separate_liquids(glass):
    if not glass:
        return []
    # To list of number
    join_list = [number_replace(j) for i in glass for j in i]
    # Sort list of number
    join_list.sort()
    print('Log Int List :',join_list)
    # Back to list of word
    join_list = [char_replace(i) for i in join_list]
    # Reshape list 
    ans_list = [join_list[i:i+len(glass[0])] for i in range(0,len(join_list),int(len(join_list)/len(glass)))]
    print('Log Ans List :',ans_list)
    return ans_list


separate_liquids([['H', 'H', 'W', 'O'],['W','W','O','W'],['H','H','O','O']])