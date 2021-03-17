from typing import Tuple, List, Set
from pprint import pprint as pp

data = [[12, 13, 1, 12], [13, 4, 13, 12], [13, 8, 10, 12], [12, 13, 12, 12], [13, 13, 13, 13]]

def get(x, y):
    return data[y][x]

print(get(1,1))

def get_unvisited_adjacent(x1, y1, visited) -> List[Tuple[int, int]]:
    around_me = ((x1 - 1, y1),
                 (x1, y1 - 1),
                 (x1 + 1, y1),
                 (x1, y1 + 1))
    return [r for r in around_me if r not in visited]


def get_volume():
    total = 0
    s = []
    for x in range(len(data[0])):
        for y in range(len(data)):
            capacity, chain = search(x, y)
            capacity -= get(x, y)
            assert capacity >= 0
            if capacity > 0:
                s.append(f'capacity({x}, {y}) = {capacity}, chain={chain}')
            total += capacity
    for t in s:
        print(t)
    return total



def not_edge(x, y):
    return 0 < x < len(data[0]) - 1 and 0 < y < len(data) - 1


def search(x, y, visited=None) -> (int, List[int]):
    if visited is None:
        visited = set()

    visited.add((x, y))

    print_d(x, y, visited)
    adj = get_unvisited_adjacent(x, y, visited)
    print(x, y, " -> ", adj)
    my_height = get(x, y)

    if not_edge(x, y) and adj:
        low = 20000
        the_chain = []
        for next_x, next_y in adj:
            cap, chain = search(next_x, next_y, visited)
            if cap < low:
                low = cap
                the_chain = chain
        the_chain.insert(0, (x, y))
        return max(my_height, low), the_chain
    else:
        return my_height, [(x, y)]


def print_d(x: int, y: int, visited: Set[Tuple[int, int]]):
    print(f'adj to ({x}, {y}):')

    def _map(arg):
        _x, _v = arg
        s = "*" if _x == x and _y == y else " "
        s2 = "x" if (_x, _y) in visited else " "
        return f"{s}{_v}{s2}"

    for _y, a in enumerate(data):
        print(list(map(_map, enumerate(a))))
    print("\n")

# v = get_volume()
# print(f'volume = {v}')


def testp(a,b,c):
    print(a,b,c)
