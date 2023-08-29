def retRight(IN):
    try:
        return int(IN)
    except:
        return IN

def removeStrangeComma(tup):
    if len(tup) == 1:
        print('('+str(tup[0])+')')
    else:
        print(tup)

t1 = tuple([retRight(x) for x in input().split(' ') if x != ''])
t2 = tuple([retRight(x) for x in input().split(' ') if x != ''])

removeStrangeComma(t2+t1+t2)
