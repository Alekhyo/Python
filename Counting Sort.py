size=int(input("Enter the number of elements \n"))
l=[]
for i in range(0,size):
    num=int(input())
    l.append(num)

def countingsort(l):
    output = [0]*(len(l))
    count=[0]*(max(l)+1)
    for i in range(0,len(l)):
        count[l[i]]+=1

    for i in range(1,max(l)+1):
        count[i]=count[i]+count[i-1]

    for i in range(len(l)-1,-1,-1):
        count[l[i]]-=1
        output[count[l[i]]]=l[i]

    for i in range(0,len(l)):
        l[i]=output[i]

    print(l)
countingsort(l)
