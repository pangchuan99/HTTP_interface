import pymysql

#pip install PyMySQL==0.9.3


'''连接数据库的 host 主机ip   
               user  账号
               password  密码
               port  端口号'''
dbinfo = {
    "host": "20.20.20.42",
    "user": "root",
    "password": "123456aA",
    "port": 7806}

class DbConnect():
    '''database数据库名称'''
    def __init__(self, db_cof, database=""):
        self.db_cof = db_cof
        # 打开数据库连接
        self.db = pymysql.connect(database=database,
                                  #'''读取出来是元组，所以进行了转换成字典'''
                                  cursorclass=pymysql.cursors.DictCursor,**db_cof)

        # 使用cursor()方法获取操作游标----相当于点击激活的意思
        self.cursor = self.db.cursor()

    def select(self, sql):
        # SQL 查询语句
        # sql = "SELECT * FROM EMPLOYEE \
        #        WHERE INCOME > %s" % (1000)

        #通过建立的游标进行查询
        self.cursor.execute(sql)
        #结果
        results = self.cursor.fetchall()
        return results

    def execute(self, sql):
        # SQL 删除、提交、修改语句
        # sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20)
        try:
           # 执行SQL语句
           self.cursor.execute(sql)
           # 提交修改
           self.db.commit()
        except:
           # 发生错误时回滚
           self.db.rollback()

    def close(self):
        # 关闭连接
        self.db.close()

def select_sql(select_sql):
    '''查询数据库'''
    db = DbConnect(dbinfo, database="gsm")
    result = db.select(select_sql)  # 查询
    db.close()
    return result

def execute_sql(insert_sql):
    '''执行sql'''
    db = DbConnect(dbinfo, database="gsm")
    db.execute(insert_sql)  # 查询
    db.close()


if __name__ == '__main__':
    sql = 'SELECT DISTINCT a1.name FROM item_uri a1 INNER JOIN item_property a2 on a1.guid=a2.guid  INNER JOIN remote a3 on a2.version=a3.version  and a1.type="ZSB_PT3" AND a1.region="01eaa630-fb88-11e9-9dda-eb6203b0a61e"  AND a2.version=1'
    a = select_sql(sql)
    # print(a)
    # # print(a[1]['name'])
    for i in a:
        c=(i["name"])
        print(c)

    # insert_sql = '''INSERT INTO `apps`.`apiapp_card`
    # (`id`, `card_id`, `card_user`, `add_time`)
    # VALUES ('2', '', 'test123', '2019-12-17');
    # '''
    # execute_sql(insert_sql)
    #
