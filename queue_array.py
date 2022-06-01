


class queue:
    def __init__(self,c):
         self.queue=[]
         self.front=self.rear=0
         self.capacity=c
    def Enqueue(self,data):
        if(self.capacity==self.rear):
            print("queue is full")
        else:
            self.queue.append(data)
            self.rear += 1
    def Dequeue(self):
        if(self.front==self.rear):
            print("queue is empty")
        else:
            x=self.queue.pop()
            self.rear -=1
    def queueDisplay(self):
        if (self.front==self.rear):
            print("queue is empty")
        for i in self.queue:
            print(i)
if __name__=='__main__':
    q=queue()
    q.Enqueue(20)
    q.Enqueue(30)
    q.Enqueue(40)
    q.queueDisplay()
    q.Enqueue(90)
    q.Enqueue(60)
    q.Dequeue()
    q.queueDisplay()
    
        


          
    
