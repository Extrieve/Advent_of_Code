with open('input.txt') as file:
    moves = file.read().split('\n')

counter, X = 0, 1
sprites = []
for move in moves:
    move = move.split()
    if len(move) > 1:
        for i in range(2):
            print(f'Starting at {counter} and moving {move[1]} X IS {X=}')
            counter += 1
            sprites.append('#' if abs(X - counter) <= 1 else '.')
            if i % 2 != 0: X += int(move[1])
            print(f'Ending at {counter} and moving {move[1]} X IS {X=}')
    else:
        print(f'Starting at {counter} and moving {move[0]} times')
        counter += 1
        sprites.append('#' if abs(X - counter) <= 1 else '.')
        print(f'Starting at {counter} and moving {move[0]} times')


# change my 1d list of 240 sprites to a 2d list of 6 rows of 40 sprites
sprites = [sprites[i:i+40] for i in range(0, len(sprites), 40)]
for sprite in sprites:
    print(''.join(sprite))