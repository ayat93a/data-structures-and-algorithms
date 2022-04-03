
# Challenge Summary
- Create a class called AnimalShelter which holds only dogs and cats.
- The shelter operates using a first-in, first-out approach. --> queue 
## Whiteboard Process
[white board](/animal_shelter.PNG)

## Approach & Efficiency
- enqueue method --> give animal and value as arguments 
animal is the type and value is the name of that type 
1. space : O(1)
2. time : O(1)
- dequeue : 2 types of dequeue was provided 
- dequeue by pref only --> return the first animal  that has that pref entered the queue 
- dequeue by pref and name : return the animal that has that pref with a spesific name 'return a specific animal'
1. space : O(1)
2. time : O(1)

## Solution
[Code ](../stack_queue_animal_shelter/stack_queue_animal_shelter/stack_queue_animal_shelter.py)
