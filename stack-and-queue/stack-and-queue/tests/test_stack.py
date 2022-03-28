

import queue
from stack_and_queue.stack import Stack , Node , Pseudo_queue

def test_push0():
    stack=Stack()
    stack.push(2)
    actual = stack.__str__()
    expected = '"{2}-> NULL"'
    assert actual == expected

def test_push1():
    stack=Stack()
    stack.push(2)
    stack.push(5)
    stack.push(7)
    actual = stack.__str__()
    expected = '"{7}-> {5}-> {2}-> NULL"'
    assert actual == expected

def test_pop0():
    stack=Stack()
    stack.push(2)
    stack.push(5)
    stack.push(7)
    actual = stack.pop()
    expected = 7
    assert actual == expected

def test_pop1():
    stack=Stack()
    stack.push(2)
    stack.push(5)
    stack.push(7)
    stack.pop()
    stack.pop()
    stack.pop()
    actual = stack.__str__()
    expected = None
    assert actual == expected

def test_empty_stack ():
    stack=Stack()
    actual = stack.__str__()
    expected = None
    assert actual == expected

# def test_empty_stack_raise_error ():
#     stack=Stack()
#     stack.peek()
#     actual = stack.__str__()
#     expected = None
#     assert actual == expected



def test_pop2():
    stack=Stack()
    stack.push(2)
    stack.push(5)
    stack.push(7)
    stack.pop()
    actual = stack.__str__()
    expected = '"{5}-> {2}-> NULL"'
    assert actual == expected


def test_peek():
    stack=Stack()
    stack.push(2)
    stack.push(5)
    stack.push(7)
    actual = stack.peek()
    expected = 7
    assert actual == expected
 
def test_peek2():
    stack=Stack()
    stack.push(2)
    stack.push(5)
    stack.push(7)
    stack.peek()
    actual = stack.__str__()
    expected = '"{7}-> {5}-> {2}-> NULL"'
    assert actual == expected

def test_is_empty1():
    stack=Stack()
    actual = stack.is_empty()
    expected = True
    assert actual == expected

def test_is_empty2():
    stack=Stack()
    stack.push(2)
    stack.push(5)
    stack.push(7)
    actual = stack.is_empty()
    expected = False
    assert actual == expected


def test_enqueue():
    queue= Pseudo_queue()
    # stack1.enqueue(1)
    # stack1.enqueue(2)
    # stack1.enqueue(3)
    # stack1.enqueue(4)
    assert queue.enqueue('ayat') == 'ayat'
    
