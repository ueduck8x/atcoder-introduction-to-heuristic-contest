# usr/bin/env python3

# collections: [deque: queue, stuck], [Counter: リスト中の同じ要素数え上げ]
# functools: [reduce: 主にnCr]
# heapq: 優先度付きキュー(最小値の取り出しO(1)で可能)
# itertools: [product: bit全探索], [permutation: 順列全探索]
# math: [factorial: n!], [sqrt: root]
# operator: [mul: 主にnCr]
# sys: [stdin: 標準入力], [maxsize: 無限大]
# typing: Libraryからのcopy & pasteするときに使用
from collections import deque, Counter
from functools import reduce
from heapq import heapify, heappop, heappush
from itertools import permutations, product
from math import ceil, factorial, floor, sqrt
from operator import mul
from sys import maxsize, stdin
from typing import Dict, List, Tuple


def main():
    # input
    # N = int(input())
    N, M = map(int, stdin.readline().rstrip().split())
    A = [int(x) for x in stdin.readline().rstrip().split()]
    # A = [list(map(int, stdin.readline().rstrip().split())) for _ in range(N)]
    # for i in range(N):
    #     a, b = map(int, stdin.readline().rstrip().split())

    # procedure


if __name__ == "__main__":
    main()
