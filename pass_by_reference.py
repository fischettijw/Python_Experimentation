from custom.func import *
import os
os.system('cls')


def create_questions(qs):
    qs = [
        ['Questions#1', 1, ['option 1', 'option 2', 'option 3', 'option 4']],
        ['Questions#2', 2, ['option 1', 'option 2', 'option 3']],
        ['Questions#3', 3, ['option 1', 'option 2', 'option 3', 'option 4']],
        ['Questions#4', 2, ['option 1', 'option 2']],
        ['Questions#5', 4, ['option 1', 'option 2', 'option 3', 'option 4']]
    ]
    return qs


def print_questions(qs):
    for q in qs:
        print_ln(q[0])
        print_ln(q[1])
        for opt in q[2]:
            print_ln(opt)
        print_ln()


def main():
    questions = []
    questions = create_questions(questions)
    print_questions(questions)


if __name__ == '__main__':
    main()
