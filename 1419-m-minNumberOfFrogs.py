class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        """
        青蛙一段连续的音频是“croak”这5个字母，这些字母可以不连续，但是各个字母出现的前后顺序不能乱，而且必须凑够这5个字母。
        给出一段由“croak”这5个字母组成的字符串croakOfFrogs，问的是至少需要多少只青蛙才能发出该字符串的叫声。
        “croakcroak”可以是一只青蛙，也可以是两只，但是至少需要1只，因此答案是2，“crcoakroak”至少需要两只，
        因为第一个叫声k结束之前就出现了第二个叫声的c，这两只的叫声有重叠。

        从左到右遍历字符串，我们准备一个数组count，用来统计各个字符的出现次数，
        准备一个变量frogs，记录当各个字符位置重叠的青蛙叫声数，题目要求的，就是最多有多少层重叠的叫声。

        叫声“croak”的首尾字符分别是“c”和“k”，每当遇到字符“c”，将frogs加一，代表新的青蛙加入，
        每当遇到字符“k”，说明一只青蛙的叫声停止，frogs减一。
        每次遇到新的字符，需要及时将最新结果记录到ans变量中。
        此外，还需要更新计数器count中对应位置处的数值，并及时研究当前叫声是否合法，
        判断的依据是，我们要求所有字符串的出现次数从左到右必须是单调递减的（也可以相等），
        一旦遇到后面的字符出现次数大于前面的情况，则这种叫声一定无法满足的，例如“croaakcrok”是不存在的
        """
        s = "croak"
        count = [0] * len(s)
        frogs = 0
        ans = 0
        for c in croakOfFrogs:
            if c == s[0]:               # One frog start.
                frogs += 1
                ans = max(ans, frogs)
            elif c == s[-1]:            # One frog finish.
                frogs -= 1
            count[s.index(c)] += 1

            if any(c1 < c2 for c1, c2 in zip(count, count[1:])):
                return -1
        return ans if frogs == 0 else -1
