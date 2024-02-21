#Lab link: https://gist.github.com/jholman-bcit/cb012203df18f5a74a88f6071c0354bb
class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
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

    def dfs_stack_of_pairs(self):
        ### This is a hint, which you might use or ignore, as you choose
        ans = []
        s = Stack()
        s.push([self, 0])
        while s.isNotEmpty():
            pair = s.pop()
            node = pair[0]
            child_index = pair[1]
            
            # Check if this is new node, if it is add to list.
            if child_index == 0:
                ans.append(node.contents)

            # Check if there are remaining children to explore, if so add to stack.
            if child_index < len(node.children):
                child = node.children[child_index]
                s.push((node, child_index + 1))
                s.push((child, 0))        
                
        return ans
    def dfs_todos_badorder(self):
        ### This is a hint, which you might use or ignore, as you choose
        # ans = []
        # s = Stack()
        # s.push(self)
        # while s.isNotEmpty():
        #     pass
        # return ans

        return "part 2 not implemented"         # obviously you delete this line when you do part 2

    def dfs_todos_goodorder(self):

        return "part 3 not implemented"         # obviously you delete this line when you do part 3




'''
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
'''

root1 = TreeNode("Z")
[Q, R, S] = root1.addChildren('Q', 'R', 'S')
[A, B, C] = Q.addChildren('A', 'B', 'C')
[D, E] = R.addChildren('D', 'E')
[F, G, H] = S.addChildren('F', 'G', 'H')
[T, U] = A.addChildren('T', 'U')
[W] = D.addChildren('W')
[X, Y] = G.addChildren('X', 'Y')
[J] = W.addChildren('J')

correct_dfs = "Z Q A T U B C R D W J E S F G X Y H".split(' ')
# print("\nDFS should be: [", ', '.join(correct_dfs), "]")
weird_correct_dfs = "Z S H G Y X F R E D W J Q C B A U T".split(' ')
# print("\nweird-order DFS should be: [", ', '.join(weird_correct_dfs), "]")

part1_ans = root1.dfs_stack_of_pairs()
print("\npart 1 goal:   ", correct_dfs)
if part1_ans == correct_dfs:
    print("part 1 successful match")
else:
    print("part 1 actual: ", part1_ans)

part2_ans = root1.dfs_todos_badorder()
print("\npart 2 goal:   ", weird_correct_dfs)
if part2_ans == weird_correct_dfs:
    print("part 2 successful match")
else:
    print("part 2 actual: ", part2_ans)


part3_ans = root1.dfs_todos_goodorder()
print("\npart 3 goal:   ", correct_dfs)
if part3_ans == correct_dfs:
    print("part 3 successful match")
else:
    print("part 3 actual: ", part3_ans)