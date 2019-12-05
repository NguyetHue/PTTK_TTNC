class TreeNode(object): 
    def __init__(self, val): 
        self.val = val 
        self.left = None
        self.right = None
        self.height = 1
class AVL_Tree(object): 
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
            root.left = self.insert(root.left, key) 
        else: 
            root.right = self.insert(root.right, key) 
        root.height = 1 + max(self.getHeight(root.left), 
                           self.getHeight(root.right)) 
        balance = self.getBalance(root) 
        if balance > 1 and key < root.left.val: 
            return self.rightRotate(root) 
        if balance < -1 and key > root.right.val: 
            return self.leftRotate(root) 
        if balance > 1 and key > root.left.val: 
            root.left = self.leftRotate(root.left) 
            return self.rightRotate(root) 
        if balance < -1 and key < root.right.val: 
            root.right = self.rightRotate(root.right) 
            return self.leftRotate(root) 
  
        return root 
  
    def leftRotate(self, z): 
  
        y = z.right 
        T2 = y.left 
  
        # Perform rotation 
        y.left = z 
        z.right = T2 
  
        # Update heights 
        z.height = 1 + max(self.getHeight(z.left), 
                         self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                         self.getHeight(y.right)) 
  
        # Return the new root 
        return y 
  
    def rightRotate(self, z): 
  
        y = z.left 
        T3 = y.right 
  
        # Perform rotation 
        y.right = z 
        z.left = T3 
  
        # Update heights 
        z.height = 1 + max(self.getHeight(z.left), 
                        self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                        self.getHeight(y.right)) 
  
        # Return the new root 
        return y 
  
    def getHeight(self, root): 
        if not root: 
            return 0
  
        return root.height 
  
    def getBalance(self, root): 
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
    timeLandingLatest = "3. the Latest landing time: " + str(maxvalue)
    print(timeLandingLatest)
