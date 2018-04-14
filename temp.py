
import sys

n = int(input ())  # No. of test cases

for _ in range (n):

    # Each test case

    A = int (input ())
    if A < 9:
        A = 9

    if A % 3 != 0:
        A += (3 - (A % 3))

    num_targets = int (A / 3)

    i = 2
    j = 2
    curr_dug = set ()
    end_test_case = False  # Flag variable for flow control
    while j != num_targets + 2:
        print ("{} {}".format (i, j))
        sys.stdout.flush ()
        hole_at = tuple ([int (i) for i in input ().strip ().split ()])
        if hole_at == (-1, -1):
            exit ()
        if hole_at == (0, 0):
            end_test_case = True
            break

        curr_dug.add (hole_at)
        if len (curr_dug) == 9:
            j += 1
            curr_dug = set ()

    if end_test_case:
        continue