a=3
exp=8

def powering(a,power):
    if power==1:
        return a

    elif power%2==0:
        return (powering(a,power//2))**2
    else:
        return ((powering(a, power//2)) ** 2)*a



val=powering(3,3)
print(val)