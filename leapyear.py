year=int(input("Enter the year \n"))
if year%100==0 and year%400==0:
    print("LEAP YEAR")
elif year%100!=0 and year%4==0:
    print("LEAP YEAR")
else:
    print("NOT A LEAP YEAR")
    
