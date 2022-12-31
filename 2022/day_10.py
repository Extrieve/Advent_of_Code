with open('input.txt') as file:
    moves = file.read().split('\n')

counter, X = 0, 1
signals = []
for move in moves:
    move = move.split()
    if len(move) > 1:
        for i in range(2):
            counter += 1
            signal_strength = X * counter
            if i % 2 != 0: X += int(move[1])
            signals.append(signal_strength)
    else:
        counter += 1
        signal_strength = X * counter
        signals.append(signal_strength)
            
print(sum([signals[19], signals[59], signals[99], signals[139], signals[179], signals[219]]))