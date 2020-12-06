from collections import Counter
def main(l):
    answers_count = 0
    for i in l:
        answers_list = [list(x) for x in i]
        answers = [y for x in answers_list for y in x]
        answers_all = len(set([a for a,num in Counter(answers).most_common() if num == len(answers_list)]))
        answers_count+=answers_all
    print(answers_count)

        

if __name__ == "__main__":
    l = [x.split("\n") for x in open("day6.input.txt").read().split("\n\n")]
    main(l)