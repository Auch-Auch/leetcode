

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


class Solution_trees:
    current_sum = 0

    def isSymmetric(self, root: TreeNode) -> bool:
        return root == None or Symm(root.left, root.right)

    def hasPathSumIter(self, root, sum) -> bool:
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

    def preoderIter(self, root) -> list:
        if not root:
            return []
        stack = [root]
        ans = []
        while stack:
            node = stack.pop()
            ans.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return ans

    def inorderIter(self, root) -> list:
        stack = []
        ans = []
        node = root
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack.pop()
                ans.append(node.val)
                node = node.right
        return ans

    def BFS(self, root) -> list:
        queue = [root]
        ans = []
        if not root:
            return []
        while queue:
            arr = []
            for i in range(len(queue)):
                node = queue.pop(0)
                arr.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(arr)
        return ans

    def hasPathSumRec(self, root, sum) -> bool:
        def recursive(root, sum, current_sum=0):
            if not root:
                return False
            current_sum += root.val
            if not root.right and not root.left:
                if sum == current_sum:
                    return True
            return recursive(root.left, sum, current_sum) + recursive(root.right, sum, current_sum)
        return bool(recursive(root, sum))

    def buildTree(self, inorder: list, postorder: list) -> TreeNode:
        pass


solution = Solution_trees()
print(solution.hasPathSumRec(root, 17))
