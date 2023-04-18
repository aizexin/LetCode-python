import os , codecs , shutil
import argparse

def replaceFileWord(oldWord, newWord ,dirPath ,fileName,tempfilePath):
    filePath = os.path.join(dirPath, fileName)
    tempFileName = "2-" + fileName
    tempPath = os.path.join(dirPath,tempFileName)
    # 先改名
    if os.path.exists(filePath):
        os.rename(filePath,tempPath)
    else:
        print('文件路径不存在' + filePath)
    # 创建原来的名字
    # file = os.getcwd()
    # if not os.path.exists(file + fileName):
        # os.makedirs(filePath, mode=0o777)
    shutil.copyfile(tempfilePath,filePath)
    
    readF = open(tempPath)
    writeF = open(filePath,'w')
        
    while True:
        line :str = readF.readline()
        if line:
            newLine = line.replace(oldWord,newWord)
            writeF.write(newLine)
        else:
            break
    readF.close()
    writeF.close()
    os.remove(tempPath)
    print('替换文件'+ fileName+'完成....')

# 替代一个文件
def replaceSingleDir(oldWord, newWord,dirPath,tempfilePath):
    allPath = os.listdir(dirPath)
    for fileName in allPath:
        currentPath = os.path.join(dirPath, fileName)
        if '.app' in fileName:
            continue
        if os.path.isdir(currentPath):
            replaceSingleDir(oldWord,newWord, currentPath,tempfilePath)
        else:
            # 如果不是。string就跳过
            if '.strings' not in currentPath or fileName == 'empty.strings':
                continue
            replaceFileWord(oldWord,newWord,dirPath,fileName,tempfilePath)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='replaceWord')
    parser.add_argument(
        '--oldWord',
        required=False,
        help='要被替换的',
        type=str
        # metavar='path'
    )
    parser.add_argument(
        '--newWord',
        required=False,
        help='新替换的',
        type=str
    )
    parser.add_argument(
        '--newWord2',
        required=False,
        help='新替换的2',
        type=str
    )
    parser.add_argument(
        '--tempFilePath',
        required=False,
        help='Use custom bazel user root (useful when reproducing a build)',
        metavar='path'
    )

    args = parser.parse_args()
    print('参数===',args)
    currentDirPath = os.getcwd() + ''
    print('currentDirPath===',currentDirPath)
    old = args.oldWord
    new = args.newWord
    new2 = args.newWord2
    tempfilePath = args.tempFilePath

    replaceSingleDir('精简IM',new,currentDirPath,tempfilePath)
    replaceSingleDir('jianjin',new2,currentDirPath,tempfilePath)
