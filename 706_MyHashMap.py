class MyHashMap:

    def __init__(self):
        self.my_hash_map = []
        

    def put(self, key: int, value: int) -> None:
        for current_key in self.my_hash_map:
            if key ==  current_key[0]:
                current_key[1] = value
                break
        else:
            self.my_hash_map.append([key, value])

    def get(self, key: int) -> int:
        for current_key in self.my_hash_map:
            if key ==  current_key[0]:
                return current_key[1]
        else:
            return -1
        

    def remove(self, key: int) -> None:
        res = []
        for current_key in self.my_hash_map:
            if key !=  current_key[0]:
                res.append(current_key)
        self.my_hash_map = res


comm_dict = {
    "put":MyHashMap.put,
    "get":MyHashMap.get,
    "remove":MyHashMap.remove}
commands = ["MyHashMap","put","put","get","get","put","get","remove","get"]
params = [[],[1,1],[2,2],[1],[3],[2,1],[2],[2],[2]]


my_hash_map = MyHashMap()
for com, par in zip(commands[1:], params[1:]):
    res = comm_dict[com](my_hash_map, *par)
    print(res)

print(my_hash_map.my_hash_map)
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)