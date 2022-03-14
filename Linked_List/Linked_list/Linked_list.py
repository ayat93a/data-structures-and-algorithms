


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
            self.append(value)
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
    def append(self,value):
        if self.head is None:
            self.head = Node(value,None)
            return
        itr = self.head
        # if itr.next is true that mean that the node is not the last one, when the condition is false --> go out side the loop
        while itr.next: 
            itr = itr.next 
        itr.next = Node(value,itr.next)
        return



# length of the linked list
    # def get_length(self):
    #     count = 0
    #     itr = self.head
    #     while itr :
    #         count += 1
    #         itr = itr.next
    #     return count

        
# Removing element with a given index 
    # def remove_at_index(self , index):
    #     if index < 0 or index >= self.get_length():
    #         # raise Exception ('unvailed index , max number to input as index is {self.get_length()}')
    #         raise Exception ('unvailed index')
    #     if index == 0 :
    #         # try to remove the first element in the list 'head'
    #         self.head = self.head.next
    #         return

            
        
    #     count = 0
    #     itr = self.head
    #     while itr:
    #         if count == index -1 : 
    #             itr.next =itr.next.next
    #             # try if inedx and itr
    #             break

    #         itr = itr.next
    #         count +=1
    #     return    
        
# insert a value at a definded location 
    # def insert_at(self , index , value):
    #     if index < 0 or index >= self.get_length():
    #         # raise Exception ('unvailed index , max number to input as index is {self.get_length()}')
    #         raise Exception ('unvailed index')
    #     if index == 0 :
    #         self.insert_at_beginning(value)
    #     count = 0
    #     itr = self.head
    #     while itr:
    #         if count == index -1:
    #             node =  Node(value , itr.next)
    #             # itr.next because you are in the previous element
    #             itr.next= node
    #             break
    #         itr = itr.next
    #         count+=1
    #     return

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
# value --> value to insert afte, new_value--> to insert
    def insert_after(self, value , new_value):

        if self.head == None:
            return

        itr =  self.head
        while itr:
            if itr.value == value:
                itr.next=Node(new_value , itr.next)
            itr = itr.next
        return

        # how to handle the case that when the give value_after is not exist?

# first step to find the value to insert befor ==> became itr.next = itr.next.next , itr.next.value = new value
# add a value after that value

    def insert_befor(self, value , new_value):
         
        if self.head == None:
            return

        if self.head.value == value:
            self.insert_at_beginning(new_value)
            return

        itr =  self.head
        while itr:
            if self.head == None:
                break

            if itr.next.value == value: 
                node = Node(new_value , itr.next)
                node.next= itr.next
                itr.next = node    
                return
            else:
                return (-1)

    
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


    def to_string(self):
        self.__str__()

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


# updated

if __name__== "__main__":
    ll=  LinkedList()
    ll = LinkedList()
    ll.insert_at_beginning('civil')
    ll.insert_at_beginning('ayat')
    ll.insert_at_beginning('python')
    ll.insert_at_beginning(16)
    ll.insert_befor(16 , 'softwear')
    ll.insert_befor('ayat' , 'devs')
    ll = ll.__str__()
    print(ll)
