class TreeNode(object): 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        self.height = 1
        self.parent = None
class AVL_Tree(object): 
    # def __init__(self, val, left=None, right=None):
    #   self.val = val ; self.left = left ; self.right = right 
    def newNode(self, val): 
        temp = TreeNode(0) 
        temp.data = val 
        temp.left = None
        temp.right = None
        return temp 
    def checkTime(self, tree,k):
        timenow = myTree.minValue(tree)
        is_available = False
        while True:
            try:
                t = int(input("Please enter time registration: "))
            except ValueError:
                print("Sorry, You must enter a number of characters.")
                continue
            else:
                if timenow >= int(t):
                    print("Registration time has expired !")
                    continue
                else:
                    t = int(t)
                    for x in range(t-(k), t+(k)):
                        # print("x = "+ str(x),myTree.find(tree,x))
                        if myTree.find(tree,x) == True:
                            is_available = True
                            print("Registration failed!")        
                            break
                        else:
                            is_available = False
                    if is_available == False:
                        print("Registration successful!") 
                        tree = myTree.insert(tree, t) 
                        print("{0} ".format(tree.val), end="") 
                        self.preOrder(tree.left) 
                        self.preOrder(tree.right)
                        return tree
    def insert(self, root, key): 
        if not root: 
            return TreeNode(key) 
        elif key < root.val: 
            lchild  = self.insert(root.left, key)
            root.left = lchild
            lchild.parent = root
        else: 
            lchild  = self.insert(root.right, key)
            root.right = lchild
            lchild.parent = root
        root.height = 1 + max(self.getHeight(root.left), 
                           self.getHeight(root.right)) 
  
        return root 
    def getHeight(self, root): 
        if not root: 
            return 0
        return root.height 
        if not root: 
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right) 
  
    def preOrder(self, root): 
  
        if not root: 
            return
 
        print("{0} ".format(root.val), end="") 
        self.preOrder(root.left) 
        self.preOrder(root.right) 
    def minValue(self,root): 
        current = root 
        # loop down to find the lefmost leaf 
        while(current.left is not None): 
            current = current.left 
        return current.val
    def maxValue(self, root): 
        # Base case  
        if (root == None):  
            return 0
        res = root.val 
        lres = myTree.maxValue(root.left)  
        rres = myTree.maxValue(root.right) 
        if (lres > res): 
            res = lres  
        if (rres > res):  
            res = rres  
        return res  
    def find(self, root,val):
        return self.findNode(root, val)

    def findNode(self, root, val):
        current = root 
        if current is None:
            return False
        elif val == current.val:
            return True
        elif val < current.val:
            return self.findNode(current.left, val)
        else:
            return self.findNode(current.right, val)
    def successor_node_right(self, n):
        """Returns the node with the smallest key larger than this node's key, or None if this has the largest key in the tree."""
        
        if n.right is not None:
            return self.minValue(n.right)
        current = n.parent
        while current is not None:
            if n != current.right:
                break
            n = current
            current = current.parent
        return current.val

    def successor_node_left(self, n):
        """Returns the node with the smallest key larger than this node's key, or None if this has the largest key in the tree."""
        if n.left is not None:
            return self.minValue(n.left)
        current = n.parent
        while current is not None:
            if n != current.left:
                break
            n = current
            current = current.parent
        return current.val
    def findnext(self, t, root):
        """Return the node for key t if is in the tree, or None otherwise."""
        node = root
        while node is not None:
            if t == node.val:
                return node
            elif t < node.val:
                node = node.left
            else:
                node = node.right
        return None
# Driver program to test above function 
if __name__ == "__main__": 
    myTree = AVL_Tree() 
    root = None
    tree = None
    root = myTree.insert(root, 37) 
    root = myTree.insert(root, 41) 
    root = myTree.insert(root, 46) 
    root = myTree.insert(root, 49) 
    root = myTree.insert(root, 56) 
    tree = myTree.checkTime(root,3)
    maxvalue = myTree.maxValue(tree)
    minvalue = myTree.minValue(tree)
    #1. thời gian đăng ký hạ cánh sớm nhất còn lưu trong cấu trúc
    timeLandingEarliest = "\n2. the earliest landing time: " + str(minvalue)
    print(timeLandingEarliest)
    #2. thời gian đăng ký hạ cánh trể nhất còn lưu trong cấu trúc
    t = int(input("Enter time now: "))
    timeLandingLatest = "3. the Latest landing time: " + str(maxvalue)
    # 4. Trả về thời điểm hạ cánh kế tiếp của thời điểm t cho trước, nếu t là giá trị lớn nhất trong cấu trúc thì -1 được trả về
    timeNext = "4. Next landing time (t ="+str(t)+"): " + str(myTree.successor_node_right(myTree.findnext(t, tree)))
    # 5. Trả về thời điểm hạ cánh trước đó của thời điểm t cho trước, nếu t là giá trị nhỏ nhất trong cấu trúc thì -1 được trả về.
    timePrevious = "5. Previous landing time (t ="+str(t)+" ) : " + str(myTree.successor_node_left(myTree.findnext(t, tree)))
    print(timeNext)
    print(timePrevious)

