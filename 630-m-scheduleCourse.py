class Solution:
    def scheduleCourseOvertime(self, courses) -> int:
        courses=sorted(courses,key=lambda x:x[1])
        print(courses)
        def study(courses,start):
            if len(courses) == 0:
                return 0
            if courses[0][1]>=courses[0][0]+start:
                return max(study(courses[1:],start),1+study(courses[1:],start+courses[0][0]))
            else:
                return study(courses[1:],start)
        return study(courses,0)
    def scheduleCourse(self, courses) -> int:  # 大根堆
    #（1）按照结束时间对课程进行排序
    #（2）使用一个大顶堆来储存已经选择的课程的长度
    #（3）一旦发现安排了当前课程之后，其结束时间超过了最晚结束时间，那么就从已经安排的课程中，取消掉一门最耗时的课程

        import heapq
        courses = sorted(courses, key = lambda x: x[1])
        d = 0
        heap = []
        for course in courses:
            d += course[0]
            heapq.heappush(heap, -course[0])
            if d > course[1]:
                d += heapq.heappop(heap)
        return len(heap)
        