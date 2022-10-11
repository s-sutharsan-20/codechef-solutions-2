# cook your code here
T=int(input())
for i in range(T):
    n,x,p=map(int,raw_input().strip().split())
    cm=x*3
    wa=n-x
    tm=cm-wa
    if tm>=p :
        print("PASS")
    else :
        print("FAIL")