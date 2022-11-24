import sqlite3

conn = sqlite3.connect("test.db")  # 打开或创建数据库文件

print("Opened database successfully!")

c = conn.cursor()  # 获取游标

#建表
# sql = '''
#     create table company
#         (id int primary key not null,
#         name text not null,
#         age int not null,
#         address char(50),
#         salary real
#         )
# '''

# c.execute(sql)
# conn.commit()
# conn.close()

#插入
sql1 = '''
    insert into company (id,name,age,address,salary)
    values(1,'张三',32,"成都",8000)
    values (2,'李四',30,"重庆",14000)
'''

#查询
sql2 = "select id,name,address,salary from company"
cursor = c.execute(sql2)

for row in cursor:
    print("id = ",row[0])
    print("name = ",row[1])
    print("address = ",row[2])
    print("salary = ",row[3])

conn.commit()
conn.close()
