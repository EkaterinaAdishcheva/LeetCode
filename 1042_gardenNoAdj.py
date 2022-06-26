def build_connenction_dict(paths):
    connenction_dict = {}
    for p in paths:
        [p[0], p[1]] = [p[0], p[1]] if p[0] < p[1] else [p[1], p[0]] 
        if p[0] not in connenction_dict:
            connenction_dict[p[0]] = set()
        connenction_dict[p[0]].add(p[1])
    return connenction_dict    

def full_connection_list(gardens_current, start, lenth, connenction_dict):
    print(gardens_current, start, lenth, connenction_dict)
    for pos in range(start, lenth):
        candidates = connenction_dict[pos].intersection(gardens_current)
        if candidates == set():
            return gardens_current
        else:
            for g in candidates:
                gardens_current_copy = gardens_current.copy()
                full_connection_list(gardens_current_copy.add(g), pos+1, lenth, full_connection_list)

def build_full_connection_list(connenction_dict):
    full_path = []
    print(list(connenction_dict.keys()).sort())
    for g in list(connenction_dict.keys()).sort():
        full_path.append(full_connection_list([g], g + 1, len(list(connenction_dict.kkeys())), connenction_dict))
    return full_path


n = 3
paths = [[1,2],[2,3],[3,1]]

connenction_dict_task = build_connenction_dict(paths)
print(connenction_dict_task)
full_path = build_full_connection_list(connenction_dict_task)



def gardenNoAdj(self, n: int, paths: list[list[int]]) -> list[int]:
    connenction_dict_task = Solution.build_connenction_dict(paths)
    print(connenction_dict_task)
    # flowers = [-1 for x in range(n)]
    # max_flower = 0
    # for garden0 in connenction_dict_task:
    #     if -1 == flowers[garden0]:
    #          flowers[garden0] = max_flower
    #          max_flower += 1
    #          for garden in list(connenction_dict_task[garden0]):




solution = Solution()

print(solution.gardenNoAdj(n, paths))