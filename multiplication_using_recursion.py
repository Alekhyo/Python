def multiply(a,b):
    if b==1:   #Base Case
        return a

    return (a+multiply(a,b-1))

result=multiply(2,13)
print(result)
