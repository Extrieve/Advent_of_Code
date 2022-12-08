with open('input.txt') as input:
    trees = input.read().split('\n')

height, width = len(trees), len(trees[0])

def find_first_index(iterator, value):
    return next((i + 1 for i, num in enumerate(iterator) if value <= num), len(iterator))

# visible_trees = height * 2 + width * 2 - 4
visible_trees = 1

tree_columns = [list(column) for column in zip(*trees)] # Transpose
print('\n'.join(trees))

for i in range(1, height - 1):
    for j in range(1, width - 1):
        current = trees[i][j]
        ### PART 1
        # print(current, tree_columns[j][:i+1])
        # if current > max(tree_columns[j][:i]): # UP
        #     visible_trees += 1
        #     continue
        # elif current > max(tree_columns[j][i+1:]): # DOWN
        #     visible_trees += 1
        #     continue
        # elif current > max(trees[i][:j]): # LEFT
        #     visible_trees += 1
        #     continue
        # elif current > max(trees[i][j+1:]): # RIGHT
        #     visible_trees += 1
        #     continue
        # else:
        #     continue

        ### PART II
        up_count, down_count, left_count, right_count = 0, 0, 0, 0

        up = tree_columns[j][:i].copy()
        up = up[::-1]
        up_count += find_first_index(up, current)

        down = tree_columns[j][i+1:]
        down_count += find_first_index(down, current)

        left = trees[i][:j]
        left = left[::-1]
        left_count += find_first_index(left, current)

        right = trees[i][j+1:]
        right_count += find_first_index(right, current)

        local_product = up_count * down_count * left_count * right_count
        visible_trees = max(visible_trees, local_product)

print(visible_trees)