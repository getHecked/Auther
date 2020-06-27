import io
import os
import urllib.request
from flask import *
from werkzeug.utils import secure_filename
from random import randint
import sqlite3
from sqlite3 import Error

conn = None
try:
    conn = sqlite3.connect("information")
    print(sqlite3.version)
except Error as e:
    print(e)


app = Flask(__name__)


@app.route('/first_auth',methods=['POST'])
def first_auth(token):
    time = time.time()
    otp = ''
    sql = ''' INSERT INTO codes (time,username,otp) VALUES(?,?,?) '''
    for _ in range(6):
        otp += randint(0, 10)
    temp_values = (time,token,otp)
    cur = conn.cursor()
    cur.execute(sql, temp_values)


if __name__ == "__main__":
    app.run()
