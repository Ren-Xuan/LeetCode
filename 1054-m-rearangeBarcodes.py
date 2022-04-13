class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        """
        对于题目给的例子[1,1,1,1,2,2,3,3]，分两步完成:
        [1, _, 1, _, 1, _, 1, _] 其中_表示还未填写
        [1, 2, 1, 2, 1, 3, 1, 4]
        """
        counter = dict(collections.Counter(barcodes))
        #按出现次数统计元素
        sortedCounter = sorted( counter, key=lambda k: 0 - counter[k])
        barcodes = []
        #重新排序
        for i in sortedCounter:
            barcodes += [i] * counter[i]
        
        arrangedBarcodes = [None for _ in range(len(barcodes))]
        #间隔插入
        arrangedBarcodes[::2] = barcodes[:len(arrangedBarcodes[::2])]
        arrangedBarcodes[1::2] = barcodes[len(arrangedBarcodes[::2]):]

        return arrangedBarcodes
