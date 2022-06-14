n = int(input("輸入正數n"))
for i in range(1, n+1, 2):
    for j in range((n-i)//2,0,-1):
        print(" ",end="")
    print("*"*i)
for i in range(n-2, 0, -2):
    for j in range((n-i)//2,0,-1):
        print(" ",end="")
    print("*"*i)