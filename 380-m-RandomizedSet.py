class RandomizedSet:

    def __init__(self):
        self.nums  = {}
        self.stack = []

    def insert(self, val: int) -> bool:
        if val not in self.nums:
            self.stack.append(val)
            self.nums[val] = len(self.stack) - 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.nums:
            last   = len(self.stack) - 1
            change = self.nums[val]
            if last == change:  #最后一位，直接pop就可以
                del self.nums[val]
                self.stack.pop()
            else:   #首先交换stack中的两个数，然后stack.pop，删除字典中的键，更新交换的字符在字典中的值
                self.stack[last], self.stack[change] = self.stack[change], self.stack[last]
                del self.nums[val]
                self.stack.pop()
                self.nums[self.stack[change]] = change
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.stack)