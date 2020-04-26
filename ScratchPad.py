"""def nestedSum(u, v):
    total = sum([(u[i] * v[j] - u[j] * v[i]) ** 2 for i in range(len(u)) for j in range(len(u))])
    return total / 2"""

P = [2,3]
A = [3, 2]
dict1 = {p: a for (p, a) in zip(P, A)}

dict_ = {p: dict1[p] for p in dict1.keys() & {0}}
print(dict_)

Q = [0, 0, 0]
