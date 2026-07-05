from pathlib import Path
import duckdb

def main():
    # Define the path to the DuckDB database file
    script_dir = Path(__file__).resolve().parent
    db_path = r"C:\Users\araro\OneDrive\Desktop\Supply Chain Analytics\supply_chain_analytics.duckdb"
     

    # Connect to the DuckDB database
    conn = duckdb.connect(database=db_path)

    # Execute the query to create the gold_dim_product table
    conn.execute("""
                CREATE OR REPLACE TABLE gold_dim_product AS
                SELECT 
                    sku AS ProductSku,
                    product_name AS ProductName,
                    category AS ProductCategory,
                    brand AS Brand,
                    unit_cost AS UnitCost
                 FROM silver__product_master__lite;
    """)

  # Close the connection
    conn.close()

if __name__ == "__main__":
    main()
    print("✅ created gold_dim_product.py executed successfully.")

