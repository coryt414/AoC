# A  = Rock        |  1
# B  = Paper       |  2
# C  = Scissors    |  3

# X  = Lose
# Y = Tie
# Z = Win

# Lose                |  0
# Tie                 |  3
#Win                  |  6


# Scoring
# Total score = sum of all rounds
# Single round score = shape thrown score (1, 2, 3) + outcome (0, 3, 6)

def round_score(filename):
    with open(filename, "r") as file:
        total_score = 0
        for line in file:
            shapes_played = line.strip().split(" ")
            print(shapes_played)
            total_score += round_calculator(shapes_played[0], shapes_played[1])
        print("Score: " + str(total_score))


def round_calculator(opponent, outcome):
    score = 0
    if opponent == 'A':
        opponent = 1
    if opponent == 'B':
        opponent = 2
    if opponent == 'C':
        opponent = 3
    if outcome == 'X':
        outcome = 1
    if outcome == 'Y':
        outcome = 2
    if outcome == 'Z':
        outcome = 3
    
    # Lose
    if outcome == 1:
        score = 0
        if opponent == 1:
            score += 3
        if opponent == 2:
            score += 1
        if opponent == 3:
            score += 2
        return score
    # Tie
    if outcome == 2:
        score = 3
        if opponent == 1:
            score += 1
        if opponent == 2:
            score += 2
        if opponent == 3:
            score += 3
        return score
    
    # Win
    if outcome == 3:
        score = 6
        if opponent == 1:
            score += 2
        if opponent == 2:
            score += 3
        if opponent == 3:
            score += 1       
        return score


round_score("Day 2\Day2_Input.txt")