from collections import deque


def greedyCoinChanging(M, k):
   n = len(M)
   result = []
   for i in range(n - 1, -1, -1):
       result += [(M[i], k // M[i])]
       k %= M[i]
   return result


def test_greedyCoinChanging(M, k):
   rv = greedyCoinChanging(M, k)
   print(f"greedyCoinChanging({M}, {k}) = {rv}")


test_greedyCoinChanging([1,5, 10, 25], 77)
test_greedyCoinChanging([1,2, 3, 4], 6)


def greedyCanoeistA(W, k):
    N = len(W)
    skinny = deque()
    fatso = deque()
    for i in range(N - 1):
        if W[i] + W[-1] <= k:
            skinny.append(W[i])
        else:
            fatso.append(W[i])
    fatso.append(W[-1])
    canoes = 0
    while skinny or fatso:
        if len(skinny) > 0:
            skinny.pop()
        fatso.pop()
        canoes += 1
        if not fatso and skinny:
            fatso.append(skinny.pop())
        while len(fatso) > 1 and fatso[-1] + fatso[0] <= k:
            skinny.append(fatso.popleft())
    return canoes
