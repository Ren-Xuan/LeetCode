from collections import Counter, defaultdict

import heapq
class FreqStack:

    def __init__(self):
        self.stack = []
        self.dict = defaultdict(int)

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.dict[val]+=1

    def pop(self) -> int:
        m = max(self.dict.values())
        i = len(self.stack)-1
        while i>=0:
            k = self.stack[i]
            if self.dict[k] == m:
                self.dict[k]-=1
                return self.stack.pop(i)
            i-=1

class FreqStack2(object):

    def __init__(self):
        self.freq = Counter()
        self.group = defaultdict(list)
        self.maxfreq = 0

    def push(self, x):
        f = self.freq[x] + 1
        self.freq[x] = f
        if f > self.maxfreq:
            self.maxfreq = f
        self.group[f].append(x)

    def pop(self):
        x = self.group[self.maxfreq].pop()
        self.freq[x] -= 1
        if not self.group[self.maxfreq]:
            self.maxfreq -= 1

        return x
