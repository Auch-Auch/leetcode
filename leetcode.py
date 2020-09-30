

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(val=5)
root.right = TreeNode(val=8)
root.left = TreeNode(val=4)
root.right.left = TreeNode(val=13)
root.right.right = TreeNode(val=4)
root.right.right.right = TreeNode(val=1)
root.left.left = TreeNode(val=11)
root.left.left.left = TreeNode(val=7)
root.left.left.right = TreeNode(val=2)

root2 = TreeNode(val=1)
root2.left = TreeNode(val=2)


def Symm(left, right):
    queue = [(left, right)]
    if not left and not right:
        return True
    while queue:
        left, right = queue.pop(0)
        if right and left and left.val == right.val:
            if left.left or right.right:
                queue.append((left.left, right.right))
            if left.right or right.left:
                queue.append((left.right, right.left))
        else:
            return False
    return True


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return root == None or Symm(root.left, root.right)

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def Path(root, sum):
            if not root:
                return False
            stack = [(root, root.val)]
            while stack:
                node, sum_val = stack.pop()
                if not node.right and not node.left:
                    if sum_val == sum:
                        return True
                if node.right:
                    stack.append((node.right, sum_val + node.right.val))
                if node.left:
                    stack.append((node.left, sum_val + node.left.val))

            return False
        return Path(root, sum)


solution = Solution()
print(solution.hasPathSum(root2, 1))
