from ast import parse


class MyLinkedList:
    def __init__(self):
        self.MyLinkedList = []        

    def get(self, index: int) -> int:
        if index < 0 or index >= len(self.MyLinkedList):
            return -1
        return self.MyLinkedList[index]

    def addAtHead(self, val: int) -> None:
        new_list = [val]
        new_list.extend(self.MyLinkedList)
        self.MyLinkedList = new_list

    def addAtTail(self, val: int) -> None:
        self.MyLinkedList.append(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > len(self.MyLinkedList):
            return
        new_list = self.MyLinkedList[:index]
        new_list.append(val)
        new_list.extend(self.MyLinkedList[index:])
        self.MyLinkedList = new_list
        
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= len(self.MyLinkedList):
            return
        new_list = self.MyLinkedList[:index]
        new_list.extend(self.MyLinkedList[index + 1:])
        self.MyLinkedList = new_list

COMMANDS = {
    "addAtHead": MyLinkedList.addAtHead,
    "addAtTail": MyLinkedList.addAtTail,
    "addAtIndex": MyLinkedList.addAtIndex,
    "get": MyLinkedList.get,
    "deleteAtIndex": MyLinkedList.deleteAtIndex,
}

commands = ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
params = [[], [1], [3], [1, 2], [1], [1], [1]]

myLst = MyLinkedList()
for comm, par in zip(commands[1:], params[1:]):
    if comm == "MyLinkedList":
        myLst = MyLinkedList()
        continue
    res = COMMANDS[comm](myLst, *par)
    if comm == "get":
        print(res)
        continue

print(myLst.MyLinkedList)