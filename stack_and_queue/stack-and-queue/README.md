
# Challenge Summary
- Create a new class called pseudo queue --> to create a queue from given 2 stacks 
- given 2 stacks 
- output queue 'FIFO'

## Whiteboard Process
[Whiteboard](./pesudo_queue.PNG)

## Approach & Efficiency
space : O(1)
time : O(n)

## Solution
[code](./stack_and_queue/stack.py)

# Stacks and Queues
## A stack is a data structure that consists of Nodes. Each Node references the next Node in the stack, but does not reference its previous.

Stacks follow these concepts:

- FILO
First In Last Out

This means that the first item added in the stack will be the last item popped out of the stack.

- LIFO
Last In First Out

## Challenge
*apply these methods for stack :*
- Push - Nodes or items that are put into the stack are pushed
- Pop - Nodes or items that are removed from the stack are popped. When you attempt to pop an empty stack an exception will be raised.
- Top - This is the top of the stack.
- Peek - When you peek you will view the value of the top Node in the stack. When you attempt to peek an empty stack an exception will be raised.
- IsEmpty - returns true when stack is empty otherwise returns false.
*apply these methods for queue :*
- Enqueue - Nodes or items that are added to the queue.
- Dequeue - Nodes or items that are removed from the queue. If called when the queue is empty an exception will be raised.
- Front - This is the front/first Node of the queue.
- Peek - When you peek you will view the value of the front Node in the queue. If called when the queue is empty an exception will be raised.
- IsEmpty - returns true when queue is empty otherwise returns false.
## Approach & Efficiency
![](bigO.PNG)

### White board 
[Stack](./stack-algorithm.PNG)
[Queue](./queue%20algo.PNG)

