import re

with open('input.txt') as file:
    data = file.read()

data = [d for d in data.split('\n') if d]
crates = [[] for i in range(9)]
for crate in data[:8]:
    for i in range(1, len(crate), 4):
        if crate[i - 1] != ' ': crates[i // 4].append(crate[i])

print(crates)
moves = []
for move in data[9:]:
    numbers = re.findall(r'\d+', move)
    moves.append(list(map(int, numbers)))

for move in moves:
    quantity, initial, end = move
    quantity = quantity if quantity < len(crates[initial - 1]) else len(crates[initial - 1]) 
    # crates[end - 1].insert(0, crates[initial - 1].pop(0))
    crates[end - 1] = crates[initial - 1][: quantity] + crates[end - 1]
    del crates[initial - 1][: quantity]
    print(crates)

final = ''.join([s[0] for s in crates if s])
print(final)