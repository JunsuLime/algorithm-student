import sys

def solve():
    data = sys.stdin.readline().split()
    repeat = int(data[0])
    string = data[1]
    for c in string:
        sys.stdout.write(c * repeat)
    sys.stdout.write('\n')

test_case = int(sys.stdin.readline())
for _ in range(test_case):
    solve()

