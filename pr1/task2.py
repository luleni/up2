print('Введите целочисленный массив nums: ')
nums = [input() for i in range(6)]
print(nums)
def counter(nums):
    for i in nums:
        countt = nums.count(i)
        if countt >=2:
            return True
        return False
print(counter(nums))