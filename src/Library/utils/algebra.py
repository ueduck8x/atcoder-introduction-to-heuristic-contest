from functools import reduce
from operator import mul
from typing import List, Tuple


# 最大公約数を求める
def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


# 複数の数から最大公約数を求める
def gcds(num_list: list) -> int:
    return reduce(gcd, num_list)


# 最小公倍数を求める
def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


# 複数の数から最小公倍数を求める
def lcms(num_list: list):
    # オプションの initializer が存在する場合，計算の際に iterable の先頭に置かれる．
    return reduce(lcm, num_list, 1)


# 約数を列挙する
def divisor(n: int) -> List[int]:
    table = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            table.append(i)
            table.append(n // i)
        i += 1
    table = list(set(table))
    return table


# 数字 n を素因数分解する
def prime_decomposition(n: int) -> List[int]:
    i = 2
    table = []
    while i * i <= n:
        while n % i == 0:
            n = int(n / i)
            table.append(i)
        i += 1
    if n > 1:
        table.append(n)
    return table


# 素数判定
def is_prime(n: int) -> bool:
    if n == 1:
        return False
    for i in range(2, n + 1):
        if i * i > n:
            break
        if n % i == 0:
            return False
    return True


# 組み合わせ数 nCr を求める
def comb(n: int, r: int) -> int:
    r = min(n - r, r)
    if r == 0:
        return 1
    # ex)
    # reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])は，
    # ((((1 + 2) + 3) + 4) + 5)を計算する．
    over = reduce(mul, range(n, n - r, -1))
    under = reduce(mul, range(1, r + 1))
    return over // under


# 組み合わせ数のあまり nCr mod p を求める(p = 10 ** 9 + 7)
def preprocess_for_cmb_mod() -> Tuple[List[int], List[int]]:
    # 参考: https://blog.satoooh.com/entry/5195/
    p = 10**9 + 7
    N = 10**6
    # それぞれの要素をあらかじめ前計算
    # nCk = n!/k!(n - k)! = n! * (k!)^(-1) * (n - k)!^(-1)
    # n!: fac[n]
    # (k!)^(^1): finv[k]
    # (n - k)!^(-1): finv[n - k]
    fac = [1, 1]
    fac_inv = [1, 1]
    inv = [0, 1]
    for i in range(2, N + 1):
        fac.append((fac[-1] * i) % p)
        # invは，a^(-1) mod pの計算
        inv.append((-inv[p % i] * (p // i)) % p)
        # fac_invは，a^(-1)! mod pの計算
        fac_inv.append((fac_inv[-1] * inv[-1]) % p)
    return fac, fac_inv


# 組み合わせ数のあまり nCr mod p を求める(p = 10 ** 9 + 7)
def cmb(n: int, r: int, fac: List[int], fac_inv: List[int]) -> int:
    p = 10**9 + 7
    if r < 0 or r > n:
        return 0
    r = min(r, n - r)
    v = fac[n] * fac_inv[r] * fac_inv[n - r] % p
    return v
