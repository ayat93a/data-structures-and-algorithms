
from dataclasses import dataclass
from itertools import count
from tkinter import N

class Node:

    def __init__(self, data = None , next =  None):
        self.data= data
        self.next=next

    
class LinkedList:


    def __init__(self):
        self.head = None
# insert at beginning of array --> insert the first element'head'

    def insert_at_beginning(self,data):
        #Node(data , self.head) --> data : any value , self.head --> the next node address
        node = Node(data , self.head)
        self.head=node


# insert at end 'append'
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        itr = self.head
        # if itr.next is true that mean that the node is not the last one, when the condition is false --> go out side the loop
        while itr.next: 
            itr = itr.next 
        itr.next = Node(data,None)

# take a list of value and create a new fresh linked list
    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


# length of the linked list
    def get_length(self):
        count = 0
        itr = self.head
        while itr :
            count += 1
            itr = itr.next
        return count

        
# Removing element with a given index 
    def remove_at_index(self , index):
        if index < 0 or index >= self.get_length():
            # raise Exception ('unvailed index , max number to input as index is {self.get_length()}')
            raise Exception ('unvailed index')
        if index == 0 :
            # try to remove the first element in the list 'head'
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index -1 : 
                itr.next =itr.next.next
                # try if inedx and itr
                break

            itr = itr.next
            count +=1
        
# insert a value at a definded location 
    def insert_at(self , index , data):
        if index < 0 or index >= self.get_length():
            # raise Exception ('unvailed index , max number to input as index is {self.get_length()}')
            raise Exception ('unvailed index')
        if index == 0 :
            self.insert_at_beginning(data)
        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                node =  Node(data , itr.next)
                # itr.next because you are in the previous element
                itr.next= node
                break
            itr = itr.next
            count+=1

    def includes (self , data):
        pass




    def __str__(self):
        if self.head is None:
            print('empty list')
            return

        itr= self.head
        llstr= " "
        # if itr is true that mean that the node has a value, when the condition is false --> go out side the loop 
        while itr :
            llstr=llstr + str(itr.data)+'-->' 
            itr=itr.next
        llstr+=" None"
        print (llstr)




if __name__== "__main__":
    ll=  LinkedList()
    ll.insert_values(['ayat','barakat','alkayed' , 28 , 'python'])
    # ll.insert_at_beginning(53)
    # ll.insert_at_beginning(89)
    # ll.insert_at_end('hamza')
    # ll.insert_at_end('ayat')
    # print('length : ' , ll.get_length())
    ll.__str__()
    ll.remove_at_index(3)
    ll.insert_at(0 ,"hi")
    ll.__str__()

