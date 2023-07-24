import chardet
import yaml
import sys
from cprint import cprint

#读取配置文件
def read_config_file(config_file):
    with open(config_file, 'r') as file:
        config = yaml.safe_load(file)
    return config


def check_files_for_keywords(config):
    keywords = config['Keywords']
    return keywords

# 用法示例
config_file = 'config.yaml'  # 替换为你的配置文件路径
config = read_config_file(config_file)
keys=check_files_for_keywords(config)



#读取文件内容的函数
def read_file_all(file_path,code):
    try:
        with open(file_path, 'r',encoding=code) as file:
            content = file.readlines()
        return content
    except FileNotFoundError:
        return "文件未找到"
    except IOError:
        return "读取文件时发生错误"


#获取文件的编码方式的函数
def detect_encoding(file_path):
    try:
        with open(file_path, 'rb') as file:
            raw_data = file.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
        confidence = result['confidence']
        return encoding, confidence
    except FileNotFoundError:
        return None, "文件未找到"
    except IOError:
        return None, "读取文件时发生错误"
    except Exception:
        return None,"获取编码异常"


def get_code(file_path):
    encoding, confidence = detect_encoding(file_path)
    if encoding is not None:
        # print(f"检测到文件编码为 {encoding}，置信度为 {confidence}")
        return encoding
    else:
        cprint.fatal("该文件无法读取")
        # print("该文件无法读取")
# code=get_code("G:\\tcsec-keeper\\sdk\\pom.xml" )

#获取编码格式并且将读取的文件转换成utf-8

#正式读取全部
def file_name_list(txt):
        f = open(txt)
        f = f.readlines()
        for path in f:
                try:
                    path = path.strip('\n')
                    code=get_code(path) #获取编码格式
                    content=read_file_all(path,code)  #组装
                    for con in content:
                        poc_file = open('file_all.txt', 'a+')
                        cprint.info(f"Read and write {path} all successful")
                        # print(f"Read and write {path} all successful")
                        poc_file.write(con + '\n')
                        poc_file.close()
                except:
                        print("读取异常")
                        continue
#正式读取全部
def file_name_list_check(txt):

        f = open(txt)
        f = f.readlines()
        for path in f:
            try:
                path = path.strip('\n')
                code=get_code(path)

                content=read_file_all(path,code)  #组装
                for con in content:  #遍历我们读取的文件
                    for key in keys: #遍历我们config.yaml
                        if key in con:
                            poc_file = open('file_filterate.txt', 'a+')
                            cprint.ok(f"Read and write {path} all check successful")
                            # print(f"Read and write {path} all check successful")
                            poc_file.write(con + '\n')
                            poc_file.close()
                            break
            except:
                cprint.fatal("读取异常")
                # print("读取异常")
                continue
def help():
    cprint.err("python Piranha.py path.txt")
    cprint.err("")
    cprint.err("Linux：")
    cprint.err("find / name *.config > path.txt")
    cprint.err("./Piranha path.txt")
    cprint.err("")
    cprint.err("Windows：")
    cprint.err("dir /s/b C:\*.config > path.txt")
    cprint.err("Piranha.exe path.txt")
    cprint.err("")
    cprint.err("build：")
    cprint.err("pyinsatller -F Piranha.py")

if __name__ == '__main__' :
    try:
        cmd1=sys.argv[1]
        file = file_name_list(cmd1)
        cprint.err(file)
        file1 = file_name_list_check(cmd1)
        cprint.err(file1)
    except:
        help()

