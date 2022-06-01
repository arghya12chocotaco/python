class node:
    def __init__ (self,data):
        self.data=data
        self.next= None
class queue:
    def __init__(self):
        self.front=self.rear=None
    def isEmpty(self):
        return(self.front==None)
    def Enqueue(self,data):
        temp=node(data)
        if(self.rear==None):
            self.front=self.rear=temp
            return
        self.rear.next=temp
        self.rear=temp
    def Dequeue(self):
        if(self.isEmpty()):
            return
        temp=self.front
        self.front=temp.next
        if(self.front==None):
            self.rear=None
if __name__=='__main__':
    q=queue()
    q.Enqueue(20)
    q.Enqueue(30)
    q.Enqueue(40)
    q.Enqueue(90)
    q.Enqueue(60)
    q.Dequeue()
    print("queue front"+ str(q.front.data))
    print("queue rear"+str(q.rear.data))
