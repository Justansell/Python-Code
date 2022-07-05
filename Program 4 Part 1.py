#A. Create a loop that will output all the positive multiples of 9 that are less than 99.

num = 0
mult_num = 0
while mult_num < 99:
    num += 1
    mult_num = num * 9
    if mult_num < 99:
        print(mult_num, end=' ')
print("'A'")

#B. Create a loop that will output all the positive numbers less than 200 that are evenly divisible by both 3 and 7.

num = 0
div_num = 0
while div_num < 200:
    num += 1
    div_num = num * 3 * 7
    if div_num < 200:
        print(div_num, end=' ')
print("'B'")

#C. Create a loop that will calculate the sum of the positive multiples of 8 that are between 100 and 500. Output the sum.

all_nums = (range(100, 501, 8))
total = 0
for num in all_nums:
    total += num
print(total, end=' ')
print("'C'")
