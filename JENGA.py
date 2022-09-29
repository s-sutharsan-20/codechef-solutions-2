# cook your dish here
T=int(input())
for i in range(T):
    n,x=map(int,input().split())
    if n<=x and x%n==0 :
        print("YES")
    else :
        print("NO")