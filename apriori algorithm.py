import numpy
import itertools



f = open('input.txt', 'r')
fw = open('output.txt', 'w')

itemset = []

for line in f:
    line = line.replace('\n', '').replace('\r', '')
    line = line.split() # 用空格分割
    line = list(set(line)) # 去重
    line.sort() # 排序
    line = [int(x) for x in line]

    itemset.append(line) # 把新整理好的一行数据放入到



dataSupport = []
for i in range(len(itemset)):
    dataSupport.extend(itemset[i])
data = list(set(dataSupport))



minSupport = 2
print("Lines in database is:", len(itemset))
print("minSupport:", minSupport)

print("\nitemset read completed.") # 数据读取完毕
print("Calculating ...\n") # 开始算法
'''
读取数据模块，并进行一定的数据处理
'''





'''''''''
主函数开始
'''''''''
'''
第一次运算
'''
C1 = numpy.zeros([len(data), 2])

for i in range(len(data)): # data: [0, 1, 2, 3, 4]
    C1[i:] = numpy.array([data[i], dataSupport.count(data[i])])

# print("C1: ", end = ''); print(C1) #打印C1: [[0, 3],[1, 4],[2, 1],[3, 2],[4, 2]]
'''
删掉小于minSupport的C1，生成L1
'''
removeList = []
for i in range(C1.shape[0]): # shape[0]：读取矩阵第一维度的长度
    if C1[i, -1] < minSupport:
        removeList.append(i)
L1 = numpy.delete(C1, removeList, 0)
'''
删掉小于minSupport的C1，生成L1
'''

'''
输出 1 结果
'''
# 输出 1 结果
ans = [tuple(i) for i in L1] # numpy数组变成tuple
ans = list(set(ans)) # 去重
ans.sort() # 排序
# print("**ans: ", end = ''); print(ans) # 结果：[(4.0, 2.0), (3.0, 2.0), (0.0, 3.0), (1.0, 4.0)]

for i in ans:
    print("(", end = ''); print(i[0], end = ''); print(") ----------> ", end = ''); print(i[-1])
    fw.write("1 "); fw.write(str(int(i[0]))); fw.write(' '); fw.write(str(int(i[-1]))); fw.write('\n') #写入文件

'''
输出 1 结果
'''


'''
开始进行迭代，从2-n
'''
Ln = L1; n = 1 # n是集合中元素的个数，每上一层，元素个数加一

while (numpy.max(Ln[:,-1]) > minSupport):

    '''''''''
    Ln -> Cn+1（不考虑脚标，直接覆盖原来的Cn）
    首先读取数据（解包，把support扔掉）之后拆解成元素，最后重新组合，并计算好support之后附加在list末尾，形成新的包
    向上层继续传递（Ln -> Cn），实现由L至C的转换
    '''''''''
    '''
    解包二维数组，并且把最后的support删掉，获得纯净的数据，为之后的解包做准备
    '''
    lastLayerAllData = []
    for i in range(Ln.shape[0]): # shape[0]：读取矩阵第一维度的长度
        # 表示在n个数组（维）中取全部数据，x[n,:]：取第n集合的所有数据（x[n,:-1]：扔掉最后一个数据，即support）
        # 这里更新的是每一次的Ln，所以每个组长度一样，比如说[[0.0, 1.0], [0.0, 4.0], [1.0, 3.0], [1.0, 4.0]]
        lastLayerAllData.append(list(Ln[i,:-1]))    
    # print("lastLayerAllData: ",end = ''); print(lastLayerAllData) #打印上一层的所有分组
    '''
    解包二维数组，并且把最后的support删掉，获得纯净的数据，为之后的解包做准备
    '''

    '''
    拆分数据，把lastLayerAllData变成一个一个元素
    '''
    thisLayerAllElement = [] # 开始拆分本层所有数据

    for i in range(Ln.shape[0]-1):
        for j in range(i+1, Ln.shape[0]):
            if (Ln[j, -2]>Ln[i, -2]):
                temp = list(numpy.copy(lastLayerAllData[i]))
                temp.append(Ln[j, -2])
                thisLayerAllElement.append(temp) # thisLayerAllElement：拆分完成的本层所有数据（拆成零散元素，之后重新组合）
    '''
    拆分数据，把lastLayerAllData变成一个一个元素
    '''      
    
    '''
    用迭代器制造新的C，方法就是把之前拆掉的元素进行迭代，之后产生新的分组
    这里不需要验证分组是否符合support limit，只需要生成就好了
    '''
    combinationList =[]
    thisLayerAllData =[]
    for element in range(len(thisLayerAllElement)):
        for combination in itertools.combinations(thisLayerAllElement[element], n):  # 迭代产生所有元素可能性组合
            combinationList.append(list(combination))
        if ([item for item in combinationList if item not in lastLayerAllData]) ==[] :
            thisLayerAllData.append(thisLayerAllElement[element])
        combinationList = []
    '''
    用迭代器制造新的C，方法就是把之前拆掉的元素进行迭代，之后产生新的分组
    这里不需要验证分组是否符合support limit，只需要生成就好了
    '''

    '''
    这里计算thisLayerAllData的support，并附加在列表最后一项中，
    到此这部分结束了（重新变成二维，就是下一次的Cn）
    '''
    num = 0
    thisLayerAllDataAndSupport = numpy.copy(thisLayerAllData)
    thisLayerAllDataAndSupport = numpy.column_stack((thisLayerAllDataAndSupport, numpy.zeros(thisLayerAllDataAndSupport.shape[0])))
    
    for i in range(len(thisLayerAllData)):
        for j in range(len(itemset)):
            if ([item for item in thisLayerAllData[i] if item not in itemset[j]]) ==[] :
                num = num+1
        thisLayerAllDataAndSupport[i,-1] = num
        num = 0          
    
    Cn = thisLayerAllDataAndSupport
    '''
    这里计算thisLayerAllData的support，并附加在列表最后一项中，
    到此这部分结束了
    '''
    '''''''''
    Ln -> Cn+1（不考虑脚标，直接覆盖原来的Cn）
    首先读取数据（解包，把support扔掉）之后拆解成元素，最后重新组合，并计算好support之后附加在list末尾，形成新的包
    向上层继续传递（Ln -> Cn），实现由L至C的转换
    '''''''''





    '''''''''
    删掉小于minSupport的Cn，生成Ln
    Cn+1 -> Ln+2（不考虑脚标，直接覆盖原来的Ln）
    '''''''''
    removeList = []
    for i in range(Cn.shape[0]): # shape[0]：读取矩阵第一维度的长度
        if Cn[i,-1] < minSupport:
            removeList.append(i)
    Ln = numpy.delete(Cn, removeList, 0) 
    '''''''''
    删掉小于minSupport的Cn，生成Ln
    Cn+1 -> Ln+2（不考虑脚标，直接覆盖原来的Ln）
    '''''''''




    
    n = n+1 # n++，向前进位，进入下一层


    
    '''
    输出 2-n 结果
    '''
    ans = [tuple(i) for i in Ln] # numpy数组变成tuple
    ans = list(set(ans)) # 去重
    ans.sort() # 排序
    #print("**ans: ", end = ''); print(ans)
    #结果：    #[(0.0, 4.0, 2.0), (0.0, 1.0, 3.0), (1.0, 3.0, 2.0), (1.0, 4.0, 2.0)]
                    #[(0.0, 1.0, 4.0, 2.0)]
    
    for i in ans:
        print(i[:-1], end = ''); print(" ----------> ", end = ''); print(i[-1])
        fw.write(str(n)); fw.write(' ')
        for allSet in i[:-1]:
            fw.write(str(int(allSet)))
            fw.write(' ')
        fw.write(str(int(i[-1])))
        fw.write('\n') #写入文件
    
    '''
    输出 2-n 结果
    '''
    
'''
开始进行迭代，从2-n
'''

f.close();
fw.close();
