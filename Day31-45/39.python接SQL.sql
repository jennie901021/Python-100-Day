#Python程序接入MySQL数据库
"""
1.創建連接。 MySQL 服務器啟動後，提供了基於 TCP （傳輸控制協議）的網絡服務。我們可以通過pymysql模塊的connect函數連接 MySQL 服務器。在調用connect函數時，需要指定主機（host）、端口（port）
  、用戶名（user）、口令（password）、數據庫（database）、字符集（charset）等參數，該函數會返回一個Connection對象。
2.獲取游標。連接 MySQL 服務器成功後，接下來要做的就是向數據庫服務器發送 SQL 語句，MySQL 會執行接收到的 SQL 並將執行結果通過網絡返回。要實現這項操作，需要先通過連接對象的cursor方法獲取游標（Cursor）對象。
3.發出 SQL。通過游標對象的execute方法，我們可以向數據庫發出 SQL 語句。
4.如果執行insert、delete或update操作，需要根據實際情況提交或回滾事務。因為創建連接時，默認開啟了事務環境，在操作完成後，需要使用連接對象的commit
  或rollback方法，實現事務的提交或回滾，rollback方法通常會放在異常捕獲代碼塊except中。如果執行select操作，需要通過游標對象抓取查詢的結果，對應的方法有三個，分別是：fetchone、fetchmany和fetchall。
  其中fetchone方法會抓取到一條記錄，並以元組或字典的方式返回；fetchmany和fetchall方法會抓取到多條記錄，以嵌套元組或列表裝字典的方式返回。
5.關閉連接。在完成持久化操作後，請不要忘記關閉連接，釋放外部資源。我們通常會在finally代碼塊中使用連接對象的close方法來關閉連接。
"""
#插入数据
import pymysql

no = int(input('部门编号: '))
name = input('部门名称: ')
location = input('部门所在地: ')

# 1. 创建连接（Connection）
conn = pymysql.connect(host='127.0.0.1', port=3306,
                       user='guest', password='Guest.618',
                       database='hrs', charset='utf8mb4')
try:
    # 2. 获取游标对象（Cursor）
    with conn.cursor() as cursor:
        # 3. 通过游标对象向数据库服务器发出SQL语句
        affected_rows = cursor.execute(
            'insert into `tb_dept` values (%s, %s, %s)',
            (no, name, location)
        )
        if affected_rows == 1:
            print('新增部门成功!!!')
    # 4. 提交事务（transaction）
    conn.commit()
except pymysql.MySQLError as err:
    # 4. 回滚事务
    conn.rollback()
    print(type(err), err)
finally:
    # 5. 关闭连接释放资源
    conn.close()

#删除数据
import pymysql

no = int(input('部门编号: '))

# 1. 创建连接（Connection）
conn = pymysql.connect(host='127.0.0.1', port=3306,
                       user='guest', password='Guest.618',
                       database='hrs', charset='utf8mb4',
                       autocommit=True)
try:
    # 2. 获取游标对象（Cursor）
    with conn.cursor() as cursor:
        # 3. 通过游标对象向数据库服务器发出SQL语句
        affected_rows = cursor.execute(
            'delete from `tb_dept` where `dno`=%s',
            (no, )
        )
        if affected_rows == 1:
            print('删除部门成功!!!')
finally:
    # 5. 关闭连接释放资源
    conn.close()

#更新数据
import pymysql

no = int(input('部门编号: '))
name = input('部门名称: ')
location = input('部门所在地: ')

# 1. 创建连接（Connection）
conn = pymysql.connect(host='127.0.0.1', port=3306,
                       user='guest', password='Guest.618',
                       database='hrs', charset='utf8mb4')
try:
    # 2. 获取游标对象（Cursor）
    with conn.cursor() as cursor:
        # 3. 通过游标对象向数据库服务器发出SQL语句
        affected_rows = cursor.execute(
            'update `tb_dept` set `dname`=%s, `dloc`=%s where `dno`=%s',
            (name, location, no)
        )
        if affected_rows == 1:
            print('更新部门信息成功!!!')
    # 4. 提交事务
    conn.commit()
except pymysql.MySQLError as err:
    # 4. 回滚事务
    conn.rollback()
    print(type(err), err)
finally:
    # 5. 关闭连接释放资源
    conn.close()

#查询数据
import pymysql

# 1. 创建连接（Connection）
conn = pymysql.connect(host='127.0.0.1', port=3306,
                       user='guest', password='Guest.618',
                       database='hrs', charset='utf8mb4')
try:
    # 2. 获取游标对象（Cursor）
    with conn.cursor() as cursor:
        # 3. 通过游标对象向数据库服务器发出SQL语句
        cursor.execute('select `dno`, `dname`, `dloc` from `tb_dept`')
        # 4. 通过游标对象抓取数据
        row = cursor.fetchone()
        while row:
            print(row)
            row = cursor.fetchone()
except pymysql.MySQLError as err:
    print(type(err), err)
finally:
    # 5. 关闭连接释放资源
    conn.close()