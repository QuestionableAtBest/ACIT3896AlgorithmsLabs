#Lab link https://gist.github.com/jholman-bcit/0aaf15c62dff31f3c8b4c11edabd1af3
from collections import deque as Deque
from time import perf_counter_ns
class Queue:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self):
        return self.items.pop(0)

    def isNotEmpty(self):
        return len(self.items) > 0


class TreeNode:
    def __init__(self, contents):
        self.contents = contents
        # self.parent = None
        self.children = []

    def __repr__(self):
        return f"TreeNode('{self.contents}')"

    def addChildren(self, *contents):
        children = [TreeNode(c) for c in contents]
        # for child in children:
        #     child.parent = self
        self.children.extend(children)
        return children

    def bfs_badqueue(self):
        ans = []
        queso = Queue()
        queso.add(self)
        while queso.isNotEmpty():
            node = queso.remove()
            ans.append(node.contents)
            for node in node.children:
                queso.add(node)
        return ans            

    def bfs_deque(self):
        ans = []
        dequeso = Deque()
        dequeso.append(self)
        while len(dequeso) != 0:
            node = dequeso.popleft()
            ans.append(node.contents)
            for node in node.children:
                dequeso.append(node)
        return ans      

    def dfs_deque(self):
        ans = []
        dequeso = Deque()
        dequeso.append(self)
        while len(dequeso) != 0:
            node = dequeso.pop()
            ans.append(node.contents)
            for node in reversed(node.children):
                dequeso.append(node)
        return ans      

# Optional Part, using a deque or bad queue
# n = 1000000
# goodQueue = Deque()
# badQueue = Queue()
# times = []
# For various values of n, try adding n things to a queue then removing all n things
# Bad Queue
# for i in range(1000):
#     start = perf_counter_ns()
#     for i in range(n):
#         badQueue.add(i)
#     for i in range(n):
#         badQueue.remove()
#     end = perf_counter_ns()
#     time = (end-start)/1_000_000
#     times.append(time)
# print(f"For size {n}, it took on average {sum(times)/len(times)} milliseconds")

# Good Queue
# for i in range(100):
#     start = perf_counter_ns()
#     for i in range(n):
#         goodQueue.appendleft(i)
#     for i in range(n):
#         goodQueue.pop()
#     end = perf_counter_ns()
#     time = (end-start)/1_000_000
#     times.append(time)
# print(f"For size {n}, it took on average {sum(times)/len(times)} milliseconds")
    
"""
A tree could look like this:
               Z
           /   |   \ 
        Q      R      S
      / | \   / \   / | \ 
    A   B  C  D E  F  G  H
   / \        |      / \ 
  T   U       W     X   Y
              |
              J
"""

root1 = TreeNode("Z")
[Q, R, S] = root1.addChildren("Q", "R", "S")
[A, B, C] = Q.addChildren("A", "B", "C")
[D, E] = R.addChildren("D", "E")
[F, G, H] = S.addChildren("F", "G", "H")
[T, U] = A.addChildren("T", "U")
[W] = D.addChildren("W")
[X, Y] = G.addChildren("X", "Y")
[J] = W.addChildren("J")

correct_dfs = "Z Q A T U B C R D W J E S F G X Y H".split(" ")
# print("\nDFS should be: [", ', '.join(correct_dfs), "]")
correct_bfs = "Z Q R S A B C D E F G H T U W X Y J".split(" ")
# print("\nweird-order DFS should be: [", ', '.join(weird_correct_dfs), "]")

part1_ans = root1.bfs_badqueue()
print("\npart 1 goal:   ", correct_bfs)
if part1_ans == correct_bfs:
    print("part 1 successful match")
else:
    print("part 1 actual: ", part1_ans)

part2_ans = root1.bfs_deque()
print("\npart 2 goal:   ", correct_bfs)
if part2_ans == correct_bfs:
    print("part 2 successful match")
else:
    print("part 2 actual: ", part2_ans)


part3_ans = root1.dfs_deque()
print("\npart 3 goal:   ", correct_dfs)
if part3_ans == correct_dfs:
    print("part 3 successful match")
else:
    print("part 3 actual: ", part3_ans)