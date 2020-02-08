def findpos(l,v):
    pos=-1
    i=0
    for x in l:
        if(x==v):
            pos=i
            break
        i=i+1
    return(pos)
