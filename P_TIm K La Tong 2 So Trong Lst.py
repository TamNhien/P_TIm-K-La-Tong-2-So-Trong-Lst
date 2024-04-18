def has_pair_with_sum(num, k):
    seen = set()
    for num in nums:
        complement = k - num
        if complement in seen:
            return True
        seen.add(num)
    return False

# Ví dụ sử dụng
nums = [10, 15, 3, 7]
k = 17
print(has_pair_with_sum(nums, k))