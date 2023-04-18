import os , codecs , shutil
import argparse

projectName='精简IM'
schemes1='jingjian'
schemes2='jianjing'
new1=''
new2=''
new3=''

def replaceFileWord(dirPath ,fileName,tempfilePath):
    filePath = os.path.join(dirPath, fileName)
    tempFileName = "2-" + fileName
    tempPath = os.path.join(dirPath,tempFileName)
    # 先改名
    if os.path.exists(filePath):
        os.rename(filePath,tempPath)
    else:
        print('文件路径不存在' + filePath)
    # 创建原来的名字
    shutil.copyfile(tempfilePath,filePath)
    
    readF = open(tempPath)
    writeF = open(filePath,'w')
        
    while True:
        line :str = readF.readline()
        if line:
            newLine = line.replace(projectName,new1)
            newLine = newLine.replace(schemes1,new2)
            newLine = newLine.replace(schemes2,new3)
            writeF.write(newLine)
        else:
            break
    readF.close()
    writeF.close()
    os.remove(tempPath)
    print('替换文件'+ fileName+'完成....')

# 替代一个文件
def replaceSingleDir(dirPath,tempfilePath):
    allPath = os.listdir(dirPath)
    for fileName in allPath:
        currentPath = os.path.join(dirPath, fileName)
        if '.app' in fileName:
            continue
        if fileName == 'BUILD':
            replaceFileWord(dirPath,fileName,tempfilePath)
        if os.path.isdir(currentPath):
            replaceSingleDir( currentPath,tempfilePath)
        else:
            # 如果不是。string就跳过
            if '.strings' not in currentPath or fileName == 'empty.strings':
                continue
            replaceFileWord(dirPath,fileName,tempfilePath)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='replaceWord')

    parser.add_argument(
        '--projectName',
        required=True,
        help='项目名称',
        type=str
    )
    parser.add_argument(
        '--schemes1',
        required=True,
        help='schemes1',
        type=str
    )
    parser.add_argument(
        '--schemes2',
        required=True,
        help='schemes2',
        type=str
    )
    parser.add_argument(
        '--tempFilePath',
        required=True,
        help='临时文件绝对路径',
        metavar='path'
    )

    args = parser.parse_args()
    print('参数===',args)
    currentDirPath = os.getcwd() + '/Esayim'
    print('currentDirPath===',currentDirPath)
    new1 = args.projectName
    new2 = args.schemes1
    new3 = args.schemes2
    if len(new1) <= 0:
        print('请输入项目名称')
        exit()
    if len(new2) <= 0:
        print('请输入schemes1')
        exit()
    if len(new3) <= 0:
        print('请输入schemes2')
        exit()

    tempfilePath = args.tempFilePath
    if len(tempfilePath) <= 0:
        print('请输入临时文件绝对路径')
        exit()

    replaceSingleDir(currentDirPath,tempfilePath)

