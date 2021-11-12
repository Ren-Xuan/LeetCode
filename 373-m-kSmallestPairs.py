class Solution:
    def kSmallestPairs(self, nums1, nums2, k: int) :
        import heapq
        pq = []
        cnt = 0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if cnt<k:
                    heapq.heappush(pq,(-(nums1[i]+nums2[j]),i,j))
                    cnt+=1
                elif cnt >=k and -(nums1[i]+nums2[j])>pq[0][0]:
                    heapq.heappop(pq)
                    heapq.heappush(pq,(-(nums1[i]+nums2[j]),i,j))
                else:#剪枝
                    break
        pq.sort(key = lambda x :-x[0])
        result = []
        for e in pq:
            result.append([nums1[e[1]]]+[nums2[e[2]]])
        return result