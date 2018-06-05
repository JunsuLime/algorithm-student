import sys

def work():
    total_score = 0
    score = 0
    for c in sys.stdin.readline().rstrip():
        if c == 'O':
            score += 1
            total_score += score
        elif c == 'X':
            score = 0

    sys.stdout.write('%d\n' % total_score)

test_case = int(sys.stdin.readline())

for _ in range(test_case):
    work()

