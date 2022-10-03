# cook your code here
for t in range(int(input())):
    p,q=list(map(int,raw_input().strip().split()))
    r = p + q
    s = r//2
    
    if s%2 == 0:
        print('Alice')
        
    else:
        print('Bob')
    
