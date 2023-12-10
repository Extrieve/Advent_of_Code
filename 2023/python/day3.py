def main():
    with open('2023/python/day3_input.txt') as f:
        # create a list of the lines, remove the newline character
        lines = [line.rstrip('\n') for line in f]

    rows, cols = len(lines), len(lines[0])

    total = 0
    # part 1
    included_nums = []
    for i in range(rows):
        j = 0
        cols = len(lines[i])
        while j < cols:
            
            if not lines[i][j].isdigit():
                j += 1
                continue

            check_hash = False
            if j > 0 and lines[i][j-1] != '.' and not lines[i][j-1].isdigit() : # check left
                # print('left')
                check_hash = True
            elif j < cols-1 and lines[i][j+1] != '.' and not lines[i][j+1].isdigit(): # check right
                # print('right')
                check_hash = True
            elif i < rows-1 and lines[i+1][j] != '.' and not lines[i+1][j].isdigit(): # check down
                # print('down')
                check_hash = True
            elif i < rows-1 and j > 0 and lines[i+1][j-1] != '.' and not lines[i+1][j-11].isdigit(): # check down left
                # print('down left')
                check_hash = True
            elif i < rows-1 and j < cols-1 and lines[i+1][j+1] != '.' and not lines[i+1][j+1].isdigit(): # check down right
                # print('down right')
                check_hash = True
            elif i > 0 and j > 0 and lines[i-1][j-1] != '.' and not lines[i-1][j-1].isdigit(): # check up left
                # print('up left')
                check_hash = True
            elif i > 0 and j < cols-1 and lines[i-1][j+1] != '.' and not lines[i-1][j+1].isdigit(): # check up right
                # print('up right')
                check_hash = True
            elif i > 0 and lines[i-1][j] != '.' and not lines[i-1][j].isdigit(): # check up
                # print('up')
                check_hash = True
            
            
            if not check_hash:
                j += 1
                continue

            current_digit = [lines[i][j]]
            j_loop = j

            while j_loop > 0:
                if not lines[i][j_loop-1].isdigit():
                    break
                current_digit.insert(0, lines[i][j_loop-1])
                j_loop -= 1

            j_loop = j
            while j_loop < cols-1:
                # append at end
                if not lines[i][j_loop+1].isdigit():
                    j = j_loop + 1 if j_loop + 1 < cols else j_loop
                    break
                current_digit.append(lines[i][j_loop+1])
                j_loop += 1

            j = j_loop + 1 if j_loop + 1 < cols else j_loop
            j = j_loop + 1 if j_loop + 1 < cols else j_loop

            
            # print(current_digit)
            included_nums.append(int(''.join(current_digit)))


    print(sorted(included_nums))
    print('Part 1: {}'.format(sum(included_nums)))
if __name__ == '__main__':
    main()