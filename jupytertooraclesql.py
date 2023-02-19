import cx_Oracle

# You should enter DSN,Username and Password information

dsn = "dsn_name"
username = "user_name"
password = "password"

# Connect Oracle Sql Dataframe
conn = cx_Oracle.connect(username, password, dsn)

# Control the connection
print(conn.version)

# Create cursor
cursor = conn.cursor()

# At this point, you should write a query that returns the information you need.
query = "SELECT * FROM CST_CUSTOMER"

# Run the query and get the results
cursor.execute(query)
results = cursor.fetchall()

# Print the results to the screen
for result in results:
    print(result)

# First close the cursor, then the connection
cursor.close()
conn.close()
