import pyodbc

conn_str = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=34.95.175.50,1433;"
    "UID=sqlserver;"
    "PWD=Dibai@Sales2025;"
    "DATABASE=melhorlead;"
    "TrustServerCertificate=yes;"
)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()
cursor.execute("SELECT GETDATE()")
print(cursor.fetchone())
conn.close()