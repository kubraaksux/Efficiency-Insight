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


def generate_different_cases(test_sizes,q_number):




    # Generates test cases of different sizes and types (best, worst, average).
    # test_sizes (list) -> A list of integers representing the sizes of test cases to generate.
    # dict -> Dictionary containing the test cases keyed by size and case type.

    # Initialize an empty dictionary to hold our test cases.
    test_cases = {}


    #Decide best or worst case according to the question
    if q_number==1:
        #doesn't matter for this
        best=2
        worst=0

    elif q_number==2:
        best=2
        worst=1

    elif q_number==3:
        best=1
        worst=0



    for size in test_sizes:

        # For each size, create a dictionary entry with sub-entries for best, worst, and average cases.


        # 'Average' case: A random mix of '0's, '1's, and '2's to simulate a typical input array.
        average_list=[]
        for i in range(10):
            average_list.append([random.randint(0, 2) for _ in range(size)])


        test_cases[size] = {

            # Best case: All elements are 2.
            # Worst case: All elements are 1.
            # Average case: Random 0s, 1s, and 2s

            'best': [best] * size,
            # 'Best' case: All '2's - Requires fewer operations within the algorithm's structure,
            # as it avoids the more complex nested loops that are activated by '0's and '1's.
            'worst': [worst] * size,
            # 'Worst' case: All '1's - Engages the most complex part of the algorithm with the
            # deepest nested loops, resulting in the highest number of operations.

            
            'average': average_list
            
        }
    return test_cases


def measure_time(algorithm, cases):

    # Calculation and print statements for the execution time for each test case.
    # algorithm (function) -> algorithm function to be tested.
    # cases (dict) -> dictionary containing the test cases.

    for size, tests in cases.items():
        for case_type, test_data in tests.items():
            
            if case_type=="average":
                total_time=0
                
                for eachList in test_data:
                    start_time = time.time()
                    algorithm(eachList)
                    end_time = time.time()
                    elapsed_time = end_time - start_time
                    total_time+=elapsed_time
                    print(
                    f"Case: {case_type.capitalize()} Size: {size} Elapsed Time (s): {elapsed_time:.6f}")
                average_time=total_time/10.
                print(
                    f"Case: {case_type.capitalize()} Average Elapsed Time (s): {average_time:.6f}")

            else:
                start_time = time.time()
                algorithm(test_data)
                end_time = time.time()
                elapsed_time = end_time - start_time
                print(
                    f"Case: {case_type.capitalize()} Size: {size} Elapsed Time (s): {elapsed_time:.6f}")


test_sizes = [1, 5, 10, 20, 30, 40, 50, 60,
              70, 80, 90, 100, 110, 120, 130, 140, 150]

print("QUESTION 1")
test_cases = generate_different_cases(test_sizes,1)
measure_time(execute_algorithm, test_cases)
print("QUESTION 2")
test_cases = generate_different_cases(test_sizes,2)
measure_time(execute_algorithm, test_cases)
print("QUESTION 3")
test_cases = generate_different_cases(test_sizes,3)
measure_time(execute_algorithm, test_cases)
#test_cases = generate_different_cases(test_sizes,4)
#measure_time(execute_algorithm, test_cases)
