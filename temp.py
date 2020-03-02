from flask import Flask, request, render_template
import pyodbc
from  timeit import timeit
from time import time
import redis
import os




# try:
#     conn = redis.StrictRedis(
#         host='yashazuredns.redis.cache.windows.net',
#         port=6380,
#         password='8gg7Xp3NAkiYo6g9tiKHcxhFNwSqefCf4aKt4mst1lE=',
#         ssl=True,)
#     print(conn)
#     conn.ping()
#     print('Connected!')
# except Exception as ex:
#     print('Error:', ex)
#     exit('Failed to connect, terminating.')


server = 'quiz3.database.windows.net'
database = 'myDB'
username = 'chay2316'
password = 'cxv145..'

cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';PORT=5000;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
print(cnxn)
print(os.getenv("PORT"))


app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('viewdb.html')

@app.route('/submit',methods = ['GET','POST'])
def submit():
    if request.method == 'POST':

        if request.form['submit_button'] == 'SUBMIT':
            # cursor.execute("SELECT TOP 20 pc.Name as CategoryName, p.name as ProductName FROM [SalesLT].[ProductCategory] pc JOIN [SalesLT].[Product] p ON pc.productcategoryid = p.productcategoryid")
            # cursor.execute("SELECT COUNT (*) FROM dbo.all_month")

            #tic = time()
            cursor.execute("SELECT * FROM [dbo].[QUAKES]")
            #toc = time()
            #print(toc - tic)

            data = cursor.fetchall()
            render_template('result.html', data=data)

if __name__ == '__main__':
    print("Main")
   
    app.run()
