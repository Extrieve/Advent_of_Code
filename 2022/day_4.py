with open('input.txt', 'r') as file:
    data = file.read().split('\n')


count = 0
# for assignments in data:
#     elf1, elf2 = assignments.split(',')
#     elf1_low, elf1_high = [int(n) for n in elf1.split('-')]
#     elf2_low, elf2_high = [int(n) for n in elf2.split('-')]

#     if elf1_low >= elf2_low and elf1_high <= elf2_high:
#         count += 1
#     elif elf1_low <= elf2_low and elf1_high >= elf2_high:
#         count += 1
#     else:
#         pass

for assignments in data:
    elf1, elf2 = assignments.split(',')
    elf1_low, elf1_high = [int(n) for n in elf1.split('-')]
    elf2_low, elf2_high = [int(n) for n in elf2.split('-')]

    if elf2_low > elf1_high or elf1_low > elf2_high: pass
    else: count += 1
    
print(count)