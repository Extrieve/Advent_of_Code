with open('2021/input.txt', 'r') as f:
    data = f.read().split('\n')

current = data[0]
counter = 0
for measurement in data[1:]: 
    print(measurement, current) 
    if measurement > current: counter += 1
    current = measurement
print(counter)