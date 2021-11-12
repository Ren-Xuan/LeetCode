class Solution:
    def arrangeWords(self, text: str) -> str:
        arr = text.split(" ")
        arr[0] = arr[0].lower()
        arr.sort(key=lambda x: len(x))
        arr[0] = arr[0].capitalize()
        s = arr[0]
        for i in arr[1:]:
            s+=" "+i
        return s


s = Solution()
print(s.arrangeWords("Keep calm and code on"))