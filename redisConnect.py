import redis


server = 'quiz3.database.windows.net'
database = 'myDB'
username = 'chay2316'
password = 'cxv145..'
driver= '{ODBC Driver 13 for SQL Server}'

def redisConnect():
    try:
        conn = redis.StrictRedis(
            host='chayredis.redis.cache.windows.net',
            port=6380,
            password='HMcQ2qlUNhCHLS2jWKflvxB7y3R3x7JsOAsGUomlJBY=',
            ssl=True,)
        return conn
        conn.ping()
        print('Connected!')
    except Exception as ex:
        print('Error:', ex)
        exit('Failed to connect, terminating.')