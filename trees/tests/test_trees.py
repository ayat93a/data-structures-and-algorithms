from trees.trees import BinaryTree , TNode  , Queue
# from stack_and_queue.queue import Queue


def test_empty_tree():
    actual = print(BinaryTree())
    expected = None
    assert actual == expected

def test_Breadth_first():
    tree = BinaryTree()
    node1 = TNode('A')
    tree.root = node1
    node2 = TNode('B')
    node3 = TNode('C')
    node4 = TNode('D')
    node5 = TNode('E')
    node6=TNode('F')
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right= node5
    node3.left= node6
    actual = tree.Breadth_first()
    expected = ['A', 'B', 'C', 'D', 'E', 'F']
    assert expected ==  actual 
