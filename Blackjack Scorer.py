def score_hand(cards):
    score = 0
    A_score = 0
    list_num = []
    A_cnt = 0

    for i in range(len(cards)):
        print(cards[i])
        if (cards[i] != 'A'):
            if (cards[i] == 'J' or cards[i] == 'Q' or cards[i] == 'K'):
                list_num.append(10)
            else:
                list_num.append(int(cards[i]))
        else:
            A_cnt += 1


    for i in range(len(list_num)):
        if type(list_num[i]) is int :
            score = score+list_num[i]
    print("Before add A : {} ".format(score))

    A_score = score
    for i in range(A_cnt):
        if( (A_score+11) <= 21):
            A_score = A_score+11
        else:
            A_score = A_score+1
    if (A_score > 21):
        A_score = score + A_cnt
    print("After add A : {} ".format(A_score))



score_hand(["A", "A", "A", "J"])

# ////////////////////// Solution //////////////////////////////////////
# def score_hand(a):
#     n = sum(11 if x == "A" else 10 if x in "JQK" else int(x) for x in a)
#     for _ in range(a.count("A")):
#         if n > 21:
#             n -= 10
#     return n
