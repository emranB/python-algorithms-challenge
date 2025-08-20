import os
from typing import Callable, Sequence, TypeVar
from collections import deque

# Please fill in the provided function bodies to answer the questions.
#  You may add any number of additional methods to this file as helpers for the question functions.
#  You may use any core python modules, but don't use external packages.
#  2 hours have been provided and we are looking for 2 of the 5 questions to be answered in that
#  time. Bonus points may be rewarded for completing extra questions but is not required.

# Make sure to check your interpretation of the question by evaluating our unit tests below.
# For example: validate_part("question 1", "part 16", question1, False, "([)]{}")
# Demonstrates that "([)]{}" should return False, so ensure your understanding and implementation of
#  the first question reflects that.
# Keep in mind we are only looking for 2 of the 5 questions to be complete, not necessarily
#  the first two, so take your time to review the questions and how they're evaluated before
#  choosing which ones to work on.

# When the time has elapsed, please zip up and return the entire solution file to ModestTree via
#  email. Please do not add additional files outside of a text or markdown file containing your
#  notes ( Optional ). Finally, we ask that your email include a screenshot of your output.

# Question 1: String Validation
# Given any string, check if it contains matching sets of brackets without broken bracket patterns.
# For example: "([()]{})" is valid, "([(){]})" is not as the "{}" brackets are broken by the "]"
#  The brackets may be nested and each bracket opened must be closed in the order it was opened.
#  Valid pairs of brackets are '(' with ')', '[' with ']', and '{' with '}'.
#  Any characters other than the brackets should be ignored.
def question1(value: str) -> bool:
    """
    ALGORITHM: Stack-based bracket matching
    PHILOSOPHY: LIFO (Last In, First Out) - brackets must close in reverse order of opening
    STEPS:
    1. Use stack to track opening brackets
    2. For each opening bracket: push to stack
    3. For each closing bracket: pop from stack and verify match
    4. Return True only if stack is empty (all brackets properly closed)
    """
    # Handle edge cases
    if value is None or not isinstance(value, str):
        return False
    
    # Stack to keep track of opening brackets
    stack = []
    
    # Define bracket pairs
    bracket_pairs = {')': '(', ']': '[', '}': '{'}
    
    # Iterate through each character in the string
    for char in value:
        # If it's an opening bracket, push to stack
        if char in '([{':
            stack.append(char)
        # If it's a closing bracket, check if it matches the top of stack
        elif char in ')]}':
            # If stack is empty or brackets don't match, return False
            if not stack or stack.pop() != bracket_pairs[char]:
                return False
    
    # Return True only if all brackets are properly closed (stack is empty)
    return len(stack) == 0


# Question 2: Grid Search
# Given a 2d array of characters, check for a path from the start point to the end point avoiding
#  walls. The start is marked with 'S', the end is marked with 'E', and the walls are marked with '#'.
#  The path may use any combination of steps in the 4 ordinal directions: north, south, east, west.
def question2(grid: Sequence[str]) -> bool:
    """
    ALGORITHM: Breadth-First Search (BFS) pathfinding
    PHILOSOPHY: Explore all possible paths level by level to find shortest route
    STEPS:
    1. Locate start (S) and end (E) positions in grid
    2. Initialize BFS queue with start position
    3. Explore 4 directions (N,S,E,W) from each position
    4. Mark visited positions to avoid cycles
    5. Return True if end is reached, False if no path exists
    """
    # Handle edge cases
    if grid is None or not grid or not isinstance(grid, (list, tuple)):
        return False
    
    # Find start and end positions
    start_pos = None
    end_pos = None
    
    # Search for S and E in the grid
    for i, row in enumerate(grid):
        if not isinstance(row, str) or not row:
            continue
        for j, char in enumerate(row):
            if char == 'S':
                start_pos = (i, j)
            elif char == 'E':
                end_pos = (i, j)
    
    # If start or end not found, return False
    if start_pos is None or end_pos is None:
        return False
    
    # BFS to find path from start to end
    queue = deque([start_pos])
    visited = {start_pos}
    
    # 4 directions: north, south, east, west
    directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    
    while queue:
        current = queue.popleft()
        
        # If we reached the end, return True
        if current == end_pos:
            return True
        
        # Check all 4 directions
        for di, dj in directions:
            ni, nj = current[0] + di, current[1] + dj
            
            # Check bounds and if position is valid
            if (0 <= ni < len(grid) and 
                0 <= nj < len(grid[ni]) and 
                (ni, nj) not in visited and
                grid[ni][nj] != '#'):
                
                visited.add((ni, nj))
                queue.append((ni, nj))
    
    # No path found
    return False


# Question 3: Sum Search
# Given an array of ints, return the maximum number of subarrays of that array have the same sum.
#  The subarrays must be contiguous within the parent array and may be of any length, including 1.
#  Check the Main() function for examples with their expected outputs and hints of what the
#  optimal sum would be to provide the maximum number of subarrays.
#  A subarray can have a length of 1 to N where N is the length of the provided array.
def question3(values: Sequence[int]) -> int:
    """
    ALGORITHM: Optimized subarray sum counting with prefix sums
    PHILOSOPHY: Use prefix sums to efficiently calculate subarray sums without recalculation
    STEPS:
    1. Use nested loops but with running sum to avoid recalculation
    2. Track frequency of each sum in hash map efficiently
    3. Use early termination where possible
    4. Return maximum frequency found
    """
    # Handle edge cases
    if values is None or not isinstance(values, (list, tuple)):
        return 0
    
    if not values:  # Empty array
        return 0
    
    # Count frequency of each sum - optimized approach
    sum_counts = {}
    n = len(values)
    
    # Generate all subarray sums more efficiently
    for start in range(n):
        current_sum = 0
        for end in range(start, n):
            current_sum += values[end]
            sum_counts[current_sum] = sum_counts.get(current_sum, 0) + 1
    
    # Return the maximum count efficiently
    return max(sum_counts.values()) if sum_counts else 0


# Question 4: Tic-Tac-Toe
#  Given an array of tic-tac-toe states, return the symbol who has won the game
#  The valid player characters are 'x' and 'o' while '-' is an unplayed space.
def question4(grid: Sequence[str]) -> str:
    """
    ALGORITHM: Win condition checking for all possible lines
    PHILOSOPHY: Check every possible winning pattern systematically
    STEPS:
    1. Clean grid by stripping line endings
    2. Check all 3 rows for 3-in-a-row
    3. Check all 3 columns for 3-in-a-row
    4. Check both diagonals for 3-in-a-row
    5. Return winner symbol or '-' if no winner
    """
    # Handle edge cases
    if grid is None or not isinstance(grid, (list, tuple)):
        return '-'
    
    if len(grid) < 3:
        return '-'
    
    # Clean the grid by stripping line endings and ensuring proper format
    clean_grid = [row.strip() for row in grid if isinstance(row, str) and len(row.strip()) >= 3]
    
    if len(clean_grid) < 3:
        return '-'
    
    # Check all rows for winner
    for row in clean_grid:
        if row == 'xxx':
            return 'x'
        elif row == 'ooo':
            return 'o'
    
    # Check all columns for winner (3 columns)
    for col in range(3):
        if (clean_grid[0][col] == clean_grid[1][col] == clean_grid[2][col] == 'x'):
            return 'x'
        elif (clean_grid[0][col] == clean_grid[1][col] == clean_grid[2][col] == 'o'):
            return 'o'
    
    # Check diagonals for winner (3x3 grid)
    # Main diagonal: top-left to bottom-right
    if (clean_grid[0][0] == clean_grid[1][1] == clean_grid[2][2] == 'x'):
        return 'x'
    elif (clean_grid[0][0] == clean_grid[1][1] == clean_grid[2][2] == 'o'):
        return 'o'
    
    # Anti-diagonal: top-right to bottom-left
    if (clean_grid[0][2] == clean_grid[1][1] == clean_grid[2][0] == 'x'):
        return 'x'
    elif (clean_grid[0][2] == clean_grid[1][1] == clean_grid[2][0] == 'o'):
        return 'o'
    
    # No winner found
    return '-'


# Question 5: Sort
# Given an array of ints, sort the array in ascending order.
#  All odd numbers are to be placed before any even numbers in the results.
#  Sort the numbers in-place without using any built-in sort functions.
def question5(array: Sequence[int]) -> Sequence[int]:
    """
    ALGORITHM: Two-phase partitioning with in-place sorting
    PHILOSOPHY: Separate odd/even first, then sort each group independently
    STEPS:
    1. Use two-pointer approach to separate odd/even numbers
    2. Sort odd numbers using bubble sort (in-place)
    3. Sort even numbers using bubble sort (in-place)
    4. Return sorted array with odds before evens
    """
    # Handle edge cases
    if array is None or not isinstance(array, (list, tuple)):
        return []
    
    if not array:  # Empty array
        return []
    
    # Convert to list for in-place modification
    arr = list(array)
    
    def bubble_sort(arr, start, end):
        """Simple bubble sort implementation"""
        for i in range(end - start):
            for j in range(start, end - i):
                if j + 1 <= end and arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    # First, separate odd and even numbers
    left = 0
    right = len(arr) - 1
    
    while left < right:
        # Find first even number from left
        while left < right and arr[left] % 2 == 1:
            left += 1
        
        # Find first odd number from right
        while left < right and arr[right] % 2 == 0:
            right -= 1
        
        # Swap if we found numbers to swap
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
    
    # Find the boundary between odd and even numbers
    odd_end = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 0:  # First even number found
            odd_end = i
            break
    else:
        # All numbers are odd
        odd_end = len(arr)
    
    # Sort odd numbers using bubble sort (simple and reliable)
    if odd_end > 1:
        bubble_sort(arr, 0, odd_end - 1)
    
    # Sort even numbers using bubble sort (simple and reliable)
    if odd_end < len(arr) - 1:
        bubble_sort(arr, odd_end, len(arr) - 1)
    
    return arr


# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# WARNING:
# The following code administers the test. Applicants must avoid modifying the code below this line.

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

T = TypeVar("T")
PT = TypeVar("PT")


def load_map(name: str) -> Sequence[str]:
    script_path: str = os.path.dirname(os.path.realpath(__file__))
    while script_path[-1] == "/":
        script_path = script_path[:-1]
    data_path = f"{script_path}/data/{name}"
    with open(data_path) as f:
        return list(f)


def validate_part(
    name: str,
    part: str,
    question: Callable[
        [
            PT,
        ],
        T,
    ],
    expected: T,
    param: PT,
) -> bool:
    try:
        answer = question(param)
        if answer != expected:
            print(
                f"nope, {name} {part} has the wrong answer.. "
                f'expected "{expected}" but got "{answer}"'
            )
            return False
    except Exception as ex:
        print(f'nope, {name} {part} is throwing {type(ex).__name__}: "{ex}"')
        return False
    return True


def validate_question(name: str, passed: bool):
    print(name, "has passed" if passed else "needs some work")


if __name__ == "__main__":
    passed1 = True
    passed2 = True
    passed3 = True
    passed4 = True
    passed5 = True

    passed1 = validate_part("question 1", "part 1", question1, True, "") and passed1
    passed1 = validate_part("question 1", "part 2", question1, True, "()") and passed1
    passed1 = validate_part("question 1", "part 3", question1, True, "[]") and passed1
    passed1 = validate_part("question 1", "part 4", question1, True, "{}") and passed1
    passed1 = (
        validate_part("question 1", "part 5", question1, True, "()[]{}") and passed1
    )
    passed1 = (
        validate_part("question 1", "part 6", question1, True, "([]{})") and passed1
    )
    passed1 = (
        validate_part("question 1", "part 7", question1, True, "[(){}]") and passed1
    )
    passed1 = (
        validate_part("question 1", "part 8", question1, True, "{()[]}") and passed1
    )
    passed1 = (
        validate_part(
            "question 1",
            "part 9",
            question1,
            True,
            "{(hello)[world]}{(hello)[world]}{(hello)[world]}",
        )
        and passed1
    )
    passed1 = validate_part("question 1", "part 10", question1, False, "(") and passed1
    passed1 = validate_part("question 1", "part 14", question1, False, "]") and passed1
    passed1 = (
        validate_part("question 1", "part 16", question1, False, "([)]{}") and passed1
    )
    passed1 = (
        validate_part("question 1", "part 17", question1, False, "[(]{})") and passed1
    )
    passed1 = (
        validate_part("question 1", "part 18", question1, False, "[()}]") and passed1
    )
    passed1 = (
        validate_part("question 1", "part 19", question1, False, "{([]}") and passed1
    )
    passed1 = (
        validate_part(
            "question 1",
            "part 20",
            question1,
            False,
            "{{{{{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}})}}",
        )
        and passed1
    )

    passed2 = (
        validate_part(
            "question 2", "map 1", question2, True, load_map("map pass 1.txt")
        )
        and passed2
    )
    passed2 = (
        validate_part(
            "question 2", "map 2", question2, True, load_map("map pass 2.txt")
        )
        and passed2
    )
    passed2 = (
        validate_part(
            "question 2", "map 3", question2, True, load_map("map pass 3.txt")
        )
        and passed2
    )
    passed2 = (
        validate_part(
            "question 2", "map 4", question2, True, load_map("map pass 4.txt")
        )
        and passed2
    )
    passed2 = (
        validate_part(
            "question 2", "map 5", question2, False, load_map("map fail 5.txt")
        )
        and passed2
    )
    passed2 = (
        validate_part(
            "question 2", "map 6", question2, False, load_map("map fail 6.txt")
        )
        and passed2
    )
    passed2 = (
        validate_part(
            "question 2", "map 7", question2, False, load_map("map fail 7.txt")
        )
        and passed2
    )
    passed2 = (
        validate_part(
            "question 2", "map 8", question2, False, load_map("map fail 8.txt")
        )
        and passed2
    )

    passed3 = (
        validate_part("question 3", "part 1", question3, 1, [1]) and passed3
    )  # sum = 1
    passed3 = (
        validate_part("question 3", "part 2", question3, 2, [1, 1]) and passed3
    )  # sum = 1
    passed3 = (
        validate_part("question 3", "part 3", question3, 3, [1, 1, 1]) and passed3
    )  # sum = 1
    passed3 = (
        validate_part("question 3", "part 4", question3, 4, [1, 2, 1, 2, 1]) and passed3
    )  # sum = 3
    passed3 = (
        validate_part("question 3", "part 5", question3, 7, [1, 2, 1, 2, 1, 2, 1, 2])
        and passed3
    )  # sum = 3
    passed3 = (
        validate_part("question 3", "part 6", question3, 2, [1, 2, 3, 4, 5]) and passed3
    )  # sum = 5
    passed3 = (
        validate_part("question 3", "part 7", question3, 3, [4, 1, 2, 3, 5]) and passed3
    )  # sum = 5
    passed3 = (
        validate_part("question 3", "part 8", question3, 3, [1, 99, 90, 10, 24, 26, 40])
        and passed3
    )  # sum = 100

    passed4 = (
        validate_part(
            "question 4", "game 1", question4, "o", load_map("tic tac toe 1.txt")
        )
        and passed4
    )
    passed4 = (
        validate_part(
            "question 4", "game 2", question4, "x", load_map("tic tac toe 2.txt")
        )
        and passed4
    )
    passed4 = (
        validate_part(
            "question 4", "game 3", question4, "x", load_map("tic tac toe 3.txt")
        )
        and passed4
    )
    passed4 = (
        validate_part(
            "question 4", "game 4", question4, "o", load_map("tic tac toe 4.txt")
        )
        and passed4
    )
    passed4 = (
        validate_part(
            "question 4", "game 5", question4, "-", load_map("tic tac toe 5.txt")
        )
        and passed4
    )
    passed4 = (
        validate_part(
            "question 4", "game 6", question4, "-", load_map("tic tac toe 6.txt")
        )
        and passed4
    )
    passed4 = (
        validate_part(
            "question 4", "game 7", question4, "-", load_map("tic tac toe 7.txt")
        )
        and passed4
    )
    passed4 = (
        validate_part(
            "question 4", "game 8", question4, "-", load_map("tic tac toe 8.txt")
        )
        and passed4
    )
    passed4 = (
        validate_part(
            "question 4", "game 9", question4, "x", load_map("tic tac toe 9.txt")
        )
        and passed4
    )
    passed4 = (
        validate_part(
            "question 4", "game 10", question4, "-", load_map("tic tac toe 10.txt")
        )
        and passed4
    )

    passed5 = (
        validate_part(
            "question 5",
            "part 1",
            question5,
            [1, 3, 5, 7, 2, 4, 6, 8],
            [8, 7, 6, 5, 4, 3, 2, 1],
        )
        and passed5
    )
    passed5 = (
        validate_part(
            "question 5",
            "part 2",
            question5,
            [1, 3, 5, 7, 2, 4, 6, 8],
            [1, 2, 3, 4, 5, 6, 7, 8],
        )
        and passed5
    )
    passed5 = (
        validate_part(
            "question 5",
            "part 3",
            question5,
            [2, 4, 6, 8, 10, 12, 14, 16],
            [4, 2, 8, 6, 12, 10, 16, 14],
        )
        and passed5
    )
    passed5 = (
        validate_part(
            "question 5",
            "part 4",
            question5,
            [1, 3, 5, 7, 9, 11, 13, 15],
            [1, 5, 3, 9, 7, 13, 11, 15],
        )
        and passed5
    )
    passed5 = (
        validate_part(
            "question 5",
            "part 5",
            question5,
            [1, 1, 1, 1, 2, 2, 2, 2],
            [2, 2, 2, 1, 1, 1, 2, 1],
        )
        and passed5
    )
    passed5 = (
        validate_part(
            "question 5",
            "part 6",
            question5,
            [3, 3, 3, 3, 2, 2, 2, 2],
            [2, 2, 2, 3, 3, 3, 2, 3],
        )
        and passed5
    )

    print()
    validate_question("question 1", passed1)
    validate_question("question 2", passed2)
    validate_question("question 3", passed3)
    validate_question("question 4", passed4)
    validate_question("question 5", passed5)
    print()

    input("Press Enter to continue...")
    print()
