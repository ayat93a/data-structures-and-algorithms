
class Node:

    def __init__(self, value = None , next =  None):
        self.value= value
        self.next=next
# value is the data stored in the node
# next is a pointer to the next element
    
class LinkedList:


    def __init__(self):
        self.head = None
# create empty list
    def create_empty_list():
        ll = LinkedList()
        return ll

# take a list of value and create a new fresh linked list
    def insert_values(self,value_list):
        self.head = None

        for value in value_list:
            self.insert_at_end(value)
        return

# <<<< TASK REQUIREMENT 
# insert at beginning of array --> insert the first element'head'
    def insert_at_beginning(self,value):
        #Node(value , self.head) --> value : any value , self.head --> the next node address
        if value == None:
            raise TypeError ('you must give a value to intrest')

        node = Node(value , self.head)
        self.head=node
        return

# insert at end 'append'
    def insert_at_end(self,value):
        if self.head is None:
            self.head = Node(value,None)
            return
        itr = self.head
        # if itr.next is true that mean that the node is not the last one, when the condition is false --> go out side the loop
        while itr.next: 
            itr = itr.next 
        itr.next = Node(value,None)
        return



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
        return    
        
# insert a value at a definded location 
    def insert_at(self , index , value):
        if index < 0 or index >= self.get_length():
            # raise Exception ('unvailed index , max number to input as index is {self.get_length()}')
            raise Exception ('unvailed index')
        if index == 0 :
            self.insert_at_beginning(value)
        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                node =  Node(value , itr.next)
                # itr.next because you are in the previous element
                itr.next= node
                break
            itr = itr.next
            count+=1
        return

# <<<< TASK REQUIREMENT 
# search about the first occurance of a specific value
    def includes (self , value):
        
            if self.head is None: 
                raise Exception ('this is an empty list')

            if value == None:
                raise TypeError ('you must give a value to intrest')

            else:
            # since the count start from 0 --> it also can refered to the index
                try:
                    itr =  self.head
                    while itr:
                        if itr.value == value:
                            return True

                        itr = itr.next
                    
                    return False
                
                except TypeError: 

                    raise ('you must give a value to find it')
                    


# first step to find the value to insert after 
# add a value after that value
    def insert_after_value(self, value_after , value_to_insert):

        if self.head == None:
            return

        itr =  self.head
        while itr:
            if itr.value == value_after:
                itr.next=Node(value_to_insert , itr.next)
            itr = itr.next
        return

        # how to handle the case that when the give value_after is not exist?
        
        

    
    def remove_by_value(self,value):
        
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next
            return

        itr =  self.head
        while itr:
            if itr.value == value:
                itr=itr.next.next
                break
            itr= itr.next
        return

# <<<< TASK REQUIREMENT 

    def __repr__(self) :
        return self.__repr__()

    def __str__(self):
        if self.head is None:
            print('empty list')
            return

        itr= self.head
        llstr= '"'
        # if itr is true that mean that the node has a value, when the condition is false --> go out side the loop 
        while itr :
            llstr= llstr + '{' +str(itr.value)+ '}' +'-> ' 
            itr=itr.next
        llstr+='NULL"'
        return llstr 




if __name__== "__main__":
    ll=  LinkedList()
    # ll.insert_at_beginning(['engineer' , 1])
    # ll.insert_at_beginning('civil')
    # ll.insert_at_beginning('ayat')
    # ll.insert_at_beginning('python')
    # ll.remove_at_index(2)
    ll = LinkedList()
    # ll.insert_at_beginning([1000 , 1])
    # ll.insert_at_beginning('civil')
    # ll.insert_at_beginning('ayat')
    # ll.insert_at_beginning('python')
    # ll.insert_at(0, 'a')
    ll.insert_at_beginning([1000 , 1])
    ll.insert_at_beginning('civil')
    ll.insert_at_beginning('ayat')
    ll.insert_at_beginning('python')
    # ll.insert_after_value('civil' , '5')
    ll.remove_by_value('civil')
    print(ll.__str__())
    # ll.insert_values('a')
    # ll.insert_at_beginning('engineer')
    # ll.insert_at_beginning('civil')
    # print(ll.__str__())
    # ll = ['ayat' , 'barakat' , 'alkayed' ]
    # ll.get_length()
    # print(ll.__str__())
    # ll.insert_at_beginning(93)
    # ll.insert_at_beginning(28)
    # ll.insert_at_beginning(8)
    # ll.__str__()
    # # # tyr to insert the date
    # ll.insert_at_end('end')
    # ll.insert_at_end('ayat')
    # ll.__str__()
    # print('length : ' , ll.get_length())
    # ll.remove_at_index(2)
    # print(ll.__str__())
    # ll.remove_at_index(3)
    # print(ll.__str__())
    # ll.__str__()
    # ll.insert_at(0 ,"hi")
    # ll.__str__()
    # print(ll.includes(5))
    # ll.__str__()
    # ll.insert_after_value(15 , 'i am here')
    # ll.__str__()
    # ll.insert_after_value('hi' , 'barakat is my lovely dad')
    # ll.__str__()
    # ll.remove_by_value('hi')
    # ll.__str__()
    # ll.insert_values(['ayat' , 'barakat' , 'alkayed'])
    # ll.__str__()