
class VanEmdeBoasTree:
    def __init__(self, universe_size):
        self.u = universe_size
        self.min = None
        self.max = None
        self.clusters = dict()  
        self.summary = None

    def high(self, x):
        return x // int(self.u ** 0.5)

    def low(self, x):
        return x % int(self.u ** 0.5)

    def index(self, high, low):
        return high * int(self.u ** 0.5) + low

    def insert(self, x):
        if self.min is None:
            self.min = self.max = x
            return
        if x < self.min:
            x, self.min = self.min, x
        if self.u > 2:
            h = self.high(x)
            l = self.low(x)
            if h not in self.clusters:
                self.clusters[h] = VanEmdeBoasTree(int(self.u ** 0.5))
            if self.clusters[h].min is None:
                if self.summary is None:
                    self.summary = VanEmdeBoasTree(int(self.u ** 0.5))
                self.summary.insert(h)
            self.clusters[h].insert(l)
        if x > self.max:
            self.max = x

    def successor(self, x):
        if self.u == 2:
            if x == 0 and self.max == 1:
                return 1
            else:
                return None
        if self.min is not None and x < self.min:
            return self.min
        h = self.high(x)
        l = self.low(x)
        if h in self.clusters and self.clusters[h].max is not None and l < self.clusters[h].max:
            offset = self.clusters[h].successor(l)
            return self.index(h, offset)
        elif self.summary is not None:
            succ_cluster = self.summary.successor(h)
            if succ_cluster is None:
                return None
            else:
                offset = self.clusters[succ_cluster].min
                return self.index(succ_cluster, offset)
        return None

    def predecessor(self, x):
        if self.u == 2:
            if x == 1 and self.min == 0:
                return 0
            else:
                return None
        if self.max is not None and x > self.max:
            return self.max
        h = self.high(x)
        l = self.low(x)
        if h in self.clusters and self.clusters[h].min is not None and l > self.clusters[h].min:
            offset = self.clusters[h].predecessor(l)
            return self.index(h, offset)
        elif self.summary is not None:
            pred_cluster = self.summary.predecessor(h)
            if pred_cluster is None:
                if self.min is not None and x > self.min:
                    return self.min
                return None
            else:
                offset = self.clusters[pred_cluster].max
                return self.index(pred_cluster, offset)
        return None

    def delete(self, x):
        if self.min == self.max:
            self.min = self.max = None
            return
        if self.u == 2:
            if x == 0:
                self.min = 1
            else:
                self.min = 0
            self.max = self.min
            return
        if x == self.min:
            first_cluster = self.summary.min if self.summary else None
            if first_cluster is None:
                self.min = self.max
                return
            x = self.index(first_cluster, self.clusters[first_cluster].min)
            self.min = x
        h = self.high(x)
        l = self.low(x)
        if h in self.clusters:
            self.clusters[h].delete(l)
            if self.clusters[h].min is None:
                self.summary.delete(h)
                del self.clusters[h]
                if self.summary.min is None:
                    self.summary = None
        if x == self.max:
            if self.summary is None:
                self.max = self.min
            else:
                max_cluster = self.summary.max
                self.max = self.index(max_cluster, self.clusters[max_cluster].max)

    def print_structure(self):
        output = f"Min: {self.min}, Max: {self.max}"
        for c in sorted(self.clusters.keys()):
            output += f", C[{c}]: {self.clusters[c].min},..."
        return output
