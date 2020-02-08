def factors(n):
        flist=[]
        for i in range(1,n+1):
                if(n%i==0):
                        flist.append(i)

        return(flist)

def isprime(n):
        if(factors(n)==[1,n]):
                return(True)
        else:
                return(False)


def nprime(n):
        count=0
        i=1
        nplist=[]
        while(count<n):
                if(isprime(i)==True):
                        nplist.append(i)
                        count=count+1

                i=i+1
                

        return(nplist)
                        
                
        

        
