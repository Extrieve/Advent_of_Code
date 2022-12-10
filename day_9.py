with open('input.txt') as file:
    moves = file.read().split('\n')

pmap = [['.' for _ in range(6)] for i in range(4)]
pmap.append(['H', '.', '.', '.', '.', '.'])

def print_map():
    for row in pmap:
        print(''.join(row))
    print()

hx, hy = 4, 0
tx, ty = 4, 0

tail_spots = set()

for move in moves:
    direction, positions = move.split()
    for i in range(int(positions)):
        if direction == 'R':
            pmap[hx][hy], pmap[hx][hy + 1] = pmap[hx][hy + 1], pmap[hx][hy]
            hy += 1

            if hy - ty > 1:
                ty += 1

            tail_spots.add(f'{tx} {ty}')
        elif direction == 'L':
            pmap[hx][hy], pmap[hx][hy - 1] = pmap[hx][hy - 1], pmap[hx][hy]
            hy -= 1

            if ty - hy > 1:
                ty -= 1

            tail_spots.add(f'{tx} {ty}')
            
        elif direction == 'U': 
            pmap[hx][hy], pmap[hx - 1][hy] = pmap[hx - 1][hy], pmap[hx][hy]
            hx -= 1

        else: 
            pmap[hx][hy], pmap[hx + 1][hy] = pmap[hx + 1][hy], pmap[hx][hy]
            hx += 1

        print_map()
        

