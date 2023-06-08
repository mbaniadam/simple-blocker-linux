import psycopg2
import datetime
import os

db_name = "wgpeers"
table_name = "users"
db_host = "127.0.0.1"
db_port =  5432
cnx = psycopg2.connect(database=db_name,
                        host=db_host,
                        user="postgres",
                        password="pgmor@1010",
                        port=db_port)
cursor = cnx.cursor()


#cursor.execute(f"SELECT * FROM {table_name}")
#selected = cursor.fetchall()
cursor.execute(f"select username, ip_address, expire_date, created_date from users ")
selected = cursor.fetchall()

for i in selected:
    print(i)
    userIP = i[1]
    userAge = i[2] - i[3]
    print(userAge.days)

    if userAge.days <= 0:
        print("user expired!")
        #os.system(f"sudo ufw deny from {userIP}")