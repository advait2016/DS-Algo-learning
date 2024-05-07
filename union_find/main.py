"""
3 Primary Operations

make_set(v) - create a new set with a single element v
union_sets(a,b) - merges the two specified sets (the set in which the element a is located and the element b is located)
find_set(v) - returns the representative (also called the leader) of the set that contains the element v.
"""


class UnionFind:

    def __init__(self, count: int = 10):
        self.parent = [i for i in range(count)]
        self.sz = [1] * count

    def find(self, x: int) -> int:
        root = x

        while root != self.parent[root]:
            root = self.parent[root]

        while x != root:
            nxt = self.parent[x]
            self.parent[x] = root
            x = nxt

        return root

    def connected(self, x: int, y: int):
        return self.find(x) == self.find(y)

    def componentSize(self, x: int):
        return self.sz[self.find(x)]

    def size(self):
        return len(self.parent)

    def unify(self, x: int, y: int):

        if self.connected(x, y):
            return

        root1 = self.find(x)
        root2 = self.find(y)

        if (self.sz[root1] < self.sz[root2]):
            self.sz[root2] += self.sz[root1]
            self.parent[root1] = root2
            self.sz[root1] = 0
        else:
            self.sz[root1] += self.sz[root2]
            self.parent[root2] = root1
            self.sz[root2] = 0


def main():
    uf = UnionFind()
    uf.unify(1, 2)
    uf.unify(3, 4)
    print(uf.parent)


if __name__ == '__main__':
    main()
