


class StackNode:
    def __init__(self,data):
        self.data=data
        self.next= None
class stack:
    def __init__(self):
        self.head=None
    def push(self,data):
        NN=StackNode(data)
        if(self.head is None):
            self.head=NN
            print(data)
        else:
            NN.next=self.head
            self.head=NN
            print(data)
    def pop1(self):
        if(self.head is None):
            print("stack is empty")
        else:
            temp=self.head
            self.head=self.head.next
            p=temp.data
            temp.next= None
            print(p,"is poped")
    def peek(self):
        if(self.head is None):
            print("empty")
        else:
            print(self.head.data,"is the peek value")
stack1=stack()
stack1.push(10)
stack1.push(20)
stack1.push(30)
stack1.pop1()
stack1.peek()   

    
