## 简介

在拿到webshell之后的收集该服务器上所有配置文件，极大节省了你手翻配置的时间，让你内网更快一步

## 版本

python >=3.1.x

Piranha=v0.1

## 安装

```
pip3 install -r re.txt
```

### 配置文件

config.yaml

![image-20230713092022703](https://github.com/mamba-2021/Piranha/assets/75511051/a89ee427-6b4c-4c57-9749-1c046496c330)


可以根据个人实战情况，进行修改字典

## 用法

### Windows

查找配置文件放到path.txt

```
dir /s/b C:\www\*.conf >path.txt  #这里配置文件后缀不仅限于conf，可根据实战环境进行搜索
```

进行搜索并且写入

```
Piranha_win_amd64.exe path.txt
```

查找完毕之后，会生成file_all.txt,file_filterate.txt；file_filterate.txt是根据字典过滤后的

![image-20230713091713413](https://github.com/mamba-2021/Piranha/assets/75511051/d3bbcf94-201a-447c-a4ac-461cfa57926c)


### Linux

查找配置文件放到path.txt

```
find /var/www/ -name *.conf >path.txt  #这里配置文件后缀不仅限于conf，可根据实战环境进行搜索
```

进行搜索并且写入

```
./Piranha_lin_amd64 path.txt
```

### 打包

```
pip3 install pyinstaller
pyinstaller -F Piranha.py
```
Linux：
![image](https://github.com/mamba-2021/Piranha/assets/75511051/fbee0b2f-6bca-412c-ae68-936466ecf8a8)


Windows：
![image](https://github.com/mamba-2021/Piranha/assets/75511051/46f52c1d-5488-48c3-bb75-b58e9ed008b7)


