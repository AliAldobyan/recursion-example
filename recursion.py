def sum_of_numbers(numbers):
    sum = 0

    for num in numbers:
        if type(num) == list:
            sum += sum_of_numbers(num)
        else:
            sum += num
    return sum


numbers = [
    [1, 2, 3, 4],
    [3, 6, [5, 6], 8, 2,[2, 4], 9],
    [4, 2, [6, 7, [2, 6, 1]]]
]

print(f"The sum is: {sum_of_numbers(numbers)}")
