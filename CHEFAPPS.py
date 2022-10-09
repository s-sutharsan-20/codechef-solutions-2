# cook your code here
T=int(input())
for i in range(T):
    s,x,y,z=map(int,raw_input().strip().split())
    u=x+y #used space
    a_s=s-u #available space
    m=max(x,y)
    if m==x :
        a=s-y
    else :
        a=s-x
    
    if z<=a_s :
        print(0)
    elif z<=a :    
        print(1)
    else :
        print(2)