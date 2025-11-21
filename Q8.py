# Program to create a dictionary of odd numbers and their cubes using dictionary comprehension

nums = list(map(int, input("Enter numbers separated by space: ").split()))

odd_num_cubes = {x: x**3 for x in nums if x % 2 != 0}

print(odd_num_cubes)
