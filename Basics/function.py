def find_max(numbers):
    """
    Function to find the maximum number in a list.
    :param numbers: list of integers or floats
    :return: maximum value in the list
    """
    if not numbers:
        return None  # return None if the list is empty
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value


# Example usage:
sample_list = [3, 7, 2, 9, 5]
print("List:", sample_list)
print("Maximum number:", find_max(sample_list))
