with open('input.txt') as file:
    commands = file.read().split('\n')

directories = {'/': {}}
current = directories.get('/')

for command in commands:
    if command.startswith('$'):
        if 'cd' in command:

            directory = command.split()[-1]
            if '..' in directory:
                current = current['parent']
            elif '/' in directory:
                current = directories.get('/')
            else:
                current = current[directory]

    else:
        command = command.split()
        if 'dir' in command:
            current[command[-1]] = {'parent': current}
        else:
            current[command[1]] = command[0]


print(directories)

total_sum = 0
def access_all_children(dictionary):
    # if is instance of dict then iterate through it else print key, value
    if isinstance(dictionary, dict):
        for key, value in dictionary.items():
            if key != 'parent':
                access_all_children(value)
    else:
        print(dictionary, type(dictionary))
        global total_sum
        if int(dictionary) <= 100_000:
            total_sum += int(dictionary)

access_all_children(directories.get('/'))
print(total_sum)