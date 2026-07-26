import pyodbc
def get_connection():
    connection = pyodbc.connect(
    r"DRIVER={ODBC Driver 17 for SQL Server};"
    r"SERVER=PRAHARSHHITH\MSSQL;"
    r"DATABASE=ecommerce;"
    r"Trusted_Connection=yes;"
)
    return connection
