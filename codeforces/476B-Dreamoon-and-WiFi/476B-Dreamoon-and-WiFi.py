import sys
sys.setrecursionlimit(10**7)


def solve():
    drazin_s = input()
    dreamon_s = input()
    destination = 0
    for cmd in drazin_s:
        if cmd == '-':
            destination -= 1
        else:
            destination += 1
    current_postion = 0
    unknown_cmd = 0
    for cmd in dreamon_s:
        if cmd == '-':
            current_postion -= 1
        elif cmd == '+':
            current_postion += 1
        else:
            unknown_cmd += 1
    total_comb = 2 ** unknown_cmd
    goal = destination - current_postion
    good_comb = 0

    per = []

    def backTrack(path):
        nonlocal good_comb
        if len(path) == unknown_cmd:

            if sum(path) == goal:
                good_comb += 1
            # print('good',good_comb)
            per.append(path[:])
            return
        backTrack(path + [1])
        backTrack(path + [-1])
    backTrack([])

    return f"{good_comb/total_comb:.12f}"


print(solve())