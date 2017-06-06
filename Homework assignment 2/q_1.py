import numpy as np

# #solution using memoization:
# def min_coins(k,v_1,v_2,v_3,v_4):
#     global MC
#     MC =[-1 for m in range (k)]
#     return bestvalue(k,MC,v_1,v_2,v_3,v_4)
#
# def bestvalue(i,MC,v_1,v_2,v_3,v_4):
#
#     if i <0:
#         return np.inf
#     if i==0:
#         return 0
#     else:
#         if MC[i-1]==-1:
#             MC[i-1]= min(bestvalue(i - v_1,MC,v_1,v_2,v_3,v_4)+1,
#                        bestvalue(i - v_2,MC,v_1,v_2,v_3,v_4)+1,
#                        bestvalue(i - v_3,MC,v_1,v_2,v_3,v_4)+1,
#                        bestvalue(i - v_4,MC,v_1,v_2,v_3,v_4)+1)
#         return MC[i-1]
# v_1=2
# v_2=10
# v_3=25
# v_4=50
#
# k=82
# min_coins=min_coins(k,v_1,v_2,v_3,v_4)
# print MC
# print min_coins



#solution using bottom-up :
# def min_coins(k,v_1,v_2,v_3,v_4):
#     # global K
#     # K = k
#
#     global MC
#     MC =[-1 for m in range (k+1)]
#     return bestvalue(k,MC,v_1,v_2,v_3,v_4)
#
# def bestvalue(k,MC,v_1,v_2,v_3,v_4):
#     fun = (lambda x: np.inf if x < 0 else 0 if x==0 else MC[x])
#
#     for i in range(len(MC)):
#
#         MC[i]=min(fun(i - v_1)+1,
#                    fun(i - v_2)+1,
#                     fun(i - v_3)+1,
#                    fun(i - v_4)+1)
#
#     return MC[k]
#
#
# v_1=2
# v_2=10
# v_3=25
# v_4=50
# k=30
# min_coins=min_coins(k,v_1,v_2,v_3,v_4)
# print MC
# print min_coins


def greedy_solution(k,v_1,v_2,v_3,v_4):
    valus=[v_1,v_2,v_3,v_4]
    sorted_index=sorted(range(len(valus)), key=lambda k: valus[k],reverse=True)
    sum_coins=0
    number_of_coins=[0 for i in range(4)]
    for i in sorted_index:
        while sum_coins+valus[i] <= k:
            sum_coins += valus[i]
            number_of_coins[i]+=1

    if sum_coins==k:
        return sum(number_of_coins),number_of_coins
    else:
        return "Greedy Solution dos not work"

v_1=1
v_2=10
v_3=25
v_4=50
k=30
min_coins=greedy_solution(k,v_1,v_2,v_3,v_4)
print min_coins