from contextlib import contextmanager
from flask import Flask
from cfenv import AppEnv
import pyodbc
import os
import sys

app = Flask(__name__)

# Get port from environment variable or choose 9099 as local default
port = int(os.getenv("PORT", 9099))

@app.route('/')
def hello_world():
    with get_cursor(get_connection_string()) as cursor:
        cursor.execute("SELECT @@version;")
        row = cursor.fetchone()
        result = ''
        while row: 
            result = result + str(row[0]) + "<br/>"
            row = cursor.fetchone()

    return (str(os.getenv("PATH")) + "<br/>" +
            str(os.getenv("ODBCSYSINI")) + "<br/>" +
            str(os.getenv("LD_LIBRARY_PATH")) + "<br/>" +
            str(os.getenv("LIBRARY_PATH")) + "<br/>" +
            result)

@contextmanager
def get_cursor(connection_string, commit=False):
    connection = pyodbc.connect(connection_string)
    cursor = connection.cursor()
    try:
        yield cursor
    except pyodbc.DatabaseError as err:
        error, = err.args
        sys.stderr.write(error.message)
        cursor.execute("ROLLBACK")
        raise err
    else:
        if commit:
            cursor.execute("COMMIT")
        else:
            cursor.execute("ROLLBACK")
    finally:
        connection.close()

def get_connection_string():
    env = AppEnv()
    mssql = env.get_service(name='mssql-service')
    server = 'tcp:' + mssql.credentials['server']
    database = mssql.credentials['database']
    username = mssql.credentials['username']
    password = mssql.credentials['password']
    return 'DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password

if __name__ == '__main__':
    # Run the app, listening on all IPs with our chosen port number
    app.run(host='0.0.0.0', port=port)
