class twoStacks:
    def __init__(self,n):
        self.size=n
        self.arr=[None]*n
        self.top1=-1
        self.top2=self.size
    def push1(self,x):
        if self.top1< self.top2-1:
            self.top1+=1
            self.arr[self.top1]=x
            print("Pushed:",x)
        else:
            print(" stack 1 is overflow")
    def push2(self,x):
         if self.top1< self.top2-1:
            self.top2-=1
            self.arr[self.top2]=x
            print("Pushed:",x)
         else:
            print(" stack2 is overflow")
    def pop1(self):
        if self.top1>=0:
            x=self.arr[self.top1]
            self.top1-=1
            return x
        else:
            print(" stack1 is undeflow")
    def pop2(self):
        if self.top2>=self.size:
            x=self.arr[self.top2]
            self.top2+=1
            return x
        else:
            print(" stack2 is undeflow")
stacks=twoStacks(5)
stacks.push1(1)
stacks.push1(2)
stacks.push2(11)
stacks.push2(12)
stacks.push1(4)
stacks.push2(8)
stacks.push1(6)
print(" Popped from stack1:",stacks.pop1())
print(" Popped from stack2:",stacks.pop2())
print(" Popped from stack1:",stacks.pop1())
print(" Popped from stack2:",stacks.pop2())
print(" Popped from stack1:",stacks.pop1())
print(" Popped from stack2:",stacks.pop2())
print(" Popped from stack1:",stacks.pop1())





    
        
        
        
            

        
        
