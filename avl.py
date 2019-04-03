#coding:utf-8
class TreeNode(object):
    def __init__(self):
        self.data=0
        self.left=None
        self.right=None
        self.height=0
class BTree(object):
    def __init__(self):
        self.root=None
    def __Max(self,h1,h2):
        if h1>h2:
            return h1
        elif h1<=h2:
            return h2
    def __LL(self,r):#左左情况，向右旋转
        node=r.left
        r.left=node.right
        node.right=r
        r.height=self.__Max(self.getHeight(r.right),self.getHeight(r.left))+1
        node.height=self.__Max(self.getHeight(node.right),self.getHeight(node.left))+1
        return node
    def __RR(self,r):#右右，左旋
        node = r.right
        r.right = node.left
        node.left = r
        r.height = self.__Max(self.getHeight(r.right), self.getHeight(r.left)) + 1
        node.height = self.__Max(self.getHeight(node.right), self.getHeight(node.left)) + 1
        return node
    def __LR(self,r):#左右，先左旋再右旋
        r.left=self.__RR(r.left)
        return self.__LL(r)
    def __RL(self,r):#右左，先右旋再左旋
        r.right=self.__LL(r.right)
        return self.__RR(r)
    def __insert(self,data,r):
        if r==None:
            node=TreeNode()
            node.data=data
            return node
        elif data==r.data:
            return r
        elif data<r.data:
            r.left=self.__insert(data,r.left)
            if self.getHeight(r.left)-self.getHeight(r.right)>=2:
                if data<r.left.data:
                    r=self.__LL(r)
                else:
                    r=self.__LR(r)
        else:
            r.right=self.__insert(data,r.right)
            if self.getHeight(r.right)-self.getHeight(r.left)>=2:
                if data>r.right.data:
                    r=self.__RR(r)
                else:
                    r=self.__RL(r)
        r.height=self.__Max(self.getHeight(r.left),self.getHeight(r.right))+1
        return r
    # 删除data节点
    def __delete(self,data,r):
        if r==None:
            print ("don't have %d"%data)
            return r
        elif r.data==data:
            if r.left==None:#如果只有右子树，直接将右子树赋值到此节点
                return r.right
            elif r.right==None:#如果只有左子树，直接将左子树赋值到此节点
                return r.left
            else:#如果同时有左右子树
                if self.getHeight(r.left)>self.getHeight(r.right):#左子树高度大于右子树
                    #找到最右节点 返回节点值 并删除该节点
                    node=r.left
                    while(node.right!=None):
                        node=node.right
                    r=self.__delete(node.data,r)
                    r.data=node.data
                    return r
                else:#右子树高度大于左子树
                    node=r.right
                    while node.left!=None:
                        node=node.left
                    r=self.__delete(node.data,r)
                    r.data=node.data
                    return r
        elif data<r.data:
            r.left=self.__delete(data,r.left)#在左子树中删除
            if self.getHeight(r.right)-self.getHeight(r.left)>=2:#右子树高度与左子树高度相差超过1
                if self.getHeight(r.right.left)>self.getHeight(r.right.right):
                    r=self.__RL(r)
                else:
                    r=self.__RR(r)
        elif data>r.data:
            r.right=self.__delete(data,r.right)#右子树中删除
            if self.getHeight(r.left)-self.getHeight(r.right)>=2:#左子树与右子树高度相差超过1
                if self.getHeight(r.left.right)>self.getHeight(r.left.left):
                    r=self.__LR(r)
                else:
                    r=self.__LL(r)
        r.height=self.__Max(self.getHeight(r.left),self.getHeight(r.right))+1
        return r
    #先序遍历
    def __show(self,root):
        if root!=None:
            print( root.data)
            self.__show(root.left)
            self.__show(root.right)
        else:
            return 0
    def Insert(self,data):
        self.root=self.__insert(data,self.root)
        return self.root
    def Delete(self,data):
        self.root=self.__delete(data,self.root)
    #求结点的高度
    def getHeight(self,node):
        if node==None:
            return -1
        #print node
        return node.height
    def Show(self):
        self.__show(self.root)
if __name__=='__main__':
    bi=BTree()
    array=[5,1,2,3,4]
    for i in array:
        bi.Insert(i)
    bi.Delete(2)
    bi.Insert(2)
    bi.Show()
