input = [line.rstrip() for line in open('./input.txt', 'r')]

def split(str):
    return (str[slice(0, len(str) // 2)], str[slice(len(str) // 2, len(str))])

def priority(char: str):
    return ord(char) - 38 if char.isupper() else ord(char) - 96

def process(ruck):
    comps = split(ruck)
    return sum([priority(char) for char in set(comps[0]) if char in comps[1]])

groups = [input[i:i+3] for i in range(0, len(input), 3)]
group_prios = [[priority(char) for char in set(group[0]) if char in group[1] and char in group[2]] for group in groups]

print(f'Solution A: {sum([process(ruck) for ruck in input])}')
print(f'Solution B: {sum(map(sum, group_prios))}')