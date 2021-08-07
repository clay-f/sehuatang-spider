import pyodbc
import datetime

# Specifying the ODBC driver, server name, database, etc. directly
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost;DATABASE=scrapy;UID=sa;PWD=.')

# Create a cursor from the connection
cursor = cnxn.cursor()

result = cursor.execute(r"insert into sehua(title, url, created_at) values(?, ?, ?)", 'foo', 'bar', datetime.datetime.now())
cursor.commit()