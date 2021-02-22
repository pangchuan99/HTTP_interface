import os
from common.connect_mysql import select_sql,execute_sql #连接数据库的    select_sql  是查询数据库操作     execute_sql 是执行增删改操作
import pytest
import json
import yaml



def get_name0(sql0,wenjian0):
    '''
    通过查询数据库 写到文档里面
    :param sql0: 查询语句变量
    :param wenjian0: 编写文件变量名
    :return:
    '''
    a = select_sql(sql0)

    # #   W 是重写
    with open(r".\TestDatas\{}".format(wenjian0), "w",encoding="utf-8") as fp:
        fp.write("")
    # for i in a:
    #     c = (i["name"])
    #     # print("为1的{}".format(c))

    with open(r".\TestDatas\{}".format(wenjian0), "a",encoding="utf-8") as fp1:
        fp1.write(str(a))





def get_yaml_data(yamlpath):
    '''
    读取文件
    :param yamlpath: 读取
    :return:
    '''
    f = open(yamlpath, "r", encoding='utf-8')
    yamldata = f.read()
    print(yamldata)

    # a = [i for i in yamldata.split("\n")]
    # # print(a)

    return yamldata

def get_name_wenjianmingcheng(mingcheng):
    '''
    获取文件路径，在读取文件
    :param mingcheng: 文件名称变量
    :return:
    '''

    # 获取当前文件的上一层路径,上一层路径
    curpath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    print(curpath)
    # 然后在获取某一个文件的绝对路径
    yamlpath = os.path.join(curpath, "common",mingcheng)
    a1=get_yaml_data(yamlpath)
    #获取的文件里面内容是string类型 转成字典类型
    a3=yaml.load(a1,Loader=yaml.FullLoader)
    print(type(a3))

    return a3


if __name__ == '__main__':
    # get_name0()
    # get_name1()
    # pc=get_yaml_data()
    # # pc=get_name_wenjianmingcheng("get_name_tb_smzdzsqwenjian_0.yaml")
    # print(pc)
    # print(type(pc))
    # a3=yaml.load(pc)
    # print(type(a3))
    # print(pc["name"])
    curpath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    print(curpath)
    yamlpath = os.path.join(curpath, "common","connect_mysql")
    print(yamlpath)