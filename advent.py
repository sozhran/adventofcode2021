import wget

# DAY 1

# Challenge 1.1

day1_read_input = open('/users/john/MM/code/advent21/day1.txt', 'r')

day1_content = day1_read_input.read().split('\n')

day1_content_ints = [int(i) for i in day1_content]

ch11_count = 0

for i in range(len(day1_content) -1):
   if int(day1_content_ints[i] < day1_content_ints[i+1]):
       ch11_count += 1
        
print("Challenge 1.1 answer:", ch11_count)

# Challenge 1.2

# To simplify: Pattern repeats every 4 steps

# 1   A   C D     E   G H
# 2   A B   D     E F   H
# 3   A B C       E F G
# 4     B C D       F G H

# Also: A = E, B = F, C = G, D = H

a = 0
b = 0
c = 0
d = 0

for i in range(len(day1_content_ints)):
    if day1_content_ints[i] % 4 == 1:
        a += day1_content_ints[i]
        c += day1_content_ints[i]
        d += day1_content_ints[i]
    elif day1_content_ints[i] % 4 == 2:
        a += day1_content_ints[i]
        b += day1_content_ints[i]
        d += day1_content_ints[i]
    elif day1_content_ints[i] % 4 == 3:
        a += day1_content_ints[i]
        b += day1_content_ints[i]
        c += day1_content_ints[i]
    elif day1_content_ints[i] % 4 == 0:
        b += day1_content_ints[i]
        c += day1_content_ints[i]
        d += day1_content_ints[i]

# since A = E, B = F, C = G, D = H, we can save on variables
arr_12 = [a, b, c, d, a, b, c, d]
ch12_count = 0

for i in range(len(arr_12) - 1):
    if int(arr_12[i]) < int(arr_12[i+1]):
       ch12_count += 1

print("Challenge 1.2 answer:", ch12_count)