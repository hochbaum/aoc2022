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
    your_score = 0
    for draw in draws:
        if draw in win_conds:
            your_score += 6
        elif draw_map[draw[0]] == draw_map[draw[1]]:
            your_score += 3   
        your_score += shapes[draw_map[draw[1]]]['SCORE']
    return your_score

def part_two():
    your_score = 0
    for draw in draws:
        opp_shape = shapes[draw_map[draw[0]]]
        strat = draw[1]
        match strat:
            case 'X':
                your_score += shapes[opp_shape['STRENGTH']]['SCORE']
            case 'Y':
                your_score += opp_shape['SCORE']
            case 'Z':
                your_score += shapes[opp_shape['WEAKNESS']]['SCORE']
    return your_score                  

print(f"Solution A: {part_one()}")
print(f"Solution B: {part_two()}")