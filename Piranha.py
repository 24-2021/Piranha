import chardet
import yaml
import sys

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
            content = file.read()
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


def get_code(file_path):
    encoding, confidence = detect_encoding(file_path)
    if encoding is not None:
        # print(f"检测到文件编码为 {encoding}，置信度为 {confidence}")
        return encoding
    else:
        print("该文件无法读取")
# code=get_code("G:\\tcsec-keeper\\sdk\\pom.xml" )

#正式读取全部
def file_name_list(txt):

        f = open(txt,encoding='utf-8')
        f = f.readlines()
        for path in f:
            try:
                path = path.strip('\n')
                code=get_code(path)
                content=read_file_all(path,code)  #组装
                poc_file = open('file_all.txt', 'a+')
                print("Read and write all successful")
                poc_file.write(content + '\n')
                poc_file.close()
            except:
                    print("读取异常")
                    continue
#正式读取全部
def file_name_list_check(txt):

        f = open(txt,encoding='utf-8')
        f = f.readlines()
        for path in f:
            try:
                path = path.strip('\n')
                code=get_code(path)
                content=read_file_all(path,code)  #组装
                for key in keys:
                # if  "jdbc:" in content or "redis" in content or "mysql" in content or "pgsql" in content or "postgresql" in content or "oracle" in content\
                #     or "oss." in content or "oss.accessKey" in content or "oss.secretKey" in content or "secretKey" in content or "accessKey" in content \
                #     or "ak" in content or "sk" in content  or "mongondb" in content or "secret" in content or "password" in content or "username" in content\
                #     or "pass" in content or "user" in content or "pwd" in content or "mail" in content or "smtp" in content or "token" in content or "token" in content\
                #     or "datasource" in content or "datasource" in content or "accessKeyId" in content or "accessKeySecret" in content or "sms" in content\
                #     or "access" in content or "access" in content or "mssql" in content or "sqlserver" in content or "aliyun" in content:
                    if key in content:
                        poc_file = open('file_filterate.txt', 'a+')
                        print("Read and write all check successful")
                        poc_file.write(content + '\n')
                        poc_file.close()
                        break
            except:
                    print("读取异常")
                    continue
def help():
    print("python Piranha.py path.txt")
    print("")
    print("Linux：")
    print("find / name *.config > path.txt")
    print("./Piranha path.txt")
    print("")
    print("Windows：")
    print("dir /s/b C:\*.config > path.txt")
    print("Piranha.exe path.txt")
    print("")
    print("build：")
    print("pyinsatller -F Piranha.py")

if __name__ == '__main__' :
    try:
        cmd1=sys.argv[1]
        file = file_name_list(cmd1)
        print(file)
        file1 = file_name_list_check(cmd1)
        print(file1)
    except:
        help()


