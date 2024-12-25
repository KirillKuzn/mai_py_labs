"""Перераспределение по размеру"""

nums = [1, 2, 3, 4, 5]
ans = [x for x in nums if x > (min(nums) + max(nums)) / 2] + [x for x in nums if x <= (min(nums) + max(nums)) / 2]
print(ans)