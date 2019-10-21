def two_sum(nums, target):
    table = {}
    for index in range(len(nums)):
        element = nums[index]
        complement = target - element
        if complement in table:
            return [table[complement], index]
        table[element] = index
    return [0, 0]


# TEST CASE
nums = [1, 4, 7, 3, 5]
target = 10

elements = two_sum(nums, target)
print(nums[elements[0]], " + ", nums[elements[1]], " = ", target)