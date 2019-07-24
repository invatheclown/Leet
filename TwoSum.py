def twoSum(nums, target):
    for a in range(0, len(nums)):
        if nums[a] < target:
            reminder = target - nums[a]
            for b in range(a + 1, len(nums)):
                if nums[b] == reminder:
                    return [a,b]
                    break
                else:
                    continue
        else:
            continue


t = 9
c = [1, 7, 8, 15]

dicks = twoSum(c, 9)

print(dicks)
