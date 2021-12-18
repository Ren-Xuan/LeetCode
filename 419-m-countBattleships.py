from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ans = 0
        for i, v in enumerate(board) :
            for j, w in enumerate(v) :
                if ((i == 0 or board[i-1][j] != 'X') and (j == 0 or board[i][j-1] != 'X')) and w == 'X':
                    ans += 1
        return ans