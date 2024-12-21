import ast
import pymysql
class Mysql(object):
    def __init__(self):
        try:
            self.db = pymysql.connect(
                host="localhost",
                user="root",
                password="Cjl202200202127==",
                database="bookstore")
            # 游标对象
            self.cursor = self.db.cursor()
            print("连接成功！")
        except:
            print("连接失败！")

    def login(self, username):
        self.cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)
        sql = 'SELECT * FROM users WHERE username = %s'
        self.cursor.execute(sql, (username))
        userinfo = self.cursor.fetchone()
        return userinfo

    def is_user_exist(self, username):
        sql = 'SELECT * FROM users WHERE username = %s'
        self.cursor.execute(sql, (username))
        results = self.cursor.fetchone()
        return results

    def register(self, username, password, type):
        sql = 'INSERT INTO users (username,password,type) VALUES(%s, %s, %s)'
        self.cursor.execute(sql, (username, password, type))

    # 查询数据函数
    def getdata(self):
        sql = "select * from books order by id"
        # 执行sql语句
        self.cursor.execute(sql)
        # 获取所有的记录
        results = self.cursor.fetchall()
        return results

    def search(self, find):
        print('find=' + find)
        args = '%' + find + '%'
        sql = "SELECT * FROM books WHERE CONCAT(ID,书名,作者,出版社,价格,数量,位置,简介) like '%s'" % args
        print('sql=' + sql)
        # 执行sql语句
        self.cursor.execute(sql)
        # 获取所有的记录
        results = self.cursor.fetchall()
        return results

    def search_by_id(self, id):
        sql = "SELECT * FROM books WHERE ID='%s'" % id
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results

    def delete(self, id):
        print('id=' + id)
        # data_tuple = ast.literal_eval(id)
        # ID=data_tuple[0]
        # print('ID='+ID)
        try:
            sql = "DELETE FROM books WHERE ID='%s'" % id
            print('sql=' + sql)
            self.cursor.execute(sql)
            self.db.commit()
            return True
        except Exception as e:
            return False

    def update(self, data):
        head = ['图片', '书名', '作者', '出版社', '价格', '数量', '位置', '简介']
        try:
            print(len(head))
            for i in range(len(head)):
                if len(data[i + 1]) == 0:
                    continue
                print('i:')
                print(i)
                sql = "UPDATE books SET " + head[i] + "=" + "'" + data[i + 1] + "'"
                sql = sql + ("WHERE ID='%s'" % data[0])
                print('sql=' + sql)
                self.cursor.execute(sql)
                self.db.commit()
            return True
        except Exception as e:
            return False

    def insert(self, data):
        head = ['ID', '图片', '书名', '作者', '出版社', '价格', '数量', '位置', '简介']
        try:
            sql = "SELECT MAX(CAST(ID AS UNSIGNED)) FROM books"
            print(sql)
            self.cursor.execute(sql)
            max_id = self.cursor.fetchone()
            print(max_id)
            if (max_id[0] == None):
                max_id = int(1)
            else:
                max_id = int(max_id[0]) + 1
            print('max_id=' + str(max_id))
            max_id = str(max_id)
            data.insert(0, max_id)
            sql = "INSERT INTO books ("

            for i in range(len(head)):
                if len(data[i]) == 0:
                    continue
                if i == 0:
                    sql = sql + head[i]
                else:
                    sql = sql + ',' + head[i]
            sql = sql + (") VALUES (")

            for i in range(len(data)):
                if len(data[i]) == 0:
                    continue
                if i == 0:
                    sql = sql + "'" + data[i] + "'"
                else:
                    sql = sql + ",'" + data[i] + "'"
            sql = sql + ")"
            print('sql=' + sql)
            self.cursor.execute(sql)
            self.db.commit()
            results = self.search_by_id(max_id)
            return results
        except Exception as e:
            return False

    # 关闭
    def __del__(self):
        self.db.close()
