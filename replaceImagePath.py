import os
from typing import List

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

# 修改一个文件
def changeSingleFile(basePath, dirPath, fileName, pathDict):
    if len(dirPath) > 0:
        fullPath = basePath + '/' + dirPath + '/' + fileName
        tempFileFullPath = basePath + '/' + dirPath + '/' + '副本' + fileName
    else:
        fullPath = basePath + '/' + fileName
        tempFileFullPath = basePath + '/' + '副本' + fileName
    
    if not os.path.exists:
        os.mknod(tempFileFullPath)

    readF = open(fullPath,mode='r', encoding='utf-8')
    writeF = open(tempFileFullPath,mode='w+', encoding='utf-8')
    
    print('正在替换文件',fileName,'....')
    while True:
        line :str = readF.readline()
        if line:
            lineString = str(line)
            for key in pathDict:
                if key in lineString:
                    oldImageNmae :str = key
                    newImageName = oldImageNmae[0] + 'ZesayIm/Legacy/' + oldImageNmae[1:]
                    lineString = lineString.replace(key,newImageName)
            writeF.write(lineString)
        else:
            break
    readF.close()
    writeF.close()
    os.remove(fullPath)
    os.rename(tempFileFullPath, fullPath)
    print('替换',fileName,'完成....')

# 遍历一个文件夹
def lookSingleDir(basePath, dirPath, pathDict):
    
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
                changeSingleFile(basePath,dirPath,fileName,pathDict)


def writeToFile(array, path):
    if not os.path.exists(path):
        print('写入文件不存在')
        return
    writeF = open(path,'w')
    for line in array:
        writeF.write(line + '\n')
    writeF.close()
        

if __name__ == '__main__':
    basePath = os.getcwd()
    # 获得图片路经名字
    imageBasePath = os.path.join(basePath,'submodules/TelegramUI/Images.xcassets')
    paths = getImagePath(imageBasePath,'',[])
    tempImagePathFile = os.path.join(basePath,'pathImage.txt')
    writeToFile(paths, tempImagePathFile)
    print('获取图片路经完成...')
    pathDict = {}
    # 初始化字典
    for path in paths:
        pathDict.setdefault(path, 0)
    
    lookSingleDir(basePath,'',pathDict)

    print('替换完成...')
   
