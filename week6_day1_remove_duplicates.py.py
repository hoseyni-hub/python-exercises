# Week 6 - Day 1
# Task: Remove duplicates from a list and sort it in ascending order

def remove_duplicates_and_sort(numbers):
    unique_numbers = list(set(numbers))  # remove duplicates using set
    unique_numbers.sort()  # sort in ascending order
    return unique_numbers

# Example usage
numbers = [4, 2, 9, 2, 4, 7, 1, 9, 3]
print("Original list:", numbers)
print("Unique sorted list:", remove_duplicates_and_sort(numbers))