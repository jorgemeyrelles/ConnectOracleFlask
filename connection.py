import os
import cx_Oracle
from dotenv import load_dotenv


load_dotenv()

user = os.getenv("USER")
password = os.getenv("PASSWORD")
cs = os.getenv("CS")
directory = os.getenv("ORACLE_CLIENT")


cx_Oracle.init_oracle_client(lib_dir=r"%s" % directory)

connection = cx_Oracle.connect(
    user=user,
    password=password,
    dsn=cs,
)

with connection.cursor() as cursor:
    for row in cursor.execute("SELECT owner, table_name FROM all_tables"):
        print(row)
