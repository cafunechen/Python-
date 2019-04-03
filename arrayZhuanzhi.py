
# -*- coding:utf-8 -*-
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
    # write code here
        result = []
        while matrix:
            result += matrix.pop(0)
            if not matrix:
                break
            matrix = self.turn(matrix)
        return result

    def turn(self, matrix):
    # 逆时针旋转函数
        col = len(matrix[0])
        newmat = []
        for i in range(col, 0, -1):
            newmat.append([x[i-1] for x in matrix])
        return newmat

if __name__ =="__main__":
    a = Solution()
    b = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    print(a.printMatrix(b))
