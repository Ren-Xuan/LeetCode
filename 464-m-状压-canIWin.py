from functools import cache


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        """
        class Solution {
            public boolean canIWin(int maxChoosableInteger, int desiredTotal) {
                // 尝试暴力的记忆化深搜(看题解)
                if ((maxChoosableInteger * (1 + maxChoosableInteger) >> 1) < desiredTotal) {
                    return false;
                }
                // 判断当前层, 也就是当前先手玩家能否获胜, dfs过程中, 两个玩家都全力保证自己每一层的选择能获胜
                return dfs(maxChoosableInteger, desiredTotal, 0, 0, new HashMap<>(16));
            }

            /**
            * 记忆化深搜
            * @param maxChoosableInteger  最大可选值1-maxChoosableInteger
            * @param desiredTotal         最大值
            * @param usedState            当前使用数字的状态, 因为数字1-20
            * @param curTotal             当前total
            * @param memory               记忆化数组
            * @return                     返回是否胜利
            */
            private boolean dfs(int maxChoosableInteger, int desiredTotal, int usedState, int curTotal, Map<Integer, Boolean> memory) {
                // 每一层的玩家不同, 但是目的都是当前层能获胜 || 下一层不能获胜则当前层能获胜
                Boolean result = memory.get(usedState);
                if (result != null) {
                    return result;
                }
                result = false;
                for (int i = 0; i < maxChoosableInteger; i++) {
                    // 暴力
                    if (((usedState >> i) & 1) == 0) {
                        if (i + 1 + curTotal >= desiredTotal) {
                            // 如果当前的玩家能获胜
                            result = true;
                            break;
                        } else if (!dfs(maxChoosableInteger, desiredTotal, usedState | (1 << i), i + 1 + curTotal, memory)) {
                            // 如果它下一个玩家不能获胜, 那么当前玩家能获胜
                            result = true;
                            break;
                        }
                    }
                }
                memory.put(usedState, result);
                return result;
            }
        }
        """
        @cache
        def dfs(usedNumbers: int, currentTotal: int) -> bool:
            for i in range(maxChoosableInteger):
                if (usedNumbers >> i) & 1 == 0:
                    if currentTotal + i + 1 >= desiredTotal or not dfs(usedNumbers | (1 << i), currentTotal + i + 1):
                        return True
            return False

        return (1 + maxChoosableInteger) * maxChoosableInteger // 2 >= desiredTotal and dfs(0, 0)
