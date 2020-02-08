num=int(input("Enter the number \n"))
n=len(str(num))
print(n)

sum=0

temp=num

while temp>0:
  a=temp%10
  sum+=a**n
  
  temp=int(temp/10)

if(sum==num):
    print('armstrong')
else:
        print('no')

