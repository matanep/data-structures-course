
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



    global MC
    MC =[[-1 for m in range (k+1)] for n in range (len(items)+1)]
    print MC
    j = k
    return bestvalue(k,MC)

def bestvalue(k,MC):
    # Return the value of the most valuable subsequence of the first i
    # elements in items whose weights sum to no more than j.
    #@memoized
        if MC[i][j]==-1:
            value, weight = items[i - 1]
            if i == 0:
                NS[i][j] =0
            else:
                if weight > j:
                    NS[i][j]=bestvalue(i - 1, j,NS)
                else:
                    NS[i][j]= max(bestvalue(i - 1, j,NS),
                       bestvalue(i - 1, j - weight,NS) + value)
        return NS[i][j]



# if __name__ == '__main__':

items = [(4, 12), (2, 1), (6, 4), (1, 1), (2, 2)]
maxweight=15
knapsack=knapsack(items, maxweight)
print NS
print knapsack
j = maxweight
result = []
for i in xrange(len(items), 0, -1):
    if NS[i][j]!= NS[i-1][j]:
        result.append(items[i - 1])
        j -= items[i - 1][1]
result.reverse()
print [knapsack,result]

