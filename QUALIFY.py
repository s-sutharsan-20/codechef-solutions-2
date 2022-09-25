# cook your dish here
T=int(input())
for i in range(0,T):
    x,a,b=map(int,input().split())
    e=a*1
    h=b*2
    s=e+h
#    print(s)
    if s>=x :
        print("Qualify")
        
    else :
        print("NotQualify")