import psycopg2 as db


connection = db.connect(host='localhost', port=5432, user='postgres',
                        password='1234', dbname='postgres')

cursor = connection.cursor()

query = "insert into reader (\"nchit\", \"fio\") VALUES(21, 'TM');"
cursor.execute(query)
# res = cursor.fetchall()

# print(res)
connection.commit()
