
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
    
    def add(self , value):
            '''root --> left -- > right'''
            
            def _add(node):
                
                if node:
                    # print(node.value)
                    if value >= node.value:
                        new_root = TNode(value , None , node)
                        print(node.value)
                        

                    if value > node.left.value :
                        _add(node.right)
                        if value > node :
                            new_node = TNode(value , None , node)
                            print('hi')
                        
                    _add(node.left)

                    _add(node.right)

            _add(self.root)





    def Contains(self):
        pass







if __name__ == '__main__':

    node1 = TNode(60)
    node2 = TNode(30)
    node3 = TNode(50)
    node4 = TNode(10)
    node5 = TNode(20)
    node6=TNode(40)
    # node7=TNode(7)
    # node1 = TNode('A')
    # node2 = TNode('B')
    # node3 = TNode('C')
    # node4 = TNode('D')
    # node5 = TNode('E')
    # node6=TNode('F')
    # node7=TNode('G')
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right= node5
    node3.left= node6
    # node3.right = node7
    

    tree = BinaryTree()
    tree.root = node1

    binary_search_tree = Binary_search_tree()
    binary_search_tree.add(35)

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