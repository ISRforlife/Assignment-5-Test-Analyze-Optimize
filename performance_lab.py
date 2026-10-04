# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    # Return None if the list is empty
    if not numbers:
        return None

    counts = {}

    # Count how many times each number appears
    for number in numbers:
        if number in counts:
            counts[number] += 1
        else:
            counts[number] = 1

    most_common = numbers[0]

    # Find the number with the highest count
    for number in counts:
        if counts[number] > counts[most_common]:
            most_common = number

    return most_common


"""
Time and Space Analysis for problem 1:
- Best-case: O(n) because I still need to go through the list and count each value.
- Worst-case: O(n) because every number has to be checked.
- Average-case: O(n) because dictionary lookups are usually O(1).
- Space complexity: O(n) because the dictionary may store every unique number.
- Why this approach? I used a dictionary because it lets me connect each number
  to the number of times it appears.
- Could it be optimized? The time is already efficient. Using less memory would
  probably require checking values more than once, which would make it slower.
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    seen = set()
    result = []

    for number in nums:
        if number not in seen:
            seen.add(number)
            result.append(number)

    return result


"""
Time and Space Analysis for problem 2:
- Best-case: O(n) because every value still needs to be checked.
- Worst-case: O(n) because the list is only scanned one time.
- Average-case: O(n) because checking and adding values to a set is usually O(1).
- Space complexity: O(n) because both the set and result list can grow with the input.
- Why this approach? I used a set to quickly check whether I had already seen a
  value and a list to keep the original order.
- Could it be optimized? This is already fast. I could avoid using a set, but then
  searching for duplicates in the result list would make the runtime slower.
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs(nums, target):
    seen = set()
    pairs = []

    for number in nums:
        needed = target - number

        if needed in seen:
            pairs.append((needed, number))

        seen.add(number)

    return pairs


"""
Time and Space Analysis for problem 3:
- Best-case: O(n) because the list is checked once.
- Worst-case: O(n) because set lookups are usually O(1).
- Average-case: O(n) because every number is processed once.
- Space complexity: O(n) because the set can store all of the input values.
- Why this approach? I used a set because it lets me quickly check if the number
  needed to reach the target has already appeared.
- Could it be optimized? A nested loop would use less extra memory, but it would
  take O(n^2) time. I chose faster performance at the cost of extra memory.
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n):
    capacity = 1
    size = 0
    items = [None] * capacity

    for value in range(n):

        # Resize when the list reaches its current capacity
        if size == capacity:
            new_capacity = capacity * 2
            print(f"Resizing from {capacity} to {new_capacity}")

            new_items = [None] * new_capacity

            # Copy all old values into the bigger list
            for i in range(size):
                new_items[i] = items[i]

            items = new_items
            capacity = new_capacity

        items[size] = value
        size += 1

    return items[:size]


"""
Time and Space Analysis for problem 4:
- When do resizes happen? A resize happens whenever the number of stored items
  reaches the current capacity.
- What is the worst-case for a single append? O(n) because all existing values
  may need to be copied into a new larger list.
- What is the amortized time per append overall? O(1), because most appends do
  not require resizing.
- Space complexity: O(n) because the list grows based on the number of items.
- Why does doubling reduce the cost overall? Doubling means that resizing happens
  less often as the list grows, so the expensive copy operations are spread out
  across many normal appends.
"""


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]


# Original version before optimization
def running_total_original(nums):
    result = []

    # Recalculate the total from the beginning each time
    for i in range(len(nums)):
        total = 0

        for j in range(i + 1):
            total += nums[j]

        result.append(total)

    return result


# Optimized version
def running_total(nums):
    result = []
    total = 0

    # Keep one running total instead of starting over
    for number in nums:
        total += number
        result.append(total)

    return result


"""
Time and Space Analysis for problem 5:

Original solution:
- Best-case: O(n^2) because the nested loops repeatedly add earlier values.
- Worst-case: O(n^2) because each position recalculates the total from the beginning.
- Average-case: O(n^2).
- Space complexity: O(n) because a new result list is created.

Optimized solution:
- Best-case: O(n) because each number is processed once.
- Worst-case: O(n) because the function only goes through the list once.
- Average-case: O(n).
- Space complexity: O(n) because a new result list is still created.

- Why this approach? My original version recalculated the sum from the beginning
  for every position. I optimized it by keeping a running total and adding each
  new value one time.
- Could it be optimized more? The extra space could be reduced to O(1) by changing
  the original input list, but that would modify the input.
- Trade-offs: The optimized version is much faster as the input gets larger, while
  still using O(n) space for the result list.
"""


# --------------------------------------------------
# Tests
# --------------------------------------------------

if __name__ == "__main__":

    print("Problem 1 Tests")
    print(most_frequent([1, 3, 2, 3, 4, 1, 3]))  # 3
    print(most_frequent([5, 5, 2, 2, 5]))        # 5
    print(most_frequent([7]))                     # 7
    print(most_frequent([]))                      # None

    print("\nProblem 2 Tests")
    print(remove_duplicates([4, 5, 4, 6, 5, 7]))  # [4, 5, 6, 7]
    print(remove_duplicates([1, 1, 1]))            # [1]
    print(remove_duplicates([]))                   # []
    print(remove_duplicates([1, 2, 3]))            # [1, 2, 3]

    print("\nProblem 3 Tests")
    print(find_pairs([1, 2, 3, 4], 5))             # [(2, 3), (1, 4)]
    print(find_pairs([1, 2, 3], 10))               # []
    print(find_pairs([], 5))                       # []
    print(find_pairs([-2, -1, 1, 2], 0))           # [(-1, 1), (-2, 2)]

    print("\nProblem 4 Tests")
    print(add_n_items(6))                           # [0, 1, 2, 3, 4, 5]
    print(add_n_items(0))                           # []
    print(add_n_items(1))                           # [0]

    print("\nProblem 5 Tests")
    print(running_total([1, 2, 3, 4]))             # [1, 3, 6, 10]
    print(running_total([]))                       # []
    print(running_total([5]))                      # [5]
    print(running_total([-1, 2, -3, 4]))           # [-1, 1, -2, 2]

    print("\nProblem 5 Original vs Optimized")
    print(running_total_original([1, 2, 3, 4]))    # [1, 3, 6, 10]
    print(running_total([1, 2, 3, 4]))             # [1, 3, 6, 10]
