import pyodbc


server = 'quiz3.database.windows.net'
database = 'myDB'
username = 'chay2316'
password = 'cxv145..'

def databaseConnect():
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
    return cnxn
print("Database Connected")