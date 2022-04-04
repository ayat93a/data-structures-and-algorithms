
from itertools import count
import queue


class Node :

    def __init__(self , value , next = None):
        self.value = value
        self.next = next


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

    def validate_brackets(self):
        new_queue = Queue()
        char = ['[' , ']' , '{' , '}' , '(' , ')']
        itr = self.front
        for i in char :
            while itr :
                if itr.value == i :
                    new_queue.enqueue(i)
                itr = itr.next

        itr = new_queue.front
        while itr :
            if itr.value == '{':
                while itr.next.value:
                    if itr.next.value == '}':
                        itr = itr.next
                        itr.next = itr.next.next
            if itr.value == '[':
                while itr.next.value:
                    if itr.next.value == ']':
                        itr = itr.next
                        itr.next = itr.next.next
            if itr.value == '(':
                while itr.next.value:
                    if itr.next.value == ')':
                        itr = itr.next
                        itr.next = itr.next.next
            else:
                itr = itr.next
        if new_queue.is_empty == True :
            print('hi')
        else:
            print('hii')            





        # new_queue =  Queue()
        # itr = self.front
        # while itr:
        #     if itr.value == '{' :
        #         new_queue.enqueue('{')
        #         while itr.next :
        #             if itr.value == '}':
        #                 new_queue.dequeue() 
        #                 itr = itr.next 
        #             else:
        #                 itr = itr.next 
        #     itr = itr.next
        # return new_queue.is_empty()
             
            



        #         while itr.next :
        #             if itr.next.value == '}':
        #                 itr.value = ' '
        #                 itr.next.value = ''
        #                 return  True
        #             if itr.next != None:
        #                 itr = itr.next
        
        #     itr = itr.next
        # itr = self.front
        # while itr:
        #     if itr.value == '{' :
        #         return False
        #     itr = itr.next
        


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
    word.enqueue('{ayat}')
    print(word.__str__())
    print(word.validate_brackets)
    
