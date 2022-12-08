# from treelib import Node, Tree

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