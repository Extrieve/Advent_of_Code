with open('2021/input.txt', 'r') as f:
    data = f.read().split('\n')

x, y, aim = 0, 0, 0

for line in data:
    command, moves = line.split(' ')
    moves = int(moves)
    if 'forward' in command:
        x += moves
        y += moves * aim
    elif 'down' in command:
        aim += moves
        # y += moves
    else:
        aim -= moves
        # y -= moves

print(x, y, x * y)