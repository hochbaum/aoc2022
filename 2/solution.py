input = [line.rstrip() for line in open('./input.txt', 'r')]
draws = [tuple(line.split(' ')) for line in input]

draw_map = {
    'A': 'ROCK',
    'X': 'ROCK',
    'B': 'PAPER',
    'Y': 'PAPER',
    'C': 'SCISSORS',
    'Z': 'SCISSORS'
}
win_conds = [
    ('A', 'Y'), 
    ('B', 'Z'), 
    ('C', 'X')
]
shapes = {
    'ROCK': {
        'WEAKNESS': 'PAPER',
        'STRENGTH': 'SCISSORS',
        'SCORE': 1
    },
    'PAPER': {
        'WEAKNESS': 'SCISSORS',
        'STRENGTH': 'ROCK',
        'SCORE': 2
    },
    'SCISSORS': {
        'WEAKNESS': 'ROCK',
        'STRENGTH': 'PAPER',
        'SCORE': 3
    }
}

def part_one():
    score = 0
    for draw in draws:
        if draw in win_conds:
            score += 6
        elif draw_map[draw[0]] == draw_map[draw[1]]:
            score += 3   
        score += shapes[draw_map[draw[1]]]['SCORE']
    return score

def part_two():
    score = 0
    for draw in draws:
        opp = shapes[draw_map[draw[0]]]
        strat = draw[1]
        match strat:
            case 'X':
                score += shapes[opp['STRENGTH']]['SCORE']
            case 'Y':
                score += opp['SCORE'] + 3
            case 'Z':
                score += shapes[opp['WEAKNESS']]['SCORE'] + 6
    return score                  

print(f"Solution A: {part_one()}")
print(f"Solution B: {part_two()}")