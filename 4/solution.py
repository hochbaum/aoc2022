input = [line.rstrip() for line in open('./input.txt', 'r')]

def parse_pairs(line):
    return line.split(',')

def parse_range(pair):
    return list(map(int, tuple(pair.split('-'))))

def contains_either(r1, r2):
    return (r1[0] <= r2[0] and r1[1] >= r2[1]) or (r2[0] <= r1[0] and r2[1] >= r1[1])

def overlaps_either(r1, r2):
    return (r1[0] <= r2[0] and r1[1] >= r2[0]) or (r1[1] >= r2[1] and r1[0] <= r2[1]) \
        or (r2[0] <= r1[0] and r2[1] >= r1[0]) or (r2[1] >= r1[1] and r2[0] <= r1[1])        

contains = 0
overlaps = 0

for line in input:
    pairs = parse_pairs(line)
    range1 = parse_range(pairs[0])
    range2 = parse_range(pairs[1])
    if contains_either(range1, range2): contains += 1
    if overlaps_either(range1, range2): overlaps += 1    
    
print(f'Solution A: {contains}')
print(f'Solution B: {overlaps}')