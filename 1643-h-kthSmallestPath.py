class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        """
        当字符串中每一种字符的数量固定时（例如对于本题，我们需要在字符串中放入 h 个H 和 v个 V），
        如果需要求出字典序第 k 小的字符串，可以考虑从高位高位向低位依次确定每一个位置的字符。

        如果我们在最高位放置了H，那么剩余的(h−1,v) 就是一个规模减少的相同问题；
        同理如果我们在最高位放置了 V，那么剩余的 (h,v−1) 也是一个规模减少的相同问题。

        我们考虑最高位是放H 还是V。由于后者的字典序较大，因此如果最高位放 V，
        那么所有最高位为 H 的字符串的字典序都比它 小，这样的字符串共有
        math.comb(h + v - 1, h - 1)个

        """
        v, h = destination
        ans = list()
        for i in range(h + v):
            if h > 0:
                o = math.comb(h + v - 1, h - 1)
                if k > o:
                    ans.append("V")
                    v -= 1
                    k -= o
                else:
                    ans.append("H")
                    h -= 1
            else:
                ans.append("V")#当h=0 时，我们只能放V，无需进行判断。
                v -= 1
        return "".join(ans)

