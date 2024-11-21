# pip install pyodbc
import pyodbc

# Define your Azure SQL connection details
server = 'your-server-name.database.windows.net'
database = 'your-database-name'
username = 'your-username'
password = 'your-password'  # Be cautious with storing passwords in code!
driver = '{ODBC Driver 17 for SQL Server}'  # Ensure the driver is installed

# Build the connection string
connection_string = f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}'

try:
    # Establish connection
    conn = pyodbc.connect(connection_string)
    print("Connection successful!")

    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()

    # Example: Fetch data from a table
    cursor.execute("SELECT TOP 10 * FROM your_table_name")
    for row in cursor.fetchall():
        print(row)

    # Close the connection
    cursor.close()
    conn.close()

except Exception as e:
    print("Error connecting to Azure SQL:", e)

