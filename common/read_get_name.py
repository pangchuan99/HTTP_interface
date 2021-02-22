
# -*- coding: utf-8 -*-
import os

def get_yaml_data(yamlpath):
    f = open(yamlpath, "r", encoding='utf-8')
    yamldata = f.read()
    print(yamldata)
    a = [i for i in yamldata.split("\n")]
    # print(a)

    return a



if __name__ == '__main__':
    # 获取当前文件的上一层路径,上一层路径
    curpath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    print(curpath)
    #然后在获取某一个文件的绝对路径
    yamlpath = os.path.join(curpath,"TestDatas","get_namelqk1.txt")
    print("文件{}".format(yamlpath))
    a=get_yaml_data(yamlpath)
    print("获取到的信息",a)


