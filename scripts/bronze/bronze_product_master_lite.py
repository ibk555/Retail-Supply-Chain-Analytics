from pathlib import Path
import duckdb

def main():
    # Define the path to the DuckDB database file
    script_dir = Path(__file__).resolve().parent
    db_path = r"C:\Users\araro\OneDrive\Desktop\Supply Chain Analytics\supply_chain_analytics.duckdb"

    # Connect to the DuckDB database
    conn = duckdb.connect(database=db_path)

    # Execute the query to create the bronze__product_master__lite table
    conn.execute("""
                CREATE OR REPLACE TABLE bronze__product_master__lite
                 AS
                SELECT 
                    sku,
                    product_name,
                    category,
                    brand,
                    unit_cost
                FROM raw__product_master__lite;
    """)

    # Close the connection
    conn.close()

if __name__ == "__main__":
    main()
    print("✅ created bronze__product_master__lite.py executed successfully.")