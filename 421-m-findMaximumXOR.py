class TreeNode(object):
    def __init__(self,i):
        self.val = i
        self.left = None
        self.right = None
class Solution(object):
    def findMaximumXOR(self, nums):
        """
        主要思路就是把nums里的每个数建树
        一共有31位，如果当前位上是0，就往左子树走
        如果当前位是1，就往右子树走，
        走完了就记录一下这条路径上的这个数是多少。

        然后再线性扫描数组，用贪心的策略向下遍历树
        贪心的地方在于，如果当前位上是0，而有右子树，就往右子树走
        因为这样0和右子树上的1异或可以得到1，反之就往左子树走。

        这种贪心策略的正确性在于，优先保障高位异或得到1。
        而对于二进制的数来说，为了得到更大的异或值，
        最高位的1的重要性比其他位1更高，比如 1000一定大于0111，所以得到的一定会是最大的异或值。
        """
        #贪心+字典Tree
        root = TreeNode(-1)
        
        for num in nums:
            cur_node = root #当前的node
            
            for i in range(0, 32):               #代表32个位
                # print num, 1 <<(31 - i), num & (1 <<(31 - i))
                if num & (1 <<(31 - i)) == 0:    #如果当前位与运算的结果是1， 就往左走
                    if not cur_node.left:
                        cur_node.left = TreeNode(0)
                    cur_node = cur_node.left
                else:                            #如果当前位与运算的结果是0， 就往右走
                    if not cur_node.right:
                        cur_node.right = TreeNode(1)
                    cur_node = cur_node.right
            cur_node.left = TreeNode(num)        #在最后的左叶子节点记录一下这个数的值
                    
        res = 0
        for num in nums:
            cur_node = root
            
            for i in range(0, 32):
                # print cur_node.val, cur_node.left, cur_node.right
                if num & (1 <<(31 - i)) == 0:     #与运算结果为0，如果能往右走，就往右走，因为右子树代表1，这样在这一位上异或会得到1
                    if cur_node.right:           #能往右走
                        cur_node = cur_node.right#就往右走
                    else:                        #不能往右走
                        cur_node = cur_node.left#就往左走
                else:                            #与运算结果为1，如果能往左走，就往左走，因为左子树代表0，这样异或会得到1
                    if cur_node.left:            #能往左走
                        cur_node = cur_node.left#就往左走
                    else:                        #不能往左走
                        cur_node = cur_node.right#就往右走  
            temp = cur_node.left.val             #得到这条路径存放的数的值
                
            res = max(res, num ^ temp)           #每次刷新res为最大值
                
        return res