# cook your code
T=int(input())
for i in range(T):
    x1,y1,x2,y2=map(int,raw_input().strip().split())
    x=x1-x2
    y=y1-y2
    l=[abs(x),abs(y)]
    print(max(l))