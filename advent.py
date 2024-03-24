# DAY 1

# Challenge 1.1

day1_read_file = open('./day1.txt', 'r')

day1_content = day1_read_file.read().split('\n')

day1_input = [int(i) for i in day1_content]

ch11_count = 0

for i in range(len(day1_content) -1):
   if int(day1_input[i] < day1_input[i+1]):
       ch11_count += 1
        
print("Challenge 1.1 answer:", ch11_count)

# Challenge 1.2

# Ok, we basiccaly need to compare (i + i+1 + i+2) vs (i+1 + i+2 + i+3)
# We can simplify it to (i) vs (i+3)

ch12_count = 0

for i in range(0, len(day1_input) - 3):
    if day1_input[i+3] > day1_input[i]:
        ch12_count += 1

print("Challenge 1.2 answer:", ch12_count)