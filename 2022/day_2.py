with open('day2.txt', 'r') as input:
    lines = input.readlines()
    lines = [line.strip() for line in lines]

# results = {
#     'X': {'loser': 'B Y', 'winner': 'C Z', 'score': 1},
#     'Y': {'loser': 'C Z', 'winner': 'A X', 'score': 2},
#     'Z': {'loser': 'A X', 'winner': 'B Y', 'score': 3},
#     'loser': 0,
#     'winner': 6,
#     'tie': 3
# }

rpz = {
    'A': {'lose': 'B', 'win': 'C', 'score': 1},
    'B': {'lose': 'C', 'win': 'A', 'score': 2},
    'C': {'lose': 'A', 'win': 'B', 'score': 3},
}

total_score = 0
for result in lines:
    opponent, outcome = result.split()
    if outcome == 'X':
        letter = rpz[opponent]['win']
        total_score += rpz[letter]['score']
        print(f'{letter=} {opponent=}')
    elif outcome == 'Y':
        total_score += 3
        total_score += rpz[opponent]['score']
        print(f'letter={opponent} {opponent=}')
    else:
        total_score += 6
        letter = rpz[opponent]['lose']
        total_score += rpz[letter]['score']
        print(f'{letter=} {opponent=}')

print(total_score)

    

# total_score = 0
# for result in lines:
#     opponent, ourselves = result.split()
#     total_score += results[ourselves]['score']
#     if opponent in results[ourselves]['loser']:
#         pass
#     elif opponent in results[ourselves]['winner']:
#         total_score += 6
#     else:
#         total_score += 3


# print(total_score)