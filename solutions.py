# solutions.py
from collections import Counter
def mastermind(guess: str, solution: str) -> tuple[int, int]:
    """Return (correct_position, correct_color) for a Mastermind guess."""
    # TODO: Implement Mastermind logic
    correct_position = 0
    solution_remaining = []
    guess_remaining= []
    for g, s in zip(guess, solution):
        if g == s:
            correct_position += 1
        else:
            solution_remaining.append(s)
            guess_remaining.append(g)
    solution_counter = Counter(solution_remaining)
    guess_counter = Counter(guess_remaining)
    correct_color = 0
    for color in guess_counter:
        correct_color += min(guess_counter[color], solution_counter.get(color, 0))
    
    return (correct_position, correct_color)
print(mastermind("RGBY", "RGBY")) 
print(mastermind("RGBY", "YRGB"))  
print(mastermind("RGBY", "RRGG"))  

def to_roman(num: int) -> str:
    """Convert integer to Roman numeral."""
    # TODO: Implement Roman numeral conversion
    roman_numerals={
        1:'I',
        4:'IV',
        5:'V',
        9:'IX',
        10:'X',
        40:'XL',
        50:'L',
        90:'XC',
        100:'C',
        400:'CD',
        500:'D',
        900:'CM',
        1000:'M',
    }
    result='' 
    for value in sorted(roman_numerals.keys(), reverse= True):
        while num >= value: 
            result += roman_numerals[value] 
            num -= value 
    return result 
print(to_roman(9))
print(to_roman(3))
print(to_roman(2023))
    

def binary_search(arr: list[int], target: int) -> int:
    """Return index of target in sorted array, or -1 if not found."""
    # TODO: Implement binary search
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
arr = [1, 3, 5, 7, 9, 11, 13]
target_1 = 7
print(binary_search(arr, target_1))

def fibonacci(n: int) -> int:
    """Return nth Fibonacci number (0-based index)."""
    # TODO: Implement Fibonacci calculation
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+ fibonacci(n-2)
print(fibonacci(10))

def is_palindrome(s: str) -> bool:
    """Check if string is a palindrome (case-insensitive, ignoring non-alphanum)."""
    # TODO: Implement palindrome checker
    s = ''.join(filter(str.isalnum, s)).lower()  
    return s == s[::-1]
print(is_palindrome("A man, a plan, a canal: Panama"))
print(is_palindrome("race a car"))
print(is_palindrome(""))


def merge_sorted_arrays(arr1: list[int], arr2: list[int]) -> list[int]:
    """Merge two sorted arrays into one sorted array."""
    # TODO: Implement array merge
    return sorted(arr1 + arr2)
print(merge_sorted_arrays([1, 3, 5], [2, 4, 6]))
print(merge_sorted_arrays([], [1, 2]), [1, 2])
print(merge_sorted_arrays([1], []), [1])

def validate_password(password: str) -> bool:
    """Validate password: 8+ chars, 1 upper, 1 lower, 1 digit, 1 special."""
    # TODO: Implement password validation
    if len(password) < 8:
        return False  
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    return all([has_upper, has_lower, has_digit, has_special])
print(validate_password("Kcardi@1")) 
print(validate_password("Kcardi@1A")) 
print(validate_password("Kcardi1"))

def cash_register(price: float, cash: float) -> dict[str, int]:
    """Calculate change in ZAR using R50, R20, R10, R5, R2, R1, 50c, 20c, 10c."""
    # TODO: Implement cash register logic for South African currency
    denominations = [50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1]
    change = round(cash - price, 2)
    result = {}
    for denom in denominations:
        count = int(change // denom)
        if count > 0:
            if denom >= 1:
                result[f"R{int(denom)}"] = count
            else:
                result[f"{int(denom * 100)}C"] = count
            change -= count * denom
    return result
price = 68.30
cash = 100.00
print(cash_register(price, cash))

def are_anagrams(str1: str, str2: str) -> bool:
    """Check if two strings are anagrams."""
    # TODO: Implement anagram checker
    if sorted(str1)==sorted(str2):
        return True
    else:
        return False
print(are_anagrams("Hello","ellho"))

def longest_common_prefix(strings: list[str]) -> str:
    """Find longest common prefix among list of strings."""
    # TODO: Implement prefix finder
    if not strings:
        return ""
    prefix = ""
    shortest = min(strings, key=len)
    for i in range(len(shortest)):
        char = shortest[i]
        for s in strings:
            if s[i] != char:
                return prefix
        prefix += char
    return prefix
print(longest_common_prefix(["flower", "flow", "flight"]))
print(longest_common_prefix(["dog", "racecar", "car"]))
print(longest_common_prefix([""]))                       

def evaluate_expression(expr: str) -> float:
    """Evaluate a simple arithmetic expression (e.g., '2 + 3 * 4')."""
    # TODO: Implement expression evaluator
    try:
        result = eval(expr)
        return float(result)
    except Exception as e:
        raise ValueError(f"Invalid expression: {str(e)}")
print(evaluate_expression("2 + 3"))
print(evaluate_expression("2 + 3 * 4"))
print(evaluate_expression("10 - 2 / 2"))

def find_duplicates(arr: list[int]) -> list[int]:
    """Find all duplicate numbers in an array."""
    # TODO: Implement duplicate finder
    from collections import Counter
    counts = Counter(arr)
    return [num for num, count in counts.items() if count > 1]
# print(find_duplicates("hello"))
print(sorted(find_duplicates([1, 2, 3, 2, 4, 1])))
print(find_duplicates([1, 2, 3]))
print(find_duplicates([]))

def print_pascal_triangle(n: int) -> str:
    """Generate Pascal's triangle as a string with n rows."""
    # TODO: Implement Pascal's triangle printer
    triangle = []
    for i in range(n):
        row = [1]
        for j in range(1, i + 1):
            row.append(row[j-1] * (i - j + 1) // j)
        triangle.append(' ' * (n - i - 1) + ' '.join(map(str, row)))
    return '\n'.join(triangle)
print(print_pascal_triangle(5))

def print_diamond_pattern(n: int) -> str:
    """Generate a diamond pattern as a string with n rows in upper half."""
    # TODO: Implement diamond pattern printer
    diamond = []
    for i in range(n):
        row = ' ' * (n - i - 1) + '*' * (2 * i + 1)
        diamond.append(row)
    for i in range(n - 2, -1, -1):
        row = ' ' * (n - i - 1) + '*' * (2 * i + 1)
        diamond.append(row)
    return '\n'.join(diamond)
print(print_diamond_pattern(3))

def factorial(n: int) -> int:
    """Calculate factorial of n."""
    # TODO: Implement factorial calculation
    if n ==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))
 
 