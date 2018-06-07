import sys

n = int(sys.stdin.readline())

for _ in range(n):
    splitted_string = sys.stdin.readline().rstrip().split()
    sys.stdout.write('god')
    
    for i in range(1, len(splitted_string)):
        sys.stdout.write(splitted_string[i])
    sys.stdout.write('\n')

