def second_largest(nums):
    largest = second = float('-inf')
    for num in nums:
        if num > largest:
            second = largest
            largest = num
        elif num > second and num != largest:
            second = num
    return second if second != float('-inf') else None

nums = list(map(int, input("Enter numbers separated by space: ").split()))
result = second_largest(nums)
print("Second largest number:", result if result else "Not available")
