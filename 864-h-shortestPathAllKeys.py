class Solution(object):
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        level order by status squeeze
        """
        door_key = {'A':'a', 'B':'b', 'C':'c', 'D':'d', 'E':'e', 'F':'f'}
        key_map = {}
        key_num = 0
        queue = []
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '@':
                    queue.append([0, i, j, 0])
                    visited.add((i, j, 0))
                elif grid[i][j] in door_key.values():
                    key_map[grid[i][j]] = key_num
                    key_num += 1
        final_status = (1 << key_num) - 1

        print(i,j)
        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
        while True:
            if len(queue) == 0:
                return -1
            step, i, j, status = queue.pop(0)
            if status == final_status:
                return step
            for d in directions:
                new_i = i + d[0]
                new_j = j + d[1]
                if new_i < 0 or new_j < 0 or new_i >= len(grid) or new_j >= len(grid[0]):
                    continue
                c = grid[new_i][new_j]
                if c == '#' or (c in door_key and (status & (1<<key_map[door_key[c]])) == 0):
                    continue
                new_status = status
                if c in key_map:
                    new_status = status | (1<<key_map[c])
                if (new_i, new_j, new_status) not in visited:
                    visited.add((new_i, new_j, new_status))
                    queue.append((step+1, new_i, new_j, new_status))