class Solution:
    # 构造一个字典，记录所有相同攻击力的单位
    # 之前用栈做的，可是发现：攻击力一样的防御力不太好比……没多想直接hash做
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        map_ = collections.defaultdict(list)
        # 防御力为0，需要记录一个防御力最大的单位
        # 逻辑很简单：只要你的防御力不是最强，而攻击力已经排序了，你又肯定比他们低
        max_defence = - 2 ** 31
        for attack, defence in properties:
            map_[attack].append(defence)
        count = 0
        for attack in sorted(map_, reverse=True):
            for defence in map_[attack]:
                if defence < max_defence:
                    count += 1
            # 刷新防御
            max_defence = max(max_defence, max(map_[attack]))
        return count