from itertools import combinations


def solution(relation):
    row_num = len(relation)
    col_num = len(relation[0])

    possible = [_ for _ in range(col_num)]
    impossible = set()

    key_len = 1
    answer = 0

    while key_len <= col_num:
        cases = combinations(possible, key_len)
        for case in cases:
            skip = False
            for caution in impossible:
                if case.issuperset(set(case)):
                    impossible.add(tuple(sorted(list(case))))
                    skip = True
            if skip:
                continue

            keys = set()
            for row in relation:
                key = ""
                for idx in case:
                    key += row[idx]
                keys.add(key)

            # if it is unique key 
            if len(keys) == row_num:
                impossible.add(tuple(sorted(list(case))))
                answer += 1

        key_len += 1

    return answer

