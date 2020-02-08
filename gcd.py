m=14
n=63
lm=[]
ln=[]
cf=[]
for i in range(1,m+1):
    if (m%i)==0:
        lm.append(i)

for j in range(1,n+1):
    if (n%j)==0:
        ln.append(j)

for x in lm:
    if x in ln:
        cf.append(x)

print(cf[-1])
        
