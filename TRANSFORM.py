# cook your code here
T=int(input())
for i in range(0,T):
    x=int(input())
    if x%3==0 :
        print("NORMAL")
    elif x%3==2 :
        print("SMALL")
    else :
        print("HUGE")