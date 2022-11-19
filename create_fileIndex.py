import os,re
from itertools import groupby
from pprint import pprint

# 対象ディレクトリ、検索対象の定義
target = r'C:\\Users\\omron\\Documents\\24_Mkdocs\\omomuroni.github.io\\docs\\'
ptrn = re.compile(r"md")

path_list = [
    os.path.join(dirPath + os.sep + file)
    # os.path.abspath(file)　#でも可
    for dirPath, dirs, files in os.walk(target) 
    for file in files 
    if ptrn.search(file)
    ]

# .md ファイルのタイトルは必ず1行目に "# "で記述すること

indexDict_list = []
indexName_list = []

for path in path_list:
    with open(path, "r", encoding="utf-8") as f:
        titleName = (f.readline().rstrip()).replace("# ", "")
    folderName = ((path.replace(target,"")).split(os.sep))
    folderName.pop(-1)
    itemName   = ("_".join(folderName))
    if itemName not in indexName_list and itemName != "":
        indexName_list.append(itemName)
    if itemName != "":
        indexDict_list.append({itemName:[titleName,path]})


pathDict = {}
for i in indexName_list:
    pathDict[i] = []


# indexDict_list group化
for indexDict in indexDict_list:
    indexDict.get()

        # for i in indexName_list:
        #     if k == indexDict_list:
        #         pathDict[i].append(v)
                
# pprint(pathDict)