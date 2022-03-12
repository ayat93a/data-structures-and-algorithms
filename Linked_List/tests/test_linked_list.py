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

# def test_get_length():
#     ll = ['ayat' , 'barakat' , 'alkayed'  ]
#     actual =ll.get_length()
#     expected = 3
#     assert actual == expected

def test_includes():
    ll = ['ayat' , 'barakat' , 'alkayed' ]
    actual = ll.includes('ayat')
    expected = True
    assert actual == expected


