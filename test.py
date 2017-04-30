# encoding:utf-8

import re

match={}
resultPath="/home/carson/Documents/结果.txt"

def Comment(text):
    with open(text,'r') as file:
        comment = file.read()
        return comment

comments = Comment('/home/carson/Documents/太空旅客.txt')

def Operate(text):
    with open(text) as readFile:
        for line in readFile.readlines():
            line = line.strip('\n')
            results = re.findall(line, comments)
            number = len(results)
            match[line] = number
    with open(resultPath, 'a') as writeFile:
        for line in match:
            writeFile.write(str(match[line]))
            writeFile.write(' ')
            writeFile.write(line)
            writeFile.write('\n')

Operate("/home/carson/Documents/词典/主题/主题.txt")
Operate("/home/carson/Documents/词典/主题/题材内容.txt")
Operate("/home/carson/Documents/词典/主题/风格.txt")
Operate("/home/carson/Documents/词典/制作/出品公司.txt")
Operate("/home/carson/Documents/词典/制作/制作.txt")
Operate("/home/carson/Documents/词典/制作/导演.txt")
Operate("/home/carson/Documents/词典/制作/编剧.txt")
Operate("/home/carson/Documents/词典/剧情/剧情.txt")
Operate("/home/carson/Documents/词典/剧情/发展.txt")
Operate("/home/carson/Documents/词典/剧情/开头.txt")
Operate("/home/carson/Documents/词典/剧情/泪点.txt")
Operate("/home/carson/Documents/词典/剧情/笑点.txt")
Operate("/home/carson/Documents/词典/剧情/结局.txt")
Operate("/home/carson/Documents/词典/视听/动作.txt")
Operate("/home/carson/Documents/词典/视听/画面.txt")
Operate("/home/carson/Documents/词典/视听/视听.txt")
Operate("/home/carson/Documents/词典/视听/镜头.txt")
Operate("/home/carson/Documents/词典/视听/音乐.txt")
Operate("/home/carson/Documents/词典/角色/反派.txt")
Operate("/home/carson/Documents/词典/角色/女主角.txt")
Operate("/home/carson/Documents/词典/角色/男主角.txt")
Operate("/home/carson/Documents/词典/角色/角色.txt")
Operate("/home/carson/Documents/词典/角色/角色中的其他.txt")
Operate("/home/carson/Documents/词典/角色/配角.txt")