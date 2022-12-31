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

# tail_spots = list()
# last_move = None
# for move in moves:
#     direction, positions = move.split()
#     print(direction, positions)
#     for i in range(int(positions)):

#         if hx != tx and hy != ty and (abs(hx - tx) > 1 or abs(hy - ty) > 1):
#             if hx < tx:
#                 tx = tx - 1 if tx > 0 else 4
#             else:
#                 tx = tx + 1 if tx < 4 else 0

#             if hy < ty:
#                 ty = ty - 1 if ty > 0 else 5
#             else:
#                 ty = ty + 1 if ty < 5 else 0

#             tail_spots.append(f'{tx} {ty}') if f'{tx} {ty}' not in tail_spots else None
#             # tx, ty = last_move

#         if direction == 'R':
#             last_move = [hx, hy]
#             hy = hy + 1 if hy < 5 else 0
#             # pmap[hx][hy], pmap[hx][hy + 1] = pmap[hx][hy + 1], pmap[hx][hy]

#             if hy - ty > 1 and hx == tx:
#                 ty = ty + 1 if ty < 5 else 0

#             tail_spots.append(f'{tx} {ty}') if f'{tx} {ty}' not in tail_spots else None

#         elif direction == 'L':
#             last_move = [hx, hy]
#             hy = hy - 1 if hy > 0 else 5
#             # pmap[hx][hy], pmap[hx][hy - 1] = pmap[hx][hy - 1], pmap[hx][hy]

#             if ty - hy > 1 and hx == tx:
#                 ty = ty - 1 if ty > 0 else 5

#             # tail_spots.add(f'{tx} {ty}')
#             tail_spots.append(f'{tx} {ty}') if f'{tx} {ty}' not in tail_spots else None

#         elif direction == 'U': 
#             last_move = [hx, hy]
#             hx = hx - 1 if hx > 0 else 4
#             # pmap[hx][hy], pmap[hx - 1][hy] = pmap[hx - 1][hy], pmap[hx][hy]

#             if tx - hx > 1 and hy == ty:
#                 tx = tx - 1 if tx > 0 else 4
            
#             tail_spots.append(f'{tx} {ty}') if f'{tx} {ty}' not in tail_spots else None
#             # tail_spots.add(f'{tx} {ty}')

#         else: 
#             last_move = [hx, hy]
#             hx = hx + 1 if hx < 4 else 0
#             # pmap[hx][hy], pmap[hx + 1][hy] = pmap[hx + 1][hy], pmap[hx][hy]

#             if hx - tx > 1 and hy == ty:
#                 tx = tx + 1 if tx < 4 else 0
#             tail_spots.append(f'{tx} {ty}') if f'{tx} {ty}' not in tail_spots else None
#             # tail_spots.add(f'{tx} {ty}')

#         print_map()

tail_spots = list()
last_move = None
for move in moves:
    direction, positions = move.split()
    print(direction, positions)
    for i in range(int(positions)):

        if direction == 'R':
            last_move = [hx, hy]
            hy = hy + 1 if hy < 5 else 0
            pmap[hx][hy], pmap[hx][last_move[1]] = pmap[hx][last_move[1]], pmap[hx][hy]

        elif direction == 'L':
            last_move = [hx, hy]
            hy = hy - 1 if hy > 0 else 5
            pmap[hx][hy], pmap[hx][last_move[1]] = pmap[hx][last_move[1]], pmap[hx][hy]

        elif direction == 'U': 
            last_move = [hx, hy]
            hx = hx - 1 if hx > 0 else 4
            pmap[hx][hy], pmap[last_move[0]][hy] = pmap[last_move[0]][hy], pmap[hx][hy]

        else: 
            last_move = [hx, hy]
            hx = hx + 1 if hx < 4 else 0
            pmap[hx][hy], pmap[last_move[0]][hy] = pmap[last_move[0]][hy], pmap[hx][hy]
        print_map()

        if abs(hx - tx) > 1 and hy == ty:
            tx += 1 if tx < hx else -1
        elif abs(hy - ty) > 1 and hx == tx:
            ty += 1 if ty < hy else -1
        elif abs(hx - tx) > 1 and hy != ty:
            tx += 1 if tx < hx else -1
            ty += 1 if ty < hy else -1
        elif abs(hy - ty) > 1 and hx != tx:
            ty += 1 if ty < hy else -1
            tx += 1 if tx < hx else -1
        else: pass

        tail_spots.append(f'{tx} {ty}') if f'{tx} {ty}' not in tail_spots else None

for move in tail_spots:
    move = list(map(int, move.split()))
    pmap[move[0]][move[1]] = 'T'

print_map()

# for move in moves:
#     direction, positions = move.split()
#     print(direction, positions)
#     for i in range(int(positions)):

#         if hx != tx and hy != ty and (abs(hx - tx) > 1 or abs(hy - ty) > 1):
#             tx = tx + 1 if tx < hx else tx - 1
#             ty = ty + 1 if ty < hy else ty - 1
#             tail_spots.append(f'{tx} {ty}') if f'{tx} {ty}' not in tail_spots else None
#             # tx, ty = last_move

#         if direction == 'R':
#             last_move = [hx, hy]
#             hy += 1 if hy + 1 <= 5 else 0
#             pmap[hx][hy], pmap[last_move[0]][last_move[1]] = pmap[last_move[0]][last_move[1]], pmap[hx][hy]

#             if hy - ty > 1 and hx == tx:
#                 ty += 1 if ty + 1 <= 5 else 0

#             tail_spots.append(f'{tx} {ty}') if f'{tx} {ty}' not in tail_spots else None

#         elif direction == 'L':
#             last_move = [hx, hy]
#             hy -= 1 if hy - 1 >= 0 else 0
#             pmap[hx][hy], pmap[last_move[0]][last_move[1]] = pmap[last_move[0]][last_move[1]], pmap[hx][hy]

#             if ty - hy > 1 and hx == tx:
#                 ty -= 1 if ty - 1 >= 0 else 0

#             # tail_spots.add(f'{tx} {ty}')
#             tail_spots.append(f'{tx} {ty}') if f'{tx} {ty}' not in tail_spots else None

#         elif direction == 'U': 
#             last_move = [hx, hy]
#             hx -= 1 if hx - 1 >= 0 else 0
#             pmap[hx][hy], pmap[last_move[0]][last_move[1]] = pmap[last_move[0]][last_move[1]], pmap[hx][hy]

#             if tx - hx > 1 and hy == ty:
#                 tx -= 1 if tx - 1 >= 0 else 0
            
#             tail_spots.append(f'{tx} {ty}') if f'{tx} {ty}' not in tail_spots else None
#             # tail_spots.add(f'{tx} {ty}')

#         else: 
#             last_move = [hx, hy]
#             hx += 1 if hx + 1 <= 4 else 0
#             pmap[hx][hy], pmap[last_move[0]][last_move[1]] = pmap[last_move[0]][last_move[1]], pmap[hx][hy]

#             if hx - tx > 1 and hy == ty:
#                 tx += 1 if tx + 1 <= 4 else 0
#             tail_spots.append(f'{tx} {ty}') if f'{tx} {ty}' not in tail_spots else None
#             # tail_spots.add(f'{tx} {ty}')

#         print_map()


print(tail_spots)
print(len(tail_spots))

