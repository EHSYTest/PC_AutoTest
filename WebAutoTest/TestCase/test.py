w = [1, 2]
n = [2, 1]
list_w = []
for i in range(len(w)):
    list_w_w = []
    for j in range(n[i]+1):
        list_w_w.append(w[i]*j)
    list_w.append(list_w_w)
r = []
for x in range(len(list_w)-1):
    for A in list_w[0]:
        for B in list_w[1]:
            r.append(A+B)
    del list_w[0]
    list_w[0] = r
print(len(set(list_w[0])), set(list_w[0]))

# from functools import reduce
#
# def sum_list(a, b):
#     return [m+n for m in a for n in b]
# r = reduce(sum_list, list_w)
# print(len(set(r)))





# P = [[w[i]*k for k in range(n[i]+1)] for i in range(len(w))]
#
#
# def set_sum(a,b):
#     return [m+n for m in a for n in b]
# L = reduce(set_sum,P)
# # print len(set(L))
# print(P, L)