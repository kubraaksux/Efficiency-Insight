import random
import time


def execute_algorithm(arr):
    # Implemented to match the logic described in the pseudocode.
    # Counts the number of operations based on specific conditions encountered in the array.
    # arr -> The input array containing 0s, 1s, and 2s.
    # n -> The length of the input array.
    # y -> Return statement that counts the number of operations performed.

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


def generate_different_cases(test_sizes):

    # Generates test cases of different sizes and types (best, worst, average).
    # test_sizes (list) -> A list of integers representing the sizes of test cases to generate.
    # dict -> Dictionary containing the test cases keyed by size and case type.

    # Initialize an empty dictionary to hold our test cases.
    test_cases = {}
    for size in test_sizes:

        # For each size, create a dictionary entry with sub-entries for best, worst, and average cases.
        test_cases[size] = {

            # Best case: All elements are 2.
            # Worst case: All elements are 1.
            # Average case: Random 0s, 1s, and 2s

            'best': [2] * size,
            # Best case: An array with all elements as '2'. This is considered the best case
            # for the algorithm because, according to its logic, the least number of operations
            # occur when the array elements are '2'. The loop that processes elements with value '2'
            # performs fewer operations compared to the loops for '0' and '1'.
            'worst': [1] * size,
            # Worst case: An array with all elements as '1'. This case is designated as the worst
            # because, as per the algorithm's structure, it forces the maximum number of operations.
            # When the element is '1', the algorithm enters into a triple-nested loop, which
            # causes a significantly higher count of operations, especially as the size of the array grows.
            'average': [random.randint(0, 2) for _ in range(size)]
            # Average case: An array with a random combination of 0s, 1s, and 2s. This represents a typical
            # scenario where the input is not skewed towards any particular case. It provides a more
            # realistic measure of the algorithm's average performance over a variety of inputs.
        }
    return test_cases


def measure_time(algorithm, cases):

    # Calculation and print statements for the execution time for each test case.
    # algorithm (function) -> algorithm function to be tested.
    # cases (dict) -> dictionary containing the test cases.

    for size, tests in cases.items():
        for case_type, test_data in tests.items():
            start_time = time.time()
            algorithm(test_data)
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(
                f"Case: {case_type.capitalize()} Size: {size} Elapsed Time (s): {elapsed_time:.6f}")


test_sizes = [1, 5, 10, 20, 30, 40, 50, 60,
              70, 80, 90, 100, 110, 120, 130, 140, 150]
test_cases = generate_different_cases(test_sizes)
measure_time(execute_algorithm, test_cases)
