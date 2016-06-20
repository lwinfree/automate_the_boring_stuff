# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 15:16:21 2016

@author: lillywinfree
"""

# ? matches 0 or 1 of the preceding group
# * matches 0 or more of the preceding group
# + matches 1 or more of the preceding group
# {n} matches exactly n of the preceding group
# {n, } matches n or more of the preceding group
# { ,m} matches 0 to m of the preceding group
# {n,m} matches at least n & at most m of the preceding group
# {n,m}? or *? or +? performs a nongreedy match of the preceding group
# ^spam means the string must begin with spam
# spam$ means the string must end with spam
# The . matches any character, except newline characters
# \d, \w, and \s match a digit, word, or space character, respectively
# \D, \W, \S match anything except a digit, word, or space, respectively
# [abc] matches any character between the brackets (a, b, or c)
# [^a,b,c] matches any charaacter that isn't between the brackets
# re.IGNORECASE (or re.I) = ignore case use as 2nd argument: re.compile('sjhdaj', re.I)
# re.DOTALL matches all characters including newline (see above)
 # re.VERBOSE ignores whitespace and comments (See above)
# can combine above 3 with | in 2nd argument (called bitwise)
