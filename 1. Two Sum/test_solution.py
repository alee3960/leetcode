import solution

test = solution.Solution()
nums = [[2,7,11,15], [3,2,4], [3,3]]
targets = [9, 6, 6]

def test_example_1():
    assert test.twoSum(nums[0], targets[0]) == [0,1]

def test_example_2():
    assert test.twoSum(nums[1], targets[1]) == [1,2]

def test_example_3():
    assert test.twoSum(nums[2], targets[2]) == [0,1]

test_example_1()
test_example_2()
test_example_3()