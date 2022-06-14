num_list = list(map(int,input().split(",")))
biggest = 0
for idx1 in range(len(num_list)):
     for idx2 in range(idx1+1, len(num_list)):
         num1, num2 = max(num_list[idx1], num_list[idx2]), min(num_list[idx1], num_list[idx2])
         while num2:
             t = num2
             num2 = num1 % num2
             num1 = t
         if num1 > biggest: biggest = num1

print(biggest)