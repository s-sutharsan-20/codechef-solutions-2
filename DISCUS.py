# cook your code here
T=int(input())
for i in range(T):
    a,b,c =map(int,raw_input().strip().split())
    l=[a,b,c]
    print(max(l))