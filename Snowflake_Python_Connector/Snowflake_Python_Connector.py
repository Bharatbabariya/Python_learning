Firstly, it is very easy to use the Python connector in your application. You just have to set the login parameters with required credential details and you are good to go.

Following example demonstrates the usage of python connector to get current date.

import snowflake.connector

# Connectio string
conn = snowflake.connector.connect(
                user='snuser',
                password='password@123',
                account='xyz12345.us-east-2',
                #warehouse='COMPUTE_WH',
                database='DEMO_DB',
                schema='public'
                )

# Create cursor
cur = conn.cursor()

# Execute SQL statement
cur.execute("select current_date;")

# Fetch result
print cur.fetchone()[0]
Output:

You will get following output when you execute Python progam.

2019-12-13
