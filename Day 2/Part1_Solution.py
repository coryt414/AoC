# A | X = Rock        |  1
# B | Y = Paper       |  2
# C | Z = Scissors    |  3

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
            shapes_played = line.strip("\n")
            shapes_played = shapes_played.split(" ")
            print(shapes_played)
            total_score += round_calculator(shapes_played[0], shapes_played[1])
            if shapes_played[1].strip() == 'X':
                total_score += 1
            if shapes_played[1].strip() == 'Y':
                total_score += 2
            if shapes_played[1].strip() == 'Z':
                total_score += 3
        print("Score: " + str(total_score))


def round_calculator(opponent, player):
    score = 0
    if opponent == 'A':
        opponent = 1
    if opponent == 'B':
        opponent = 2
    if opponent == 'C':
        opponent = 3
    if player == 'X':
        player = 1
    if player == 'Y':
        player = 2
    if player == 'Z':
        player = 3
    # Tie
    if opponent == player:
        score = 3
        return score
    
    # Lose
    if (opponent == 1 and player == 3) | (opponent == 2 and player == 1) | (opponent == 3 and player == 2):
        score = 0
        return score
    
    # Win
    if (opponent == 1 and player == 2) | (opponent == 2 and player == 3) | (opponent == 3 and player == 1):
        score = 6
        return score


round_score("Day 2\Day2_Input.txt")