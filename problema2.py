def removeStrangeComma(tup):
    if len(tup) == 1:
        print('('+str(tup[0])+')')
    else:
        print(tup)

removeStrangeComma(tuple(reversed(input().split(' '))))
