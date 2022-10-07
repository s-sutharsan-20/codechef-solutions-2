
T =int(raw_input())
for _ in range(T):
    result = 0
    num = str(raw_input())
    for word in num:
        result = result + int(word)
    print(result)    
        


