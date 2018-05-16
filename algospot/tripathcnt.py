import sys


def work():
    height = int(sys.stdin.readline())

    max_vals = list()
    max_cnts = list()

    max_vals.append(int(sys.stdin.readline()))
    max_cnts.append(1)

    for i in range(1, height):
        c_vals = max_vals[:]
        c_cnts = max_cnts[:]

        for idx, e in enumerate(map(int, sys.stdin.readline().rstrip().split())):
            if idx == i:
                max_vals.append(c_vals[idx-1] + e)
                max_cnts.append(c_cnts[idx-1])
            elif idx == 0:
                max_vals[0] = c_vals[0] + e
                max_cnts[0] = c_cnts[0]
            else:
                if c_vals[idx-1] > c_vals[idx]:
                    max_vals[idx] = c_vals[idx-1] + e
                    max_cnts[idx] = c_cnts[idx-1]
                elif c_vals[idx-1] == c_vals[idx]:
                    max_vals[idx] = c_vals[idx] + e
                    max_cnts[idx] = c_cnts[idx] + c_cnts[idx-1]
                else:
                    max_vals[idx] = c_vals[idx] + e
                    max_cnts[idx] = c_cnts[idx]

    max_val = max(max_vals)
    cnt = 0
    for v, c in zip(max_vals, max_cnts):
        if v == max_val:
            cnt += c

    sys.stdout.write('%d\n' % cnt)

test_case = int(sys.stdin.readline())

for _ in range(test_case):
    work()

