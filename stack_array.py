def create_stack():
    stack=[]
    return(stack)
def isEmpty(stack):
    if(len(stack)==0):
        return True
    else:
        return False
def push(stack,data):
    stack.append(data)
    print(data,"is pushed inside the stack")
def pop1(stack):
    if(isEmpty(stack)):
        print("stack is empty")
    else:
        poped=stack.pop()
        print(poped,"is deleted")
def peek(stack):
    if(isEmpty(stack)):
        print("stack is empty")
    else:
        print(stack[len(stack)-1])
stack1=create_stack()
push(stack1,10)
push(stack1,20)
push(stack1,30)
pop1(stack1)
pop1(stack1)
peek(stack1)
