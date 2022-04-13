
from tkinter import N
from stack_and_queue.stack import Stack

class TNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
  
  
class BinaryTree(TNode):
    def __init__(self):
        self.root = None

    
    def Pre_order_rec(self):
        '''root --> left -- > right'''
        '''     1- Check if the current node is empty .

                2- Display the data part of the root (or current node).

                3- Traverse the left subtree by recursively calling the in-order function.

                4- Traverse the right subtree by recursively calling the in-order function.'''
        def _traverse(node):
            if node:
                print(node.value)
                if node.left:
                    _traverse(node.left)
                if node.right:
                    _traverse(node.right)

        _traverse(self.root)

    def In_order_rec(self):
        '''left --> root --> right'''
        '''     1- Check if the current node is empty .

                2- Traverse the left subtree by recursively calling the in-order function.

                3- Display the data part of the root (or current node).

                4- Traverse the right subtree by recursively calling the in-order function.'''

        def _traverse(node):
            if node:
                if node.left:
                    _traverse(node.left)
   
                print(node.value)

                if node.right:
                    _traverse(node.right)
            
        _traverse(self.root)
   
              
    def Post_ord_rec(self):
        '''left --> right --> root'''
        '''     1- Check if the current node is empty .

                2- Traverse the left subtree by recursively calling the in-order function.

                3- Traverse the right subtree by recursively calling the in-order function.

                4- Display the data part of the root (or current node).'''

        def _traverse(node):
            if node :
                if node.left:
                    _traverse(node.left)

                if node.right:
                    _traverse(node.right)            

                print(node.value)   

        _traverse(self.root)


class Binary_search_tree(BinaryTree):
    def __init__(self):
        self.root = None
        
    def Contains(self , value):
        if self.root == None:
            return 'empty'

        def _contain(node):
            if node:
                if node.value == value:
                    return True
                elif node.value > value :
                    return _contain(node.left)
                elif node.value < value :
                    return _contain(node.right)
                
            return False
        return _contain(self.root)
         
    
    def Add(self, value):
        '''best way to traverse the search tree to add a new mode --> pre-order traverse'''
        '''root --> left -- > right'''
        # if contain function return false then go
        itr = self.root
        pointer = None
        while itr:
            pointer = itr
            if itr.value > value :
                itr = itr.left
            else:
                itr = itr.right
        if pointer == None:
            self.root = TNode(value)
        elif pointer.value > value:
            pointer.left = TNode(value)
        else:
            pointer.right = TNode(value)

    
    







if __name__ == '__main__':

    node1 = TNode('A')
    node2 = TNode('B')
    node3 = TNode('C')
    node4 = TNode('D')
    node5 = TNode('E')
    node6=TNode('F')
    node7=TNode('G')
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right= node5
    node3.left= node6
    # node3.right = node7
    
    tree = BinaryTree()
    tree.root = node1

    binary_search_tree = Binary_search_tree()
    binary_search_tree.Add(20)
    binary_search_tree.Add(5)
    binary_search_tree.Add(30)
    binary_search_tree.Add(1)
    binary_search_tree.Add(15)
    binary_search_tree.Add(9)
    binary_search_tree.Add(12)
    binary_search_tree.Add(25)
    binary_search_tree.Add(40)
    binary_search_tree.Add(7)

    # binary_search_tree.Pre_order_rec()
    print(binary_search_tree.Contains(1))
    # print(binary_search_tree.root.left.left.value)
    # tree.Pre_order_rec()
    # tree.In_order_rec()
    # tree.Post_ord_rec()



 # def In_order_(self)
        # while not stack.is_empty() and itr:
            
        #     while itr.left:
        #         stack.push(itr.left)
        #         itr = itr.left
        #     itr = stack.pop()
        #     print(itr.value)
            
        #     while itr.right:
        #         stack.push(itr.right)
        #         itr = itr.right
        #     itr = stack.pop()
        #     print(itr.value)
            
        #     itr = itr.right
        #     stack.push(itr)
        # return

     # def Pre_order(self):
    #     '''Root --> Left --> Right'''

    #     stack = Stack()
    #     itr = self.root 
    #     stack.push(itr)

    #     while not stack.is_empty():
    #         itr = stack.pop()
    #         print(itr.value)
           
    #         if itr.right:
    #            stack.push(itr.right)

    #         if itr.left:
    #             stack.push(itr.left)