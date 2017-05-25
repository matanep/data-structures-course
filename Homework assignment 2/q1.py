
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      reutb
#
# Created:     23/05/2017
# Copyright:   (c) reutb 2017
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import numpy as np

#one way:
# def min_coins(k):
#     """
#     Solve the knapsack problem by finding the most valuable
#     subsequence of `items` subject that weighs no more than
#     `maxweight`.
#
#     `items` is a sequence of pairs `(value, weight)`, where `value` is
#     a number and `weight` is a non-negative integer.
#
#     `maxweight` is a non-negative integer.
#
#     Return a pair whose first element is the sum of values in the most
#     valuable subsequence, and whose second element is the subsequence.
#
#     # >>> items = [(4, 12), (2, 1), (6, 4), (1, 1), (2, 2)]
#     # >>> knapsack(items, 15)
#     (11, [(2, 1), (6, 4), (1, 1), (2, 2)])
#     """
#
#
#
#     global MC
#     MC =[-1 for m in range (k+1)]
#     print MC
#     return bestvalue(k,MC)
#
# def bestvalue(i,MC):
#     # Return the value of the most valuable subsequence of the first i
#     # elements in items whose weights sum to no more than j.
#     #@memoized
#     if i <0:
#         return np.inf
#     if i==0:
#         return 0
#     else:
#         if MC[i]==-1:
#             MC[i]= min(bestvalue(i - 1,MC)+1,
#                        bestvalue(i - 10, MC) + 1,
#                        bestvalue(i - 25, MC) + 1,
#                        bestvalue(i - 50, MC) + 1)
#             print MC
#         return MC[i]
#
#
# k=30
# min_coins=min_coins(k)
# print MC
# print min_coins


#and the other:
def min_coins(k):
    """
    Solve the knapsack problem by finding the most valuable
    subsequence of `items` subject that weighs no more than
    `maxweight`.

    `items` is a sequence of pairs `(value, weight)`, where `value` is
    a number and `weight` is a non-negative integer.

    `maxweight` is a non-negative integer.

    Return a pair whose first element is the sum of values in the most
    valuable subsequence, and whose second element is the subsequence.

    # >>> items = [(4, 12), (2, 1), (6, 4), (1, 1), (2, 2)]
    # >>> knapsack(items, 15)
    (11, [(2, 1), (6, 4), (1, 1), (2, 2)])
    """


    global K
    K = k

    global MC
    MC =[-1 for m in range (k+1)]
    print MC

    return bestvalue(0,MC)

def bestvalue(i,MC):
    # Return the value of the most valuable subsequence of the first i
    # elements in items whose weights sum to no more than j.
    #@memoized
    if i >K:
        return np.inf
    if i==K:
        return 0
    else:
        if MC[i]==-1:
            MC[i]= min(bestvalue(i + 1,MC)+1,
                       bestvalue(i + 10, MC) + 1,
                       bestvalue(i + 25, MC) + 1,
                       bestvalue(i + 50, MC) + 1)
            print "here"
        print MC
        return MC[i]


k=30
min_coins=min_coins(k)
print MC
print min_coins