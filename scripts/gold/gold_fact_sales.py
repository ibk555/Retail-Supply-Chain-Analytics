from pathlib import Path
import duckdb

def main():
    # Define the path to the DuckDB database file
    script_dir = Path(__file__).resolve().parent
    db_path = r"C:\Users\araro\OneDrive\Desktop\Supply Chain Analytics\supply_chain_analytics.duckdb"
     

    # Connect to the DuckDB database
    conn = duckdb.connect(database=db_path)

    # Execute the query to create the gold_fact_sales table
    conn.execute("""
                CREATE OR REPLACE TABLE gold_fact_sales AS
                SELECT 
                    transaction_id AS SalesTransactionID,
                    transaction_date AS SalesDate,
                    sku AS ProductSku,
                    location_id AS LocationID,
                    qty AS Quantity,
                    unit_price AS UnitPrice,
                FROM silver__sales_transactions__lite;
    """)

  # Close the connection
    conn.close()

if __name__ == "__main__":
    main()
    print("✅ created gold_fact_sales.py executed successfully.")

