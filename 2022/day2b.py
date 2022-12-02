score_map = {
    # rock
    "rock": 1,
    # paper
    "paper": 2,
    # scissor
    "scissor": 3
}


winning_map = {
    "rock": "paper",
    "paper": "scissor",
    "scissor": "rock"
}

losing_map = {value: key for key, value in winning_map.items()}


def map_game(s):
    match s:
        case "B":
            return "paper"
        case "A":
            return "rock"
        case "C":
            return "scissor"


def run_game(opponent, you):
    selected = None
    # draw
    if you == "Y":
        selected = opponent
    if you == "Z":
        selected = winning_map[opponent]
    if you == "X":
        selected = losing_map[opponent]
    selection_score = score_map[selected]

    if selected == opponent:
        return 3 + selection_score

    match opponent+"_"+selected:
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
    # l = [(map_game(x.split(" ")[0]), x.split(" ")[1])
    #      for x in s.split("\n")]
    l = [(map_game(x.split(" ")[0]), x.split(" ")[1])
         for x in open("day2.input.txt").read().split("\n")]
    main(l)
