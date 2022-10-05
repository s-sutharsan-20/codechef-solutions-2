t = int(input())
for i in range(0,t):
    num = int(input())
    fact = 1
    for j in range(2,num+1):
        fact = fact*j
    print(fact)


