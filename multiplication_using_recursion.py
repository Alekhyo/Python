a=2
b=3

def multiply(a,b):
    if b==1:
        return a

    return (a+multiply(a,b-1))

result=multiply(2,13)
print(result)
