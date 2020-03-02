"""Cloud Foundry test"""
from flask import Flask, request, render_template, send_from_directory
import os
from  timeit import timeit
from time import time
import os
from dbConnect import databaseConnect
from redisConnect import redisConnect
import random
import pickle

cnxn = databaseConnect()
cursor = cnxn.cursor()
redisO = redisConnect()


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('base.html')

@app.route('/submit',methods = ['POST'])
def submit():

    if request.method == 'POST':
        result = request.form 

        depth1 = str(result['depth1'])
        depth2 = str(result['depth2'])
        queries = int(result['queries'])
        timeR = 0
        timeS = 0
        
        if str(result['cache']) == "True":

            for x in range(queries):

                random1 = random.uniform(float(depth1),float(depth2))
                random2 = random.uniform(random1,float(depth2))
                t3 = time()
                if redisO.get(str(depth1)):
                    print("GOT IN CACHE")
                else:
                    tableData = cursor.execute('SELECT TIME, LATITUDE, LONGITUDE, DEPTHERROR FROM dbo.QUAKES WHERE DEPTHERROR > ? AND DEPTHERROR < ?', (random1,random2))
                    row = cursor.fetchone()
                    if row:
                        redisO.set(str(depth1), "Value")
                        print("DONE")
                    # else:
                    #     redisO.set(str(mag1), "NONE")
                    #     print("DONE with NONE")
                t4 = time()
                timeR = timeR + (t4 - t3)
                print("timeR : ",timeR)
                return "Time without cache is : " + str(timeR) 

        else:
            for x in range(queries):
                random1 = random.uniform(float(depth1),float(depth2))
                random2 = random.uniform(random1,float(depth2))
                t3 = time()
                
                tableData = cursor.execute('SELECT TIME, LATITUDE, LONGITUDE, DEPTHERROR FROM dbo.QUAKES WHERE DEPTHERROR > ? AND DEPTHERROR < ?', (str(random1),str(random2)))
                   
                t4 = time()
                timeR = timeR + (t4 - t3)
                print("timeR : ",timeR)
                return "Time with cache is : " + str(timeR) 

    return render_template('view.html', tableData = tableData) 

                



if __name__ == '__main__':
    print("Main")
   
    app.run()






    