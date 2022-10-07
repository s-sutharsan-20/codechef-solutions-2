
x, y = map(float, raw_input().split())
if x%5==0 and y-.5>=x:
    print(format(y-x-0.50,".2f"))
else:
    print(format(y,".2f"))
