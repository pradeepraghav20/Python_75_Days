num=32
def happy_number(num):
    sum=0
    while(num>0):
        temp=num%10
        sum+=temp**2
        num=num//10


    if sum==1:
        print ("Yess Nmber is haapy number")
    elif (sum>9):
        happy_number(sum)
    else:
        print(sum)
    # elif sum>9:
    #     happy_number(sum)
    # else:
    #     print("Not Happy Number")


happy_number(31)