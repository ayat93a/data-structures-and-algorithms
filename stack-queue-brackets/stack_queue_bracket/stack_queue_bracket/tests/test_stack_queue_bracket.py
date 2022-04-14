from stack_queue_bracket.stack_queue_bracket import validate_brackets

def test_val1():
    assert validate_brackets("{***}") == True

def test_val2():
    assert validate_brackets("(](") == False



'''the problem in the repo '''