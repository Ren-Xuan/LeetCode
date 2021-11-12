from os import waitpid


class Solution:
    def minimumDistanceLocalOptimum(self, word: str) -> int:
        loc = {
            'A':(0,0),
            'B':(0,1),
            'C':(0,2),
            'D':(0,3),
            'E':(0,4),
            'F':(0,5),

            'G':(1,0),
            'H':(1,1),
            'I':(1,2),
            'J':(1,3),
            'K':(1,4),
            'L':(1,5),

            'M':(2,0),
            'N':(2,1),
            'O':(2,2),
            'P':(2,3),
            'Q':(2,4),
            'R':(2,5),

            'S':(3,0),
            'T':(3,1),
            'U':(3,2),
            'V':(3,3),
            'W':(3,4),
            'X':(3,5),

            'Y':(4,0),
            'Z':(4,1)
        }
        def distance(charA,charB):
            a = loc[charA]
            b = loc[charB]
            return abs(a[0] - b[0])+abs(a[1] -b[1])
        m = -1
        finger = [word[0],None]
        for i in range(1,len(word)):
            finger[0] = word[0]
            finger[1] = word[i]
            step = 0
            #print("-"*20)
            for j in range(1,len(word)):
                print(finger,word[j],step,m)
                if m!=-1 and step>m:
                    break
                if j < i :
                    step+=distance(finger[0],word[j])
                    finger[0] = word[j]
                    continue
                elif finger[1] == word[j]:
                    continue
                one = distance(finger[0],word[j])
                two = distance(finger[1],word[j])
                if one > two:
                    step+=two
                    finger[1] = word[j]
                else:
                    step+=one
                    finger[0] = word[j]
            if step<m or m == -1:
                m = step
        return m
    def minimumDistance(self, word: str) -> int:
        loc = {
            'A':(0,0),
            'B':(0,1),
            'C':(0,2),
            'D':(0,3),
            'E':(0,4),
            'F':(0,5),

            'G':(1,0),
            'H':(1,1),
            'I':(1,2),
            'J':(1,3),
            'K':(1,4),
            'L':(1,5),

            'M':(2,0),
            'N':(2,1),
            'O':(2,2),
            'P':(2,3),
            'Q':(2,4),
            'R':(2,5),

            'S':(3,0),
            'T':(3,1),
            'U':(3,2),
            'V':(3,3),
            'W':(3,4),
            'X':(3,5),

            'Y':(4,0),
            'Z':(4,1)
        }
        def distance(charA,charB):
            a = loc[charA]
            b = loc[charB]
            return abs(a[0] - b[0])+abs(a[1] -b[1])

        def stepLenth(twoIndex,word,curMin):
            step = 0
            for i in range(0,twoIndex):
                step+=distance(word[0],word[i])
            #m = -1
            if step > curMin and curMin!=-999:
                return -1
            oneIndex = twoIndex-1
            #twoIndex
            return resultLenth(0,1,word[oneIndex:],curMin - step)+step


        def resultLenth(oneIndex,twoIndex,wordRes,curMin):
            
            """
            oneIndex twoIndex wordRes
            """
            if curMin < 0:
                return 99999999
            if oneIndex == len(wordRes)-1 or twoIndex == len(wordRes)-1:
                return 0
            if oneIndex+1 == twoIndex:
                l=resultLenth(oneIndex+2,twoIndex,wordRes,curMin -distance(wordRes[oneIndex],wordRes[oneIndex+2]))+distance(wordRes[oneIndex],wordRes[oneIndex+2])
                r=resultLenth(oneIndex,twoIndex+1,wordRes,curMin -distance(wordRes[twoIndex],wordRes[twoIndex+1]))+distance(wordRes[twoIndex],wordRes[twoIndex+1])
                if l <curMin or r < curMin:
                    return 999999999
                return min(l,r)
            elif oneIndex - 1 == twoIndex:
                l=resultLenth(oneIndex+1,twoIndex,wordRes,curMin -distance(wordRes[oneIndex],wordRes[oneIndex+1]))+distance(wordRes[oneIndex],wordRes[oneIndex+1])
                r=resultLenth(oneIndex,twoIndex+2,wordRes,curMin -distance(wordRes[twoIndex],wordRes[twoIndex+2]))+distance(wordRes[twoIndex],wordRes[twoIndex+2])
                if l <curMin or r < curMin:
                    return 999999999
                return min(l,r)
            else:
                l=resultLenth(oneIndex+1,twoIndex,wordRes,curMin -distance(wordRes[oneIndex],wordRes[oneIndex+1]))+distance(wordRes[oneIndex],wordRes[oneIndex+1])
                r=resultLenth(oneIndex,twoIndex+1,wordRes,curMin -distance(wordRes[twoIndex],wordRes[twoIndex+1]))+distance(wordRes[twoIndex],wordRes[twoIndex+1])
                if l <curMin or r < curMin:
                    return 999999999
                return min(l,r)
        #for i in range(1,len(word)):
        #    print("i",stepLenth(i,word))
        curMin = -999
        for i in range(1,len(word)):
            res = stepLenth(i,word,curMin)
            if res == -1:
                continue
            if curMin==-999 or res < curMin:
                curMin = res
            
        return curMin
        return min(stepLenth(i,word) for i in range(1,len(word)))
        return resultLenth(0,1,word)
            
s = Solution()
print(s.minimumDistance("AXFX"))#局部最优
print(s.minimumDistance("ABYZ"))#局部最优
print(s.minimumDistance("AXFFAOKFQWOLSSFSCDEIKN"))