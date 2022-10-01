# cook your code here
T=int(input())
for i in range(T):
    x,y=map(int,raw_input().strip().split())
    if x>y :
        print(x-y)
    else :
        print(y-x)