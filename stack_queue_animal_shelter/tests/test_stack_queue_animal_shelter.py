
from stack_queue_animal_shelter.stack_queue_animal_shelter import StackQueueAnimalShelter, Node

def test_create_class():
    shelter = StackQueueAnimalShelter()
    actual = shelter.__str__()
    expected = None
    assert actual == expected

def test_enqueue():
    shelter = StackQueueAnimalShelter()
    shelter.enqueue('cat'  , 'lolo')
    shelter.enqueue('dog' ,'roro')
    shelter.enqueue('dog' , 'meme' )
    shelter.enqueue('cat'  , 'soso')
    shelter.enqueue('dog' , 'jojo' )
    shelter.enqueue('dog' , 'jojo' )
    shelter.enqueue('anything' , 'anyname')
    actual = shelter.__str__()
    expected = '"{cat:lolo}-> {dog:roro}-> {dog:meme}-> {cat:soso}-> {dog:jojo}-> {dog:jojo}-> NULL"'
    assert actual == expected

def test_dequeue():
    shelter = StackQueueAnimalShelter()
    shelter.enqueue('cat'  , 'lolo')
    shelter.enqueue('dog' ,'roro')
    shelter.enqueue('dog' , 'meme' )
    shelter.enqueue('cat'  , 'soso')
    shelter.enqueue('dog' , 'jojo' )
    shelter.enqueue('dog' , 'jojo' )
    shelter.enqueue('anything' , 'anyname')
    shelter.dequeue('dog' , 'jojo' )
    actual = shelter.__str__()
    expected = '"{cat:lolo}-> {dog:meme}-> {cat:soso}-> {dog:jojo}-> {dog:jojo}-> NULL"'
    assert actual == expected


def test_dequeue1():
    shelter = StackQueueAnimalShelter()
    shelter.enqueue('cat'  , 'lolo')
    shelter.enqueue('dog' ,'roro')
    shelter.enqueue('dog' , 'meme' )
    shelter.enqueue('cat'  , 'soso')
    shelter.enqueue('dog' , 'jojo' )
    shelter.enqueue('dog' , 'jojo' )
    shelter.enqueue('anything' , 'anyname')
    actual = shelter.dequeue('dog' , 'jojo' )
    expected = 'dog : jojo is dequeued'
    assert actual == expected

def test_dequeue2():
    shelter = StackQueueAnimalShelter()
    shelter.enqueue('cat'  , 'lolo')
    shelter.enqueue('dog' ,'roro')
    shelter.enqueue('dog' , 'meme' )
    shelter.enqueue('cat'  , 'soso')
    shelter.enqueue('dog' , 'jojo' )
    shelter.enqueue('dog' , 'jojo' )
    shelter.enqueue('anything' , 'anyname')
    actual =shelter.dequeue('camel' , 'jojo' )
    expected = None
    assert actual == expected

