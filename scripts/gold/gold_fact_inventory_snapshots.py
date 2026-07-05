from pathlib import Path
import duckdb

def main():
    # Define the path to the DuckDB database file
    script_dir = Path(__file__).resolve().parent
    db_path = r"C:\Users\araro\OneDrive\Desktop\Supply Chain Analytics\supply_chain_analytics.duckdb"
     

    # Connect to the DuckDB database
    conn = duckdb.connect(database=db_path)

    # Execute the query to create the gold_fact_inventory_snapshots table
    conn.execute("""
                CREATE OR REPLACE TABLE gold_fact_inventory_snapshots AS
                SELECT 
                    snapshot_date AS SnapshotDate,
                    location_id AS LocationID,
                    sku AS ProductSku,
                    on_hand_qty AS OnHandQuantity,
                 FROM silver__inventory_snapshots__lite;
    """)

  # Close the connection
    conn.close()

if __name__ == "__main__":
    main()
    print("✅ created gold_fact_inventory_snapshot.py executed successfully.")

