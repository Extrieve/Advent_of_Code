import string

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
all_letters = lowercase + uppercase

with open('input.txt') as f:
    data = f.read()

data = data.split('\n')
common_sum = 0
# for line in data:
#     first_half = line[:len(line)//2]
#     second_half = line[len(line)//2:]
#     for letter in first_half:
#         if letter in second_half:
#             common_sum += all_letters.index(letter) + 1
#             break

# print(common_sum)
for i in range(0, len(data), 3):
    item1, item2, item3 = set(data[i]), set(data[i + 1]), set(data[i + 2])
    unique = item1.intersection(item2, item3)
    common_sum += all_letters.index(list(unique)[0]) + 1

print(common_sum)
    