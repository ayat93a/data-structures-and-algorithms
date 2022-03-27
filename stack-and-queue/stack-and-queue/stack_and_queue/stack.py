

class Node :

    def __init__(self , value , next = None):
        self.value = value
        self.next = next


class Stack:

    def __init__(self):
        self.top = None

    
    def push(self , value):
        if self.top == None:
            self.top = Node (value , None)
            return
        node = Node(value , self.top)
        self.top = node
        return


    def pop(self):

        if self.top == None:
            raise('empty stack')
        itr = self.top
        external_storage = self.top.value
        self.top = itr.next  
        return external_storage

    def peek(self):
        if self.top == None:
            raise('empty stack')
        node = self.top.value
        return node

    def is_empty(self):
        if self.top == None:
            return True
        return False


    def __repr__(self) :
            return self.__repr__()

    def to_string(self):
            self.__str__()

    def __str__(self):
            if self.top is None:
                print('empty list')
                return

            itr= self.top
            llstr= '"'
            while itr :
                llstr= llstr + '{' +str(itr.value)+ '}' +'-> ' 
                itr=itr.next
            llstr+='NULL"'
            return llstr 

if __name__ == '__main__':

    stack = Stack()
    stack.push(2)
    stack.push(5)
    stack.push(7)
    # print(stack.pop())
    print(stack.peek())
    # print(stack.is_empty())
    print (stack)
    
  
