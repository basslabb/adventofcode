def main(l):
    answers_count = 0
    for i in l:
        answers = set([y for x in i for y in list(x)])
        answers_count += len(answers)
    print(answers_count)


if __name__ == "__main__":
    l = [x.split("\n") for x in open("day6.input.txt").read().split("\n\n")]
    main(l)