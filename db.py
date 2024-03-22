from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://sql6693232:yDntHLHaqy@sql6.freesqldatabase.com/sql6693232?charset=utf8mb4")

# Define the query
query = text("SELECT * FROM employees")

# Execute the query
with engine.connect() as connection:
    result = connection.execute(query)
    for row in result:
        print(row)