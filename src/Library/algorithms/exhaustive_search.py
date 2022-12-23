from itertools import permutations, product
from math import sqrt, factorial
from sys import stdin


# bit全探索(itertoolsを用いる)
def bit_search() -> None:
    N = 5
    for comb_fruits in product(range(2), repeat=N):
        for i in range(N):
            if comb_fruits[i] == 1:
                # 何らかの処理
                pass


# 順列全探索
def permutational_search() -> None:
    N = 5
    for comb in permutations(range(N)):
        # 何らかの処理
        print(comb)


# [sample] ABC128 C - Switches
def abc128c():
    # input
    N, M = map(int, stdin.readline().rstrip().split())
    switches = {}
    for x in range(M):
        _s = [int(i) - 1 for i in stdin.readline().rstrip().split()]
        _s.pop(0)
        switches.update({x: set(_s)})
    p = {x: int(i) for x, i in enumerate(stdin.readline().rstrip().split())}

    # calculation
    ans = 0
    for comb_switch in product(range(2), repeat=N):
        num_lights = 0
        cnt = {x: 0 for x in range(M)}
        for s in range(N):
            if comb_switch[s] != 1:
                continue
            for x in range(M):
                if s in switches[x]:
                    cnt[x] += 1
        for m in range(M):
            if cnt[m] % 2 == p[m]:
                num_lights += 1
        if num_lights == M:
            ans += 1

    # output
    print(ans)


# [sample] ABC147 C - HonestOrUnkind2
def abc147c():
    # input
    N = int(input())
    evidences: dict[int, dict[int, str]] = {}
    for i in range(N):
        A = int(input())
        evdi = {}
        for _ in range(A):
            x, y = map(int, stdin.readline().rstrip().split())
            evdi[x - 1] = y
        evidences[i] = evdi

    # calculation
    ans = 0
    for comb_honest in product(range(2), repeat=N):
        flag = False
        for i in range(N):
            if comb_honest[i] == 0:  # 真偽不明な人は嘘をついているわけではない
                continue
            for k, v in evidences[i].items():
                if comb_honest[k] != v:
                    flag = True
                    break
            if flag:
                break
        if flag is False:
            v = sum(comb_honest)
            ans = v if v > ans else ans

    # output
    print(ans)


# [sample] ABC145 C - Average Length
def abc145c():
    # input
    N = int(input())
    coordinates = {}
    for i in range(N):
        x, y = map(int, stdin.readline().rstrip().split())
        coordinates[i] = {"x": x, "y": y}

    # calculation
    ans = 0
    for path in permutations(range(N)):
        for i in range(N - 1):
            s = path[i]
            t = path[i + 1]
            a = (coordinates[s]["x"] - coordinates[t]["x"]) ** 2
            b = (coordinates[s]["y"] - coordinates[t]["y"]) ** 2
            ans += sqrt(a + b)

    # output
    print(ans / factorial(N))
