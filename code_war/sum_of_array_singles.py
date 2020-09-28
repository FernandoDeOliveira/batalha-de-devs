""""
In this Kata, you will be given an array of numbers in which two numbers occur once and the rest occur only twice.
Your task will be to return the sum of the numbers that occur only once.

For example, repeats([4,5,7,5,4,8]) = 15 because only the numbers 7 and 8 occur once, and their sum is 15.
"""
from memory_profiler import profile


@profile
def repeats(arr: list):
    arr_copy = arr.copy()
    not_repeats = []
    while arr_copy:
        num = arr_copy.pop(0)
        if num in arr_copy:
            [arr_copy.remove(same) for same in arr_copy if same == num]
        else:
            not_repeats.append(num)
    return sum(not_repeats)
