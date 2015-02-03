#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2015
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

def collatz_read (s) :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    # <your code>
    maxcycle = 0 
    for k in range(i, j + 1): # range() needs to be invoked with j + 1 as end index since range() excludes the end index
        cycleLength = 0
        l = k # temporary value equal to k
        """
        While k is greater than 1

        """
        while (l > 1):
            cycleLength += 1 # increment cycle length
            if (l % 2 == 0): # If l is even
                l /= 2       # divide l by 2
            else:            # If l is odd
                l *= 3 # Multiply l by 3
                l += 1 # Add 1 to l
        if cycleLength > maxcycle:
            maxcycle = cycleLength
    return maxcycle

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    for s in r :
        i, j = collatz_read(s)
        v    = collatz_eval(i, j)
        collatz_print(w, i, j, v)
