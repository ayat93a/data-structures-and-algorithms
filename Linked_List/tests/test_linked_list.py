from Linked_list.Linked_list import Node , LinkedList


def test_create_empty_list():
    ll = LinkedList()
    actual = ll.__str__()
    expected = None
    assert actual == expected


def test_insert_values():
    ll = LinkedList()
    ll.insert_values('alkayed')
    ll.insert_values('barakat')
    ll.insert_values('ayat')
    actual =ll.__str__()
    expected = '{ayat}-> {barakat}-> {alkayed}-> NULL'
    # print(actual)
    assert actual == expected