class UnionFind:
    def __init__(self, n: int) -> None:
        self.n = n
        # root[x] < 0 ならそのノードが根であり，かつその値が木の要素数となる
        self.root = [-1] * (n + 1)
        # 木をくっつける時にアンバランスにならないように調整する
        self.rank = [0] * (n + 1)

    # ノードxのrootノードを見つける
    def findRoot(self, x: int) -> int:
        if self.root[x] < 0:
            return x
        else:
            # ここで代入しておくことで、後の繰り返しを避ける
            self.root[x] = self.findRoot(self.root[x])
            return self.root[x]

    # 木の併合、入力は併合したい各ノード
    def unite(self, x: int, y: int) -> None:
        # 入力ノードのrootノードを見つける
        x = self.findRoot(x)
        y = self.findRoot(y)
        # すでに同じ木に属していた場合
        if x == y:
            return
        # 違う木に属していた場合rankを見てくっつける方を決める
        if self.rank[x] > self.rank[y]:
            self.root[x] += self.root[y]
            self.root[y] = x
        else:
            self.root[y] += self.root[x]
            self.root[x] = y
            # rankが同じ(深さに差がない場合)は1増やす
            if self.rank[x] == self.rank[y]:
                self.rank[y] += 1

    #  xとyが同じグループに属するか判断
    def isSameGroup(self, x: int, y: int) -> bool:
        return self.findRoot(x) == self.findRoot(y)

    # ノードxが属する木のサイズを返す
    def count(self, x: int) -> int:
        return -1 * self.root[self.findRoot(x)]
