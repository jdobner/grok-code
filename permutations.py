def find_permutation(s: str, pattern: str) -> bool:
    l = [c for c in pattern]
    for n in range(len(l)):
        for i in range(len(l)-1):
            l[i], l[i+1] = l[i+1], l[i]
            newString = "".join(l)
            if s.find(newString) >= 0:
                return True
    return False


def permutate(s: str):
    l = [c for c in s]
    for n in range(len(l)):
        for i in range(len(l) - 1):
            l[i], l[i + 1] = l[i + 1], l[i]
            newString = "".join(l)
            print(newString)

permutate('abc')
print(find_permutation('oidbcaf', 'abc'))