import numpy as np

#one way:
# def min_coins(k):
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
# k=30
# min_coins=min_coins(k)
# print MC
# print min_coins




#and the other:
# def min_coins(k):
#     global K
#     K = k
#
#     global MC
#     MC =[-1 for m in range (k+1)]
#     print MC
#
#     return bestvalue(0,MC)
#
# def bestvalue(i,MC):
#     # Return the value of the most valuable subsequence of the first i
#     # elements in items whose weights sum to no more than j.
#     #@memoized
#     if i >K:
#         return np.inf
#     if i==K:
#         return 0
#     else:
#         if MC[i]==-1:
#             MC[i]= min(bestvalue(i + 1,MC)+1,
#                        bestvalue(i + 10, MC) + 1,
#                        bestvalue(i + 25, MC) + 1,
#                        bestvalue(i + 50, MC) + 1)
#             print "here"
#         print MC
#         return MC[i]
#
#
# k=30
# min_coins=min_coins(k)
# print MC
# print min_coins


# new try:
def min_coins(k):
    global MC
    MC = np.full((k + 1, k + 1, k + 1, k + 1), -1)
    # print MC
    return bestvalue(k,k,k,k, MC)

def bestvalue(i,j,l,m,MC):
    # Return the value of the most valuable subsequence of the first i
    # elements in items whose weights sum to no more than j.
    #@memoized
    if i<0 or j<0 or l<0 or m<0:
        return np.inf

    if  4*k - (i+j+l+m)>k:
        return np.inf

    if  4*k - (i+j+l+m)==k:
        print "here"
        return 0

    else:
        print i, j, l, m
        if MC[i,j,l,m]==-1:
            MC[i,j,l,m]= min(bestvalue(i - 1,j,l,m,MC)+1,
                       bestvalue(i,j - 10,l,m, MC) + 1,
                       bestvalue(i,j,l - 25,m, MC) + 1,
                       bestvalue(i,j,l,m - 50, MC) + 1)
            # print MC
        print i,j,l,m
        return MC[i,j,l,m]

k=12
min_coins=min_coins(k)
# print MC
print min_coins