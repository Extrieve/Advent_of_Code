with open('2021/input.txt', 'r') as f:
    data = f.read().split('\n')

x, y = 0, 0

for line in data:
    command, moves = line.split(' ')
    if 'forward' in command:
        x += int(moves)
    elif 'down' in command:
        y += int(moves)
    else:
        y -= int(moves)

print(x, y, x * y)