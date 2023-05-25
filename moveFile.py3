import os, shutil
from typing import List, Optional

def removeFile(baseFolder :Optional[str] = os.getcwd(), nameList :List[List[str]] = [], newFolderName :str = '',oldFolderPathWithBasePath :str = None):
    
    folderPath = os.path.join(baseFolder,newFolderName)
    if os.path.exists(folderPath) == False:
        os.mkdir(folderPath)
    if oldFolderPathWithBasePath:
        oldListDir = os.path.join(baseFolder,oldFolderPathWithBasePath)
    else:
        oldListDir = baseFolder
    allFileName = os.listdir(path=oldListDir)
    
    for fileName in allFileName:
        for dayIndex, dayNameList in enumerate(nameList, start=1):
            for numberIndex, subName in enumerate(dayNameList, start=1):

                temp = subName.split('. ')
                if len(temp) == 2:
                    subName = temp[1]
                
                if subName in fileName:
                    newName = str(dayIndex) + '-' + str(numberIndex) + '-' + subName
                    if os.path.exists(fileName):
                        os.rename(fileName, newName)
                    filePath = os.path.join(baseFolder, newName)
                    # newPath = os.path.join(filePath, folderPath)
                    if os.path.exists(filePath):
                        shutil.move(filePath, folderPath)
                    print('移动==='+ fileName)

array = [
         ['1480. 一维数组的动态和','724. 寻找数组的中心下标'],
         ['205. 同构字符串','392. 判断子序列'],
         ['21. 合并两个有序链表','206. 反转链表'],
         ['876. 链表的中间结点','142. 环形链表 II'],
         ['121. 买卖股票的最佳时机','409. 最长回文串'],
         ['589. N 叉树的前序遍历','102. 二叉树的层序遍历'],
          ['704. 二分查找','278. 第一个错误的版本'],
          ['98. 验证二叉搜索树','235. 二叉搜索树的最近公共祖先'],
          ['733. 图像渲染','200. 岛屿数量'],
          ['509. 斐波那契数','70. 爬楼梯'],
          ['746. 使用最小花费爬楼梯','62. 不同路径'],
          ['438. 找到字符串中所有字母异位词','424. 替换后的最长重复字符'],
          ['1. 两数之和','299. 猜数字游戏'],
          ['844. 比较含退格的字符串','394. 字符串解码'],
          ['1046. 最后一块石头的重量','692. 前K个高频单词']
          ]
removeFile(nameList=array,newFolderName= "Level1", oldFolderPathWithBasePath="Level1")

