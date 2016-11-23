class Group:
    def __init__(self, rel, elems, identity='e'):
        self.rel = rel
        self.elems = elems
        self.id = identity

    def inv(self, g):
        for h in self.elems:
            if self.rel[g, h] == self.id:
                return h

    def map(self, morph):
        return {x for x in map(morph, self.elems)}

    def lcoset(self, x, sub):
        return sub.map(lambda g: self.rel[x, g])

    def rcoset(self, x, sub):
        return sub.map(lambda g: self.rel[g, x])

    def automorph(self, g):
        return self.map(lambda h: self.rel[g, self.rel[h, self.inv(g)]])

    def rewrite(self, g, h):
        return self.rel[g, self.rel[h, self.inv(g)]]

    def __iter__(self):
# I think I should've just made this inherit from set and dict
        return iter(self.elems)

def cyclic(order):
    rel = {(a, b): (a + b) % order for a in range(0, order)
            for b in range(0, order)}
    return Group(rel, set(range(0, order)), identity=0)

def load(path):
    f = open(path, 'r')
    rel = dict()
    top = f.readline().split()[1:]
    lines = f.readlines()
    for line in lines:
        line = line.split()
        row = line[0]
        for i in range(len(line[1:])):
            rel[row, top[i]] = line[1:][i]
    f.close()
    return Group(rel, set(top))

def product(G, H):
    elems = {(g, h) for g in G for h in H}
    rel = {(a, b): (G.rel[a[0], b[0]], H.rel[a[1], b[1]]) for a in elems for b in elems}
    return Group(rel, elems, identity=(G.id, H.id))

klein = product(cyclic(2), cyclic(2))
