import os
import sys
import cx_Oracle
from flask import Flask, request
from dotenv import load_dotenv

load_dotenv()

user = os.getenv("USER")
password = os.getenv("PASSWORD")
cs = os.getenv("CS")
directory = os.getenv("ORACLE_CLIENT")


cx_Oracle.init_oracle_client(lib_dir=r"%s" % directory)


def init_session(connection, requestedTag_ignored):
    cursor = connection.cursor()
    cursor.execute(
        """ALTER SESSION SET
          TIME_ZONE = 'UTC'
          NLS_DATE_FORMAT = 'DD-MM-YYYY HH24:MI'"""
    )

def start_pool():
    pool_min = 4
    pool_max = 4
    pool_inc = 0
    pool_gmd = cx_Oracle.SPOOL_ATTRVAL_WAIT

    print("Connecting by SERVICE NAME")

    pool = cx_Oracle.SessionPool(
        user=user,
        password=password,
        dsn=cs,
        min=pool_min,
        max=pool_max,
        increment=pool_inc,
        threaded=True,
        getmode=pool_gmd,
        sessionCallback=init_session
    )

    return pool


def create_schema():
    connection = pool.acquire()
    cursor = connection.cursor()
    cursor.execute("SELECT owner, table_name FROM all_tables")


app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, world!"

# localhost:3000/report?init='2022-11-01'&final='2022-12-01'
@app.route('/report', methods=['GET'])
def show_values():
    args = request.args
    init = args.get('init')
    final = args.get('final')
    connection = pool.acquire()
    cursor = connection.cursor()
    cursor.execute("query of report", [init, final])
    r = cursor.fetchone()
    return r[0]


if __name__ == '__main__':
    pool = start_pool()

    # if it does not exist table in DB
    create_schema()

    app.run(port=int(os.environ.get('PORT', 3000)))

