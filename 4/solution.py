input = [line.rstrip() for line in open('./input.txt', 'r')]
pairs = [[(int(i[0]), int(i[1])) for i in [num.split('-') for num in rng]] \
    for rng in [line.split(',') for line in input]]

def contains_either(r1, r2):
    return (r1[0] <= r2[0] and r1[1] >= r2[1]) or (r2[0] <= r1[0] and r2[1] >= r1[1])

def overlaps_either(r1, r2):
    return (r1[0] <= r2[0] and r1[1] >= r2[0]) or (r1[1] >= r2[1] and r1[0] <= r2[1]) \
        or (r2[0] <= r1[0] and r2[1] >= r1[0]) or (r2[1] >= r1[1] and r2[0] <= r1[1])          

contains = len([pair for pair in pairs if contains_either(pair[0], pair[1])])
overlaps = len([pair for pair in pairs if overlaps_either(pair[0], pair[1])])
print(f'Solution A: {contains}')
print(f'Solution B: {overlaps}')