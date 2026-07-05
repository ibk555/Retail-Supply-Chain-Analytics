from pathlib import Path
import duckdb

def main():
    # Define the path to the DuckDB database file
    script_dir = Path(__file__).resolve().parent
    db_path = r"C:\Users\araro\OneDrive\Desktop\Supply Chain Analytics\supply_chain_analytics.duckdb"

    # Connect to the DuckDB database
    conn = duckdb.connect(database=db_path)

    # Execute the query to create the silver__product_master__lite table
    conn.execute("""
                CREATE OR REPLACE TABLE silver__product_master__lite
                 AS
                SELECT 
                    UPPER(TRIM(sku)) AS sku,
                    TRIM(product_name) AS product_name,
                    TRIM(category) AS category,
                    TRIM(brand) AS brand,
                    unit_cost
                FROM bronze__product_master__lite;
    """)

    # Close the connection
    conn.close()

if __name__ == "__main__":
    main()
    print("✅ created silver__product_master__lite.py executed successfully.")