import solution

test = solution.Solution()

def test_example_1():
    assert test.isValid('()') == True

def test_example_2():
    assert test.isValid('()[]{}') == True

def test_example_3():
    assert test.isValid('(]') == False

def test_example_4():
    assert test.isValid('([])') == True

def test_example_5():
    assert test.isValid('([)]') == False

def test_example_6():
    assert test.isValid('(') == False