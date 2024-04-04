class SpecialStack:
    def __init__(self,data):
        self.data=data
        self.minele=None
    def push(self,data):
        new_node=Node(data)
        if self.top==None:
            self.top==new_node
            self.minele=data
        else:
            if data<self.minele:
                new_node.data=2*data-self.minele
                self.minele=data
            new_node.next==self.top
            self.top=new_node
        print(f"Pushed:{data}, Peek:{self.top.data},Min:{self.minele}")
    def pop(self):
        if self.top is None:
            raise IndexError(" pop from an empty stack")
        temp=self.top.data
        self.top==self.top.next
        if temp< self.minele:
            min_removed==self.minele
            self.minele=2*self.minele-temp
            print(f"popped: {temp},Peek{self.top.data if self.top else None}, Min:{self.minele}")
            return min_removed
        else:
            print(f"popped: {temp},Peek{self.top.data if self.top else None}, Min:{self.minele}")
            return temp
    def isEmpty(self):
        return self.top is None
    def getMin(self):
        if self.top is None:
            raise Indexerror(" getmin from an empty stack")
        return self.minele
special_stack=SpecialStack()
data=[3,5,2,1,1,-1]
for item in data:
    special_stack.push(item)
while not special_stack.isEmpty():
    special_stack.pop()

        
            
            
