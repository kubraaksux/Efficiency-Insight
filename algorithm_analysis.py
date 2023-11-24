import random
import time


def algorithm(arr):
    # Implemented to match the logic described in the pseudocode
    y = 0
    n = len(arr)

    for i in range(n):
        if arr[i] == 0:
            for j in range(i, n):
                y += 1
                k = n
                while k > 0:
                    k = k // 3
                    y += 1
        elif arr[i] == 1:
            for m in range(i, n):
                y += 1
                for l in range(m, n):
                    for t in range(n, 0, -1):
                        z = n
                        while z > 0:
                            y += 1
                            z -= t
        else:  # arr[i] is 2
            y += 1
            p = 0
            while p < n:
                for j in range(p ** 2):
                    y += 1
                p += 1

    return y


def generate_different_cases(sizes):

    # Created different test cases for each in [sizes] and returns a dictionary with the test cases.
    # sizes -> A list of integers representing the sizes of test cases to generate.
    # dict -> First key is the size, second key is the case type.

    cases_dict = {}
    for size in sizes:
        cases_dict[size] = {

            #  Best case: List with all elements as 2
            # Worst case: List with all elements as 1
            # Average case: Random 0s, 1s, and 2s

            'best': [2] * size,
            'worst': [1] * size,
            'average': [random.randint(0, 2) for _ in range(size)]
        }
    return cases_dict


def measure_time(func, test_cases):

    # Calculation and print statements for the execution time.
    # test_cases (dict) -> A dictionary with test case data.

    for size, cases in test_cases.items():
        for case_type, case_data in cases.items():
            start = time.time()
            func(case_data)
            end = time.time()
            print(
                f"{case_type.capitalize()} case for size {size} took {end - start:.6f} seconds to execute.")


sizes_to_test = [1, 5, 10, 20, 30, 40, 50, 60,
                 70, 80, 90, 100, 110, 120, 130, 140, 150]
cases = generate_different_cases(sizes_to_test)
measure_time(algorithm, cases)
