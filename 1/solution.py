input = [line.rstrip() for line in open('./input.txt', 'r')]
cals = [0]

for line in input:
    if line == "": 
        cals.append(0)
    else:
        cals[-1] = cals[-1] + int(line)

cals.sort()
print(f'Solution A: {cals[-1]}')
print(f'Solution B: {cals[-1] + cals[-2] + cals[-3]}')