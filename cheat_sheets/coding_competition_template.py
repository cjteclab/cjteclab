"""Template for Coding Competitions.

This template can be use for coding competition problem sets.

Table of Content
    1. Docstring:
        - can be use to collect informations about the problem.
        - serves as notepad
        - using doctests to test the code
    2. Toughts about Input Handling:
        - different ways how to handle inputs
        - Tip: admit input handling as a part of the problem
    3. Main Function:
        - a main function to execute the code
    4. Test your code

Sources:
    - https://docs.python.org/3/library/doctest.html
    - https://www.geeksforgeeks.org/python-input-methods-competitive-programming/


"""

# 1. Docstring

"""Docstring:
1. Read the problem and make notes.

Notes:
    1.
    2.
    3.

2. Create examples and think about edge cases.
    - Use available examples from the problem set.

3. Writing Doctests:

1.

>>> main(???)
???

2.

>>> main(???)
???
"""

# 2. Input Handling

"""Thoughts about Input Handling:
Example 1:
    Input:
        5
        1 2 3 4 5

    Handling: normal method using raw_input()
        # for the first line with one int:
        single_value = int(input())
        # for the second line with multiple ints:
        multi_values = [int(element) for element in input().split()]

    Handling: a bit faster method using inbuilt stdin, stdout
        from sys import stdtin, stdout
        # for the first line with one int:
        single_value = stdin.readline()
        # for the second line with multiple ints:
        mutli_values = [int(element) for element in stdin.readline().split()]

Example 2: particular integer given in a single line
    Input: 5 7 19 20

    Handling: get ints with seperate variables to reference them
        # get the ints with:
        def get_ints(): return map(int, sys.stdin.readline().strip().split())
        a, b, c, d = get_ints()

    Handling: get all ints as list
        #  get the ints with:
        def get_ints(): return list(map(int,
        sys.stdin.readline().strip().split()))
        list_of_ints = get_ints()

More examples:
    - https://levelup.gitconnected.com/basic-input-and-output-techniques-used-in-competitive-programming-5be5622b4525
    - https://www.geeksforgeeks.org/python-input-methods-competitive-programming/

    or just search on google

"""

# 3. Main Function


def main():
    pass
    # return result


if __name__ == '__main__':
    import doctest
    doctest.testmode()

# 4. Test your code

"""Test your code:
To test your code and get a detailed log of the test execute:
    --> python file.py -v
"""
