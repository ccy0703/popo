ans = 0
for i in range(int(input("班級的數量"))):
    student = int(input("每班人數"))
    if student > ans: ans = student
print(ans)