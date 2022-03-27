
from stack_and_queue.stack import Stack , Node

def test_push():
    stack=Stack()
    stack.push(2)
    stack.push(5)
    stack.push(7)
    actual = stack.__str__()
    expected = '"{7}-> {5}-> {2}-> NULL"'
    assert actual == expected

def test_pop():
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
