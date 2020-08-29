def powering(num,power):
    '''
    Recursive function to calculate the Nth power of a number
    '''
    if power==1:    #Base Case
        return num

    elif power%2==0: #Even Power
        return (powering(num,power//2))**2
    else:  #Odd Power
        return ((powering(num, power//2)) ** 2)*num



result=powering(3,1023)
print(result)
