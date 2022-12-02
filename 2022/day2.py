score_map = {
    # rock
    "rock": 1,
    # paper
    "paper": 2,
    # scissor
    "scissor": 3
}


def map_game(s):
    match s:
        case "Y" | "B":
            return "paper"
        case "X" | "A":
            return "rock"
        case "Z" | "C":
            return "scissor"

# A - rock
# B - paper
# C - scissor


def run_game(opponent, you):
    selection_score = score_map[you]
    if opponent == you:
        return 3 + selection_score
    match opponent+"_"+you:
        case "rock_paper" | "paper_scissor" | "scissor_rock":
            return 6 + selection_score
        case "paper_rock" | "scissor_paper" | "rock_scissor":
            return 0 + selection_score


def main(l):
    print(sum(run_game(x, y) for x, y in l))


if __name__ == "__main__":
    s = """A Y
B X
C Z"""
    # l = [(map_game(x.split(" ")[0]), map_game(x.split(" ")[1]))
    #      for x in s.split("\n")]
    l = [(map_game(x.split(" ")[0]), map_game(x.split(" ")[1]))
         for x in open("day2.input.txt").read().split("\n")]
    main(l)
