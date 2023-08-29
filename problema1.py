def retRight(IN):
    try:
        return int(IN)
    except:
        return IN

t1 = tuple([retRight(x) for x in input().split(' ')])
t2 = tuple([retRight(x) for x in input().split(' ')])

print(t2+t1+t2)
