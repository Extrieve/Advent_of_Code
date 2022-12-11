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

    # Define a method to add a file to this node
    def add_file(self, name, size):
        # Add the file to the list of files
        file = File(name, size)
        self.files.append(file)

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
        # Set the current node to the new directory
        self.current = node

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
        self.current = self.root

    # Define a method to add a file to the current node
    def add_file(self, name, size):
        # Create a new file
        file = File(name, size)
        # Add the file to the current node
        self.current.add_file(file)

    # Define a method to print the tree
    def print_tree(self):
        # Create a list to store the nodes to print
        nodes = [self.root]
        # Loop while there are still nodes to print
        while nodes:
            # Get the next node to print
            node = nodes.pop(0)
            # Print the node name
            print(node.name)
            # Print the files in the node
            for file in node.files:
                print(f'  {file.name} ({file.size})')
            # Add the node's children to the list of nodes to print
            nodes.extend(node.children)


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
                tree.go_down(directory)
    else:
        command = command.split()
        if 'dir' in command:
            tree.current.add_child(Node(command[-1], tree.current))
        else:
            tree.current.add_file(command[1], command[0])

tree.print_tree()