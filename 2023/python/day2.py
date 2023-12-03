from math import prod


def part1(line: str, pre_reqs: dict):
    bags = line.split(';')
    for bag in bags:
        items = bag.split(',')
        for item in items:
            number, color = item.split(' ')[1:]
            if int(number) > pre_reqs[color]:
                return False
            
    return True

def part2(line: str):
    bags = line.split(';')
    cube_mins = {'blue': 0, 'red': 0, 'green': 0}
    for bag in bags:
        items = bag.split(',')
        for item in items:
            number, color = item.split(' ')[1:]
            if int(number) > cube_mins[color]:
                cube_mins[color] = int(number)

    return prod(cube_mins.values())


# def main():
#     # txt input from day2_input.txt
#     with open('2023/python/day2_input.txt') as f:
#         # create a list of the lines, remove the newline character
#         lines = [line.rstrip('\n') for line in f]

#     pre_reqs = {'blue': 14, 'red': 12, 'green': 13}
#     valid_ids = 0
#     for line in lines:
#         game_id, line = line.split(':')
#         game_id = int(game_id.split(' ')[1])
#         if part1(line, pre_reqs):
#             valid_ids += game_id

#     print(valid_ids)

def main():
    # txt input from day2_input.txt
    with open('2023/python/day2_input.txt') as f:
        # create a list of the lines, remove the newline character
        lines = [line.rstrip('\n') for line in f]

    sum_of_powers = 0
    for line in lines:
        game_id, line = line.split(':')
        game_id = int(game_id.split(' ')[1])
        sum_of_powers += part2(line)

    print(sum_of_powers)

if __name__ == '__main__':
    main()