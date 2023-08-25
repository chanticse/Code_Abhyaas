def second_largest_smallest(numbers):
    if len(numbers) < 2:
        return None, None
    
    largest = second_largest = float('-inf')
    smallest = second_smallest = float('inf')
    
    for num in numbers:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
        
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    
    return second_largest, second_smallest

input_numbers = input("Enter a list of numbers: ")
numbers = list(map(int, input_numbers.split()))

second_largest, second_smallest =second_largest_smallest(numbers)
print("Second largest:", second_largest)
print("Second smallest:", second_smallest)
