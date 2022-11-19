import re
from pprint import pprint


# 変数定義
# 対象ファイルの指定
target_file = r"C:\Users\omron\Documents\24_Mkdocs\omomuroni.github.io\docs\Linux\command1.md"
# 各見出しの正規表現定義
index2_ptrn = re.compile(r"^#{2}\s")
index3_ptrn = re.compile(r"^#{3}\s")
index4_ptrn = re.compile(r"^#{4}\s")
index5_ptrn = re.compile(r"^#{5}\s")


def create_index(target_file):
    indexList = [] #　ファイルから読み取った見出しを格納するリスト 
    result = [] # 整形した目次を格納するリスト
    
    # ファイルの読込み
    with open(target_file,"r", encoding="utf-8") as f:
        textline = f.readlines()
    # 見出しを抽出
    # TODO: 「## Page Index」の場合に無視するようにする
    # TODO: 辞書型に変更？
    for text in textline:
        if "## " in text:
            indexList.append(text.replace("\n",""))
    # 見出しを整形
    for index in indexList:
        if index2_ptrn.match(index):
            indexText = index2_ptrn.sub("",index)
            result.append(f"- [{indexText}](#{indexText})")
        elif index3_ptrn.match(index):
            indexText = index3_ptrn.sub("",index)
            result.append(f"  - [{indexText}](#{indexText})")
        elif index4_ptrn.match(index):
            indexText = index4_ptrn.sub("",index)
            result.append(f"    - [{indexText}](#{indexText})")
        elif index5_ptrn.match(index):
            indexText = index5_ptrn.sub("",index)
            result.append(f"      - [{indexText}](#{indexText})")
    
    #確認用
    print(result)
    return result


def output_result(result):
    with open("./pageIndex.md", "w",encoding="utf-8") as f:
        for i in result:
            f.write(f"{i}\n")



if __name__ == "__main__":
    output_result(create_index(target_file))
