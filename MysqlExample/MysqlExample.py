import pymysql

# 打开数据库连接
connection = pymysql.connect(host='localhost',
                             user='root',  # 填入用户名
                             password='xxxx',  # 填入密码
                             db='test',  # 需要连接的数据库
                             charset='utf8mb4',  # 指定数据集编码，很重要
                             cursorclass=pymysql.cursors.DictCursor)  # 这个也很有用，特别是从数据库中读数据的时候


# 查询
def select_table():
    cursor = connection.cursor()
    sql = "SELECT * FROM `user`"
    cursor.execute(sql)
    result = cursor.fetchall()
    print(result)


# 插入
def insert_table():
    try:
        cursor = connection.cursor()
        sql = "INSERT INTO `user`(`name`, age) VALUES('name', 20)"
        result = cursor.execute(sql)
        print("insert影响行数：%s" % result)
        connection.commit()
    except:
        print("执行sql失败")
        connection.rollback()


# 修改
def update_table():
    try:
        cursor = connection.cursor()
        sql = "UPDATE `user` SET age = 30 WHERE `name` = 'name'"
        result = cursor.execute(sql)
        print("update影响行数：%s" % result)
        connection.commit()
    except:
        print("执行sql失败")
        connection.rollback()


# 删除
def delete_table():
    try:
        cursor = connection.cursor()
        sql = "DELETE FROM `user` WHERE `name` = 'name'"
        result = cursor.execute(sql)
        print("delete影响行数：%s" % result)
        connection.commit()
    except:
        print("执行sql失败")
        connection.rollback()


if __name__ == '__main__':
    select_table()
    insert_table()
    update_table()
    delete_table()

    # 关闭数据库
    connection.close()
