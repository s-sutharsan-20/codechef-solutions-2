# cook your code here
T=int(input())
for i in range(T):
    x,y,d=map(int,raw_input().split())
    a=x-y
    if abs(a)<=d :
        print("YES")
    else :
        print("NO")