import argparse
import mysql.connector

def run_sql_query(query_name, start_date, end_date, category):
    # Connect to MySQL database
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sharath@9224",
        database="terrapay"
    )
    cursor = db_connection.cursor()

    # Define the SQL queries
    sql_queries = {
        'demand': "SELECT * FROM terrapay WHERE Description = %s AND InvoiceDate BETWEEN %s AND %s;",
        # Add more SQL queries as needed
    }

    # Check if query_name exists
    if query_name not in sql_queries:
        print("Query name not recognized.")
        return

    # Execute the SQL query
    try:
        cursor.execute(sql_queries[query_name], (category, start_date, end_date))
        results = cursor.fetchall()
        for row in results:
            print(row)
    except mysql.connector.Error as err:
        print("Error executing SQL query:", err)
    finally:
        cursor.close()
        db_connection.close()

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Run SQL queries by name.")
    parser.add_argument("query_name", help="Name of the SQL query to run")
    parser.add_argument("start_date", help="Start date of the time window (YYYY-MM-DD)")
    parser.add_argument("end_date", help="End date of the time window (YYYY-MM-DD)")
    parser.add_argument("category", help="Category for the query")
    args = parser.parse_args()

    # Run the SQL query
    run_sql_query(args.query_name, args.start_date, args.end_date, args.category)
