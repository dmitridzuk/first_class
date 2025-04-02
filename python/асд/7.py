def max_subarray(nums):
    if not nums:
        return 0, -1, -1
    max_sum = current_sum = nums[0]
    start = end = 0
    temp_start = 0
    for i in range(1, len(nums)):
        if current_sum + nums[i] > nums[i]:
            current_sum += nums[i]
        else:
            current_sum = nums[i]
            temp_start = i
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i
    return max_sum, start, end

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum, start, end = max_subarray(nums)
print(f"Максимальная сумма подмассива: {max_sum}")
print(f"Подмассив: {nums[start:end + 1]}")