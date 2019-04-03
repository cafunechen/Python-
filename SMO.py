# -*- coding: utf-8 -*-
from numpy import *
# 加载数据
def loadDataSet(fileName):
    dataMat = [];labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = line.strip().split('\t')
        dataMat.append([float(lineArr[0]),float(lineArr[1])])
        labelMat.append([float(lineArr[2])])
    return  dataMat,labelMat

# 从0到m中产生一个不为i的整数
def selectJrand(i,m):
    j = i
    while(j == i):
        j = int(random.uniform(0,m))
    return j

# 使得aj 在边界值[L,H]以内
def clipAlpha(aj,H,L):
    if aj > H:
        aj = H
    if L > aj:
        aj = L
    return aj


#SMO 序列最小优化
def smoSimple(dataMatIn,classLabels,C,toler,maxIter):
    # 这里书上的代码有误，不用mat(classLabels)不用转置
    dataMat = mat(dataMatIn)
    labelMat = mat(classLabels)
    b = 0
    m,n = shape(dataMat)
    alphas = mat(zeros((m,1)))
    iter = 0
    # alphaPairsChanged 用来更新的次数
    # 当遍历  连续无更新 maxIter 轮，则认为收敛，迭代结束
    while iter < maxIter:
        alphaPairsChanged = 0
        for i in range(m):
            # KKT 条件计算出
            fXi = float(multiply(alphas,labelMat).T * (dataMat*dataMat[i,:].T))+b
            # 误差
            Ei = fXi - float(labelMat[i])
            # toler：容忍错误的程度
            # labelMat[i]*Ei < -toler 则需要alphas[i]增大，但是不能>=C
            # labelMat[i]*Ei > toler 则需要alphas[i]减小，但是不能<=0
            if ((labelMat[i]*Ei < -toler) and (alphas[i] < C)) or ((labelMat[i]*Ei > toler) and (alphas[i] > 0)):
                # 从0到m中产生一个不为i的整数
                j = selectJrand(i,m)
                fXj = float(multiply(alphas,labelMat).T * (dataMat*dataMat[j,:].T)+b)
                Ej = fXj - float(labelMat[j])
                alphaIold = alphas[i].copy()
                alphaJold = alphas[j].copy()
               # 算法讲解“二变量优化问题”部分
                if labelMat[i] != labelMat[j]:
                    L = max(0,alphas[j]-alphas[i])
                    H = min(C,C+alphas[j]-alphas[i])
                else:
                    L = max(0,alphas[j] + alphas[i] - C)
                    H = min(C,alphas[j] + alphas[i])

                if L == H:
                    print("L == H")


               # 见式 7.107
                eta = -2.0* dataMat[i,:] * dataMat[j,:].T + dataMat[i,:] *\
                                                            dataMat[i,:].T + dataMat[j,:] * dataMat[j,:].T
                if eta <= 0:
                    print("eta <= 0")

                # 见式 7.106
                alphas[j] += labelMat[j]*(Ei-Ej)/eta
                # 见式 7.108 ，讲alphas[j] 约束在 [L,H]
                alphas[j] = clipAlpha(alphas[j],H,L)
                if(abs(alphas[j] - alphaJold) < 0.00001):
                    print("j not moving")
               # 见式 7.109
                alphas[i] += labelMat[j]*labelMat[i]*(alphaJold-alphas[j])
               # 见式 7.114
                b1 = b - Ei -labelMat[i]*(alphas[i]-alphaIold)*dataMat[i,:]*dataMat[i,:].T\
                     - labelMat[j]*(alphas[j]-alphaJold)*dataMat[i,:]*dataMat[j,:].T
                b2 = b - Ej - labelMat[i] * (alphas[i] - alphaIold) * dataMat[i, :] * dataMat[j, :].T \
                     - labelMat[j] * (alphas[j] - alphaJold) * dataMat[j, :] * dataMat[j, :].T

                if  (0 < alphas[i]) and (C > alphas[i]):
                    b = b1
                elif (0 < alphas[j]) and (C > alphas[j]):
                    b = b2
                else:
                    b = (b1+b2)/2.0

                alphaPairsChanged += 1
                print ("iter: %d i:%d pairs: %d" %(iter,i,alphaPairsChanged))

        if alphaPairsChanged == 0:
            iter += 1
        else:
            iter = 0
        print ("iter %d" %iter)

    return b,alphas
