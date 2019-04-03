
class Solution:
    def Print1ToMaxOfNDigits(self, n):
        if n<=0:
            return
        number=['0']*n#用数组来表示[‘0’，‘0’~~]
        for i in range(10):
            number[0]=str(i)#依次取0-9的值，第一位
            self.Print1ToMaxOfNDigitsRecursively(number,n,0)#第一次调用递归函数

    def PrintNumber(self,number):#输出数字
        #此处的number为一个str类型的数组，每个数组元素是一个0-9之间数字的字符串形式
        isBeginning0=True
        nLength=len(number)
        for i in range(nLength):
            if isBeginning0 and number[i]!='0':#只输出非零项
                isBeginning0=False
            if not isBeginning0:
                print('%c' %number[i],end='')
        print('\t')

    def Print1ToMaxOfNDigitsRecursively(self,number,length,index):#index表示变换位数
        if index==length-1:#最后一位
            self.PrintNumber(number)
            return
        for i in range(10):
            number[index+1]=str(i)#改变下一位
            self.Print1ToMaxOfNDigitsRecursively(number,length,index+1)#递归调用

if __name__=="__main__":
    Solution().Print1ToMaxOfNDigits(3)
#----------------------------------------------------------------
def printMaxN(n):
    #null str
    if n==0:
        return 0
    number = ['0']*n
    for i in range(10):
        number[0] = str(i)
        nextMaxN(number,n,0)
def nextMaxN(number,n,index):
    #last one
    if index == n-1:
        maxNPrint(number,n)
        return
    # not last one
    for i in range(10):
        number[index+1] = str(i)
        nextMaxN(number,n,index+1)

def maxNPrint(number,n):
    flag = 1
    for i in range(n):
        if number[i]!='0'and flag==1:
            flag = 0
        if not flag:
            print('%c' % number[i],end = '')
    print("\t")
if __name__ == '__main__':
    n = int(input())
    printMaxN(n)
