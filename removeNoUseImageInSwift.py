import os , shutil
from typing import List
from collections import defaultdict

# 获取图片名字返回名字数组
def getImagePath(basePath, dirPath, pathList) -> List[str]:
    if len(dirPath) > 0:
        imagesPath = os.path.join(basePath, dirPath)
    else:
        imagesPath = basePath
    allPath: List[str] = os.listdir(imagesPath)
    for fileName in allPath:
        currentDirPath = os.path.join(dirPath, fileName)
        fullPath = os.path.join(basePath, currentDirPath)
        if 'ZesayIm' in fileName:
            continue
        # 如果是.imageset 直接加入
        if fileName.endswith('.imageset'):
            imageName = '"' + currentDirPath.replace('.imageset','') + '"'
            pathList.append(imageName)
            continue
        # 如果是文件夹
        if os.path.isdir(fullPath):
            getImagePath(basePath, currentDirPath, pathList)
    return pathList

# 读取一个文件
def readSingleFile(basePath, dirPath, fileName, pathDict) -> defaultdict:
    if len(dirPath) > 0:
        fullPath = basePath + '/' + dirPath + '/' + fileName
    else:
        fullPath = basePath + '/' + fileName
    readF = open(fullPath, encoding='utf-8')
    print('正在读取文件',fileName,'....')
    while True:
        line :str = readF.readline()
        if line:
            lineString = str(line)
            for key in pathDict:
                if key in lineString:
                    pathDict[key] += 1
        else:
            break
    readF.close()
    print('读取',fileName,'完成....')
    return pathDict
# 遍历一个文件夹
def lookSingleDir(basePath, dirPath, pathDict) -> defaultdict:
    
    allPath :List[str] = os.listdir(os.path.join(basePath, dirPath))
    for fileName in allPath:
        currentPath = os.path.join(dirPath, fileName)
        # 如果是.xcassets 直接跳过
        if fileName.endswith('.xcassets') or fileName.endswith('.imageset'):
            continue
        # 如果是文件夹
        fullPath = os.path.join(basePath,currentPath)
        if os.path.isdir(fullPath):
            lookSingleDir(basePath, currentPath, pathDict)
        else:
            # 如果是文件
            if fullPath.endswith('.swift'):
                pathDict = readSingleFile(basePath,dirPath,fileName,pathDict)
    return pathDict

def writeToFile(array, path):
    if not os.path.exists(path):
        os.mknod(tempImagePathFile)
        print('写入文件不存在')
    writeF = open(path,'w+')
    for line in array:
        writeF.write(line + '\n')
    writeF.close()

if __name__ == '__main__':
    basePath = os.getcwd()
    # 获得图片路经名字
    imageBasePath = os.path.join(basePath,'submodules/TelegramUI/Images.xcassets')
    paths = getImagePath(imageBasePath,'',[])
    print('获取图片路经完成...')
    pathDict = {}
    # 初始化字典
    for path in paths:
        pathDict.setdefault(path, 0)
    pathDict = lookSingleDir(basePath,'',pathDict)
    print('编号完成...')
    # 创建临时文件，放没有使用的照片
    noUseImagePath = os.path.join(basePath,'TempNoUseImages')
    if os.path.exists(noUseImagePath) == False:
        os.mkdir(noUseImagePath)
    
    noUseArray = list()
    for key in pathDict:
        if pathDict[key] == 0:
            # 这些初步认为是没有用到的图片
            noUseArray.append(key)
            imageName = str(key).replace('"','')
            fullPath = os.path.join(imageBasePath, imageName) + '.imageset'
            toPath = os.path.join(noUseImagePath, imageName) + '.imageset'
            if os.path.exists(fullPath):
                shutil.move(fullPath,toPath)
    print('移除完成...')
    tempImagePathFile = os.path.join(basePath,'pathImage.txt')
    writeToFile(noUseArray, tempImagePathFile)
    print('未使用的图片名字写入txt完成...')
            
        
