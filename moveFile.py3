import os, shutil
from typing import List

def removeFile(nameList :List[str], newFolder :str):
    basePath = os.getcwd()
    folderPath = os.path.join(basePath,newFolder)
    if os.path.exists(folderPath) == False:
        os.mkdir(folderPath)
    
    allFileName = os.listdir()
    
    index = 1
    for subName in nameList:
        for fileName in allFileName:
            if subName in fileName:
                newName = str(index) + '-' + fileName
                os.rename(fileName, newName)
                filePath = os.path.join(basePath, newName)
                # newPath = os.path.join(filePath, folderPath)
                shutil.move(filePath, folderPath)
                print('移动==='+ fileName)
                index += 1
        

array = ["快乐数","螺旋矩阵","球会落何处","最长公共前缀",'字符串相乘','删除链表的倒数第 N 个结点','回文链表','奇偶链表',
         '排序链表','连接两字母单词得到的最长回文串','任务调度器','翻转二叉树','平衡二叉树',
         '二叉树的直径','路径总和 III','搜索旋转排序数组','搜索二维矩阵','将有序数组转换为二叉搜索树','二叉搜索树中第K小的元素','二叉搜索树迭代器']
removeFile(array, "Level2")

