
from unittest import result


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

        def is_empty(self):
            if self.top == None:
                return True
            return False

        def __str__(self):
            if self.top is None:
                print('empty list')
                return

            itr= self.top
            llstr= '"'
            while itr :
                llstr= llstr  +str(itr.value) + '-> ' 
                itr=itr.next
            llstr+='NULL"'
            return llstr 

class Queue:

    def __init__(self):
        self.front = None


    def enqueue(self , str):
        for value in str:
            if self.front == None:
                self.front= Node(value , None)
            else :
                itr = self.front
                while itr.next:
                    itr = itr.next
                itr.next = Node(value , None)
        return 

    def dequeue(self):

        if self.front == None:
            raise False
        itr = self.front
        node = self.front.value
        self.front= itr.next  
        return node

    def is_empty(self):
        if self.front == None:
            return True
        return False

    def dequeue_by_value(self , value):
        if self.front.value == value:
            node = self.front.value
            self.front = self.front.next
            return 
        itr = self.front
        while itr :
                if itr.next.value == value:
                    node = itr.next.value
                    valuee = itr.next.value
                    itr.next = itr.next.next
                    return 
                itr = itr.next
        return 


    def validate_brackets(self):

        close_stack = Stack()
        open_stack = Stack()
        open_ = ['['  , '{'  , '('  ]
        close = [ ']' ,  '}' ,  ')']
        itr = self.front
        while itr:
            for i in open_:
                if itr.value == i:
                    open_stack.push(i)
            itr = itr.next


        itr = self.front
        while itr:
            for i in close:
                if itr.value == i:
                    close_stack.push(i)
            itr = itr.next

        print(f' 1 {open_stack}')
        print(f'1{close_stack}')   

        current = open_stack.top
        while current :
            
            while current.value == '{':
                while current.next:
                    if current.next.value == '}':
                        open_stack.pop()
                        close_stack.pop()
                    current.next= current.next.next
                

            if current.value == '(':
                while current.next:
                    if current.next.value == ')':
                        open_stack.pop()
                        close_stack.pop()
                    current.next = current.next.next
                
            if current.value == '[':
                while current.next:
                    if current.next.value == ']':
                        open_stack.pop()
                        close_stack.pop()
                    current.next = current.next.next
                    
            current = current.next  

            # print(f'2{open_stack}')
            # print(f'2{close_stack}') 
            
        if open_stack.is_empty == True and close_stack.is_empty == True :
            result = True
        else:
            result = False

        return result


        # new_queue = Queue()

        # char = ['[' , ']' , '{' , '}' , '(' , ')']
        
        # itr = self.front
        # while itr:
        #     for i in char :
        #         if itr.value == i:
        #             new_queue.enqueue(i)
        #     itr = itr.next
        # print(new_queue)


        # current = new_queue.front
        # while current :
        #     if current.value == '{':
        #         while current.next:
        #             if current.next.value == '}':
        #                 new_queue.dequeue_by_value('{')
        #                 new_queue.dequeue_by_value('}')
        #             current.next = current.next.next  
                
            
        #     if current.value == '(':
        #         while current.next:
        #             if current.next.value == ')':
        #                 new_queue.dequeue_by_value('(')
        #                 new_queue.dequeue_by_value(')')
        #             current.next = current.next.next

        #     if current.value == '[':
        #         while current.next:
        #             if current.next.value == ']':
        #                 new_queue.dequeue_by_value('[')
        #                 new_queue.dequeue_by_value(']')
        #             current.next = current.next.next
                    
        #     current = current.next
        #     print(new_queue)
        # if new_queue.is_empty == True :
        #     result = True
        #     print('hi')
        # else :
        #     result = False
        
        # return result

        # new_queue = Stack()
        # char = ['[' , ']' , '{' , '}' , '(' , ')']
        
        # itr = self.front
        # while itr:
        #     for i in char :
        #         if itr.value == i:
        #             new_queue.push(i)
        #     itr = itr.next
        # print(new_queue)
    def __str__(self):
            if self.front is None:
                print('empty list')
                return

            itr= self.front
            llstr= '"'
            while itr :
                llstr= llstr  +str(itr.value) + '-> ' 
                itr=itr.next
            llstr+='NULL"'
            return llstr 


if __name__ == '__main__':
    word = Queue()
    word.enqueue('{{aayat}}a')
    print(word.__str__())
    print(word.validate_brackets())

    




