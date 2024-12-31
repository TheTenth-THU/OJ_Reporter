import re
import chardet

# 检测文件编码
with open('requirements.txt', 'rb') as file:
    raw_data = file.read()
    result = chardet.detect(raw_data)
    encoding = result['encoding']

# 使用检测到的编码读取文件
with open('requirements.txt', 'r', encoding=encoding) as file:
    lines = file.readlines()

# 使用 utf-8 编码写入文件
with open('requirements.txt', 'w', encoding='utf-8') as file:
    for line in lines:
        # 使用正则表达式匹配包名和版本号
        match = re.match(r'([a-zA-Z0-9_-]+)==([0-9.]+)', line)
        if match:
            file.write(f"{match.group(1)}=={match.group(2)}\n")
        else:
            # 如果没有版本号，则直接写入包名
            match = re.match(r'([a-zA-Z0-9_-]+)', line)
            if match:
                file.write(f"{match.group(1)}\n")