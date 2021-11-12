class Solution:
    def storeWater(self, bucket, vat) -> int:
        import math
        if max(vat) == 0:
            return 0
        n = len(bucket)

        res = float('inf')

        min_pour_op = 1     #已经知道不可能是0次了
        max_pour_op = max(vat) #最多的情况（直接一次又一次地倒）这只是倾倒次数，升容次数再算。

        for pour_time in range(min_pour_op, max_pour_op + 1):
            cur = pour_time     #总操作 = 倾倒 + 桶升容
            for i in range(n):
                ###### 桶的大小至少是多大
                need_bucket_size = math.ceil(vat[i] / pour_time)
                ###### 桶升容的次数
                need_bucket_op = max(0, need_bucket_size - bucket[i])
                ###### cur += 桶升容次数
                cur += need_bucket_op
            
            res = min(res, cur)
        
        return res
    def storeWater2(self, bucket, vat) -> int:
        import heapq
        import math
        heap, cnt, res, opt = [], 0, max(vat), 0
        if res==0: return 0
        for i,j in zip(bucket,vat):
            if j==0: continue
            if i==0: i, cnt = 1, cnt + 1
            heapq.heappush(heap, [-math.ceil(j/i),i,j])
        
        while opt < res:
            res = min(res, opt-heap[0][0])
            k,i,j = heap[0]
            if k>=-2: break
            new = [-math.ceil(j/(i+1)),i+1,j]
            heapq.heapreplace(heap, new)
            opt += 1
        return res + cnt
