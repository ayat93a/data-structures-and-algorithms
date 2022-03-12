from Linked_list.Linked_list import LinkedList , Node
import pytest

def test_create_empty_list():
    ll = LinkedList()
    actual = ll.__str__()
    expected = None
    assert actual == expected


def test_insert_values():
    ll = LinkedList()
    ll.insert_values(['ayat' , 'barakat' , 'alkayed'])
    actual =ll.__str__()
    expected = '"{ayat}-> {barakat}-> {alkayed}-> NULL"'
    # print(actual)
    assert actual == expected


def test_insert_at_beginning():
    ll = LinkedList()
    ll.insert_at_beginning('engineer')
    ll.insert_at_beginning('civil')
    actual =ll.__str__()
    expected = '"{civil}-> {engineer}-> NULL"'
    assert actual == expected

def test_insert_at_end():
    ll = LinkedList()
    ll.insert_values(['ayat' , 'barakat' , 'alkayed'  ])
    ll.insert_at_end('28')
    actual =ll.__str__()
    expected = '"{ayat}-> {barakat}-> {alkayed}-> {28}-> NULL"'
    assert actual == expected

def test_get_length():
    ll = LinkedList()
    ll.insert_at_beginning(['engineer' , 1])
    ll.insert_at_beginning('civil')
    ll.insert_at_beginning('ayat')
    ll.insert_at_beginning('python')
    actual =ll.get_length()
    expected = 4
    assert actual == expected

def test_includest():
    ll = LinkedList()
    ll.insert_values (['ayat' , 'barakat' , 'alkayed' ])
    actual = ll.includes('ayat')
    expected = True
    assert actual == expected

def test_includesf():
    ll = LinkedList()
    ll.insert_values (['ayat' , 'barakat' , 'alkayed' ])
    actual = ll.includes('hi')
    expected = False
    assert actual == expected

def test_remove_at_index():
    ll = LinkedList()
    ll.insert_at_beginning([1000 , 1])
    ll.insert_at_beginning('civil')
    ll.insert_at_beginning('ayat')
    ll.insert_at_beginning('python')
    ll.remove_at_index(2)
    actual = ll.__str__()
    expected = '"{python}-> {ayat}-> {[1000, 1]}-> NULL"'
    assert actual == expected

def test_insert_at():
    ll = LinkedList()
    ll.insert_at_beginning([1000 , 1])
    ll.insert_at_beginning('civil')
    ll.insert_at_beginning('ayat')
    ll.insert_at_beginning('python')
    ll.insert_at(0, 'a')
    actual = ll.__str__()
    expected = '"{a}-> {python}-> {ayat}-> {civil}-> {[1000, 1]}-> NULL"'
    assert actual == expected

def test_insert_after_value():
    ll = LinkedList()
    ll.insert_at_beginning([1000 , 1])
    ll.insert_at_beginning('civil')
    ll.insert_at_beginning('ayat')
    ll.insert_at_beginning('python')
    ll.insert_after_value('civil' , '5')
    actual = ll.__str__()
    expected = '"{python}-> {ayat}-> {civil}-> {5}-> {[1000, 1]}-> NULL"'
    assert actual == expected


def test_remove_by_value():
    ll = LinkedList()
    ll.insert_at_beginning([1000 , 1])
    ll.insert_at_beginning('civil')
    ll.insert_at_beginning('ayat')
    ll.insert_at_beginning('python')
    ll.remove_by_value('civil')
    actual = ll.__str__()
    expected = '"{python}-> {ayat}-> {civil}-> {[1000, 1]}-> NULL"'
    assert actual == expected


