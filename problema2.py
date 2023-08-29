def retRight(IN):
    try:
        return int(IN)
    except:
        return IN
      
print(tuple(retRight(x) for x in reversed(input().split(' '))))
