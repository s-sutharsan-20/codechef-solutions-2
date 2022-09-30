# cook your code here
T=int(input())
for i in range(T):
    a,b,c,d=map(int,raw_input().strip().split())
    x=max(a,b)
    y=max(c,d)
    print(x+y)