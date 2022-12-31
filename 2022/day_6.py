with open('input.txt') as input:
    string = input.read().lstrip().rstrip()


for i in range(14, len(string)):
    if len(set(string[i-14:i])) == 14:
        print(i)
        break