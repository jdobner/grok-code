import typing
from collections import defaultdict


class Node:
    nodes = {}

    def __init__(self, value: int, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


__nodes = {}


def node(value: int) -> Node:
    return __nodes.setdefault(value, Node(value))


def print_nodes(node: Node):
    if node.left:
        print_nodes(node.left)
    print(node.value)
    if node.right:
        print_nodes(node.right)


def print_nodes_2(node: Node, lines: typing.List[str], level: int, pos: int):
    if len(lines) <= level:
        lines.append("")
    if node.left:
        print_nodes_2(node.left, lines, level + 1, pos + 1)
    else:
        lines[level] += " "
    if node.right:
        print_nodes_2(node.right, lines, level + 1, pos + 2)
    lines[level] = add(lines[level], node.value, pos)


def add(s: str, value: int, pos: int) -> str:
    s += " " * ((pos * 2) - len(s)) + str(value)
    return s


def main():
    head_node = node(3)
    node(3).left = node(1)
    node(1).right = node(2)
    node(3).right = node(5)
    node(5).right = node(6)
    print_nodes(head_node)
    print("")
    arr = []
    print_nodes_2(head_node, arr, 0, 0)
    for s in arr:
        print(s)


if __name__ == "__main__":
    main()