ans = input("解答")
guess_num = input("幾a幾b")
while guess_num != "0000":
    a, b = 0, 0
    for num in guess_num:
        if num in ans:
            if guess_num.index(num) == ans.index(num):
                a += 1
            else:
                b += 1
    print(f"{a}A{b}B")
    guess_num = input("幾a幾b")