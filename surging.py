def abc(number):
    if number<=0:
        return False
    return (number & (number-1))==0
n=int(input("enter a number"))
if abc(n):
    print ("power of 2")
else:
    print("invalid number")