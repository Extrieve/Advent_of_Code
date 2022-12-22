with open('input.txt') as file:
    commands = file.read().split('\n')

class Node:
    def __init__(self, name, parent=None):
        # Store the name of the node
        self.name = name
        # Store the parent node
        self.parent = parent
        # Create an empty list to store child nodes
        self.children = []
        # Create an empty list to store files
        self.files = []

    # Define a method to add a child node to this node
    def add_child(self, child):
        # Add the child node to the list of children
        self.children.append(child)

    def add_file(self, name, size):
        self.files.append(File(name, int(size)))

    def directory_size(self):
        return sum([file.size for file in self.files])

    def total_directory_size(self):
        total = self.directory_size()
        for child in self.children:
            total += child.total_directory_size()
        return total

    # Define a method to represent the node as a string
    def __repr__(self):
        # Return the node name and its parent and children
        return f'Node({self.name}, {self.parent}, {self.children})'


# Define a File class to represent a file in the tree
class File:
    def __init__(self, name, size):
        # Store the name of the file
        self.name = name
        # Store the size of the file
        self.size = size

    # Define a method to represent the file as a string
    def __repr__(self):
        # Return the file name and size
        return f'File({self.name}, {self.size})'


# Define a Tree class to represent the directory tree
class Tree:
    def __init__(self):
        # Create a root node with the name '/'
        self.root = Node('/')
        # Set the current node to the root node
        self.current = self.root

    # Define a method to add a directory to the current node
    def add_directory(self, name):
        # Create a new node for the directory
        node = Node(name, self.current)
        # Add the new node to the current node's children
        self.current.add_child(node)

    # Define a method to go up one level in the tree
    def go_up(self):
        # Set the current node to its parent
        self.current = self.current.parent

    def go_down(self, name):
        if self.current.children is None:
            print('No children')
        else:
            for child in self.current.children:
                if child.name == name:
                    self.current = child
                    break

    def go_to_root(self):
        while self.current.parent is not None:
            self.current = self.current.parent

    # Define a method to add a file to the current node
    def add_file(self, name, size):
        self.current.add_file(name, int(size))

    # Define a method to print the tree, print a node and its children recursively
    def print_tree(self, node=None, level=0):
        # If no node is passed in, start with the root node
        if node is None:
            node = self.root

        # Print the node name and its files
        print(' ' * level + node.name, node.files)

        # Print the children of the node
        for child in node.children:
            self.print_tree(child, level + 1)

# Create a new tree
tree = Tree()

for command in commands:
    if command.startswith('$'):
        if 'cd' in command:
            directory = command.split()[-1]
            if '..' in directory:
                tree.go_up()
            elif '/' in directory:
                tree.go_to_root()
            else:
                # print('Changed directory:', directory)
                tree.go_down(directory)
                # print('Current Node:', tree.current.name, '\n')
    else:
        command = command.split()
        if 'dir' in command:
            # print('Added directory:', command[-1], 'in', tree.current.name)
            tree.current.add_child(Node(command[-1], tree.current))
        else:
            tree.add_file(command[1], command[0])


max_space, update_size = 70_000_000, 30_000_000
space_needed = max_space - tree.root.total_directory_size()
print('Space Needed:', space_needed)

qualified_directories = []
def access_all_children(node):
    if node.total_directory_size() >= space_needed:
        qualified_directories.append(node.total_directory_size())
    for child in node.children:
        access_all_children(child)

min_node = None
def minumum_viable_space(node):
    global min_node
    if min_node is None:
        min_node = node

    if node.total_directory_size() < min_node.total_directory_size() and node.total_directory_size() >= space_needed:
        min_node = node

    for child in node.children:
        minumum_viable_space(child)


minumum_viable_space(tree.root)
total = 0
least = None
for child in sorted(min_node.children, key=lambda x: x.total_directory_size())[2:]:
    print(child.name, child.total_directory_size())
    total += child.total_directory_size() if child.total_directory_size() < space_needed - total else 0
    least = child
print('Minimum Viable Space:', min_node.total_directory_size())
print()
for child in sorted(least.children, key=lambda x: x.total_directory_size(), ):
    print(child.name, child.total_directory_size())
    total += child.total_directory_size() if child.total_directory_size() < space_needed - total else 0

print(total)

# tst = tree.root.children
# for child in tst:
#     qualified_directories.append((child, child.total_directory_size()))

# best = sorted(qualified_directories, key=lambda x: x[1])[-1]
# candidates = best[0].children
# ts = []
# for child in candidates:
#     amount = child.total_directory_size()
#     ts.append(amount)
#     print(amount)

# print(sum(sorted(ts)[2:]))

# access_all_children(tree.root)
# print(sorted(qualified_directories))