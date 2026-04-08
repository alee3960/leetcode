import solution

test = solution.Solution()

def test_example_1():
    assert test.isPalindrome(121) == True

def test_example_2():
    assert test.isPalindrome(-121) == False

def test_example_3():
    assert test.isPalindrome(10) == False

def test_example_4():
    assert test.isPalindrome(11) == True

def test_example_5():
    assert test.isPalindrome(0) == False

def test_example_6():
    assert test.isPalindrome(3333) == True

def test_example_7():
    assert test.isPalindrome(-1) == False