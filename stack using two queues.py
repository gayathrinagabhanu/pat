from queue import Queue
class Stackusingqueues:
    def __init__(self):
        self.queue1=Queue()
        self.queue2=Queue()
    def push(self,x):
        self.queue2.put(x)
        while not self.queue1.empty():
            self.queue.put(self.queue1.get())
            self.queue1,self.queue2= self.queue2,self.queue1
    def pop(self):
        if self.queue1.empty():
            raise IndexError (" pop from an empty stack")
            return self.queue1.get()
    def top(self):
        if self.queue1.empty():
            raise IndexError (" top on an empty stack")
            return self.queue1.queue[0]
    def isEmpty(self):
        return self.queue1.empty() 
            
stack=Stackusingqueues()
stack.push(1)
stack.push(2)
stack.push(3)
print("top element:", stack.top())
print("popped element:", stack.pop())
print("is stack empty?", stack.isEmpty())

