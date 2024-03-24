## Data preparation

day1_read_file = open('./day1.txt', 'r')
day1_content = day1_read_file.read().split('\n')
day1_input = [int(i) for i in day1_content]

day2_read_file = open('./day2.txt', 'r')
day2_input = day2_read_file.read().split('\n')

day3_read_file = open('./day3.txt', 'r')
day3_input = day3_read_file.read().split('\n')

# DAY 1

# Challenge 1.1

ch11_count = 0

for i in range(len(day1_content) -1):
   if int(day1_input[i] < day1_input[i+1]):
       ch11_count += 1
        
print("Challenge 1.1 answer:", ch11_count)

# Challenge 1.2

# Ok, we basically need to compare (i + i+1 + i+2) vs (i+1 + i+2 + i+3)
# We can simplify it to (i) vs (i+3)

ch12_count = 0

for i in range(0, len(day1_input) - 3):
    if day1_input[i+3] > day1_input[i]:
        ch12_count += 1

print("Challenge 1.2 answer:", ch12_count)

# DAY 2

# Challenge 2.1

ch21_count_horizontal = 0
ch21_count_depth = 0

for line in day2_input:
    if line[0] == "f":
        ch21_count_horizontal += int((line.split(' ')[1]))
    if line[0] == "d":
        ch21_count_depth += int((line.split(' ')[1]))
    if line[0] == "u":
        ch21_count_depth -= int((line.split(' ')[1]))

print("Challenge 2.1 answer:", ch21_count_horizontal * ch21_count_depth)

# Challenge 2.2
        
ch22_count_horizontal = 0
ch22_count_aim = 0
ch22_count_depth = 0

for line in day2_input:
    if line[0] == "f":
        ch22_count_horizontal += int((line.split(' ')[1]))
        ch22_count_depth += (ch22_count_aim * int((line.split(' ')[1])))
    if line[0] == "d":
        ch22_count_aim += int((line.split(' ')[1]))
    if line[0] == "u":
        ch22_count_aim -= int((line.split(' ')[1]))

print("Challenge 2.2 answer:", ch22_count_horizontal * ch22_count_depth)
        
# DAY 3

# Challenge 3.1
        
# Since the task is basically to find out whether 1's or 0' dominate in each column,
# I count the sum of each column (which will also be the sum of 1's) and check if the 1's
# make up more than half of the column, and assign values accordingly.
        
gamma = ""
epsilon = ""
input3_length = len(day3_input[0])
ch31_counter = 0

for i in range(input3_length):

    for elm in day3_input:
        ch31_counter += int(elm[i])
    if ch31_counter > (len(day3_input) / 2):
        gamma += "1"
        epsilon += "0"
    else:
        gamma += "0"
        epsilon += "1"
    ch31_counter = 0

print("Challenge 3.1 answer:", int(gamma, 2) * int(epsilon, 2))

# Challenge 3.2

oxygen = 0
scrubber = 0
input3_length = len(day3_input[0])
ch32_counter = 0

for i in range(input3_length):
    for elm in day3_input:
        ch31_counter += int(elm[i])
    if ch31_counter > (len(day3_input) / 2):