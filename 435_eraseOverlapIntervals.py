from operator import itemgetter
class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals = sorted(intervals, key=lambda x: x[1])
        print(intervals)
        res = 1
        end = intervals[0][1]
        for int1 in intervals[1:]:
            if int1[0] >= end:
                res += 1
                end = int1[1]

        res = len(intervals) - res
        return res    
    # def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
    #     intervals_overlap = {}
    #     intervals_contains = {}
    #     intervals.sort()
    #     print(intervals)
    #     for n0 in range(len(intervals)-1):
    #         n1 = n0 + 1
    #         while n1 < len(intervals) and intervals[n1][0] < intervals[n0][1]:
    #             if intervals[n1][1] > intervals[n0][1] and intervals[n1][0] != intervals[n0][0]:
    #                 if n0 not in intervals_overlap:
    #                     intervals_overlap[n0] = set()
    #                 intervals_overlap[n0].add(n1)     
    #                 if n1 not in intervals_overlap:
    #                     intervals_overlap[n1] = set()
    #                 intervals_overlap[n1].add(n0)
    #             if  intervals[n1][1] > intervals[n0][1] and intervals[n1][0] == intervals[n0][0]:
    #                 if n1 not in intervals_contains:
    #                     intervals_contains[n1] = set()
    #                 intervals_contains[n1].add(n0)
    #             if intervals[n1][1] <= intervals[n0][1]:
    #                 if n0 not in intervals_contains:
    #                     intervals_contains[n0] = set()
    #                 intervals_contains[n0].add(n1)                    
    #             n1 += 1
    #     print("CONTAINS")   
    #     print(intervals_contains)

    #     print("OVERLAP")   
    #     print(intervals_overlap)

    #     int_to_delete = []
    #     for int0 in intervals_contains:
    #         if int0 in intervals_overlap:
    #             for int1 in intervals_overlap[int0]:
    #                 intervals_overlap[int1].remove(int0)
    #                 if len(intervals_overlap[int1]) == 0:
    #                     intervals_overlap.pop(int1)
    #             intervals_overlap.pop(int0)
    #         int_to_delete.append(int0)
        
    #     for int0 in int_to_delete:
    #         intervals_contains.pop(int0)
    #     res = len(int_to_delete)
    #     print("RES")   
    #     print(res)
    #     print(int_to_delete)
    #     print("CONTAINS")   
    #     print(intervals_contains)

    #     print("OVERLAP")   
    #     print(intervals_overlap)

    #     while intervals_overlap != {}:
    #         max_len = 0
    #         max_int = None
    #         for int0 in intervals_overlap:
    #             if len(intervals_overlap[int0]) > max_len:
    #                 max_len = len(intervals_overlap[int0])
    #                 max_int = int0
    #         print(max_int)
    #         for int1 in intervals_overlap[max_int]:
    #             intervals_overlap[int1].remove(max_int)
    #             if len(intervals_overlap[int1]) == 0:
    #                 intervals_overlap.pop(int1)
    #         intervals_overlap.pop(max_int)
    #         print(intervals_overlap)
    #         res += 1
        
    #     return res


solution = Solution()
intervalse = [[1,2],[2,3],[3,4],[1,3]]
solution.eraseOverlapIntervals(intervalse)


