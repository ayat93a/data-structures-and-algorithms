
from stack_and_queue.stack import Stack

class TNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
  
  
class BinaryTree:
    def __init__(self):
        self.root = None

    def Pre_order_rec(self):
        '''root --> left -- > right'''
        def _traverse(node):
            if node:
                print(node.value)

                _traverse(node.left)

                _traverse(node.right)

        _traverse(self.root)

    def In_order_rec(self):
        '''left --> root --> right'''

        def _traverse(node):
            if node:
                _traverse(node.left)
                
                print(node.value)

                _traverse(node.right)
            
        _traverse(self.root)
   
              
    def Post_ord_rec(self):
        '''left --> right --> root'''
        def _traverse(node):
            if node :
                _traverse(node.left)

                _traverse(node.right)            

                print(node.value)   

        _traverse(self.root)


class Binary_search_tree(BinaryTree):
    
    def add(self):
        pass

    def Contains(self):
        pass







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

    tree.Pre_order_rec()
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