from pathlib import Path
import duckdb

def main():
    # Define the path to the DuckDB database file
    script_dir = Path(__file__).resolve().parent
    db_path = r"C:\Users\araro\OneDrive\Desktop\Supply Chain Analytics\supply_chain_analytics.duckdb"

    # Connect to the DuckDB database
    conn = duckdb.connect(database=db_path)

    # Execute the query to create the silver
    # __inventory_snapshots__lite table
    conn.execute("""
                CREATE OR REPLACE TABLE silver__inventory_snapshots__lite AS
                WITH base AS (
                SELECT 
                    snapshot_date,
                    UPPER(TRIM(location_id)) AS location_id,
                    UPPER(TRIM(sku)) AS sku,
                    on_hand_qty
                FROM bronze__inventory_snapshots__lite
        )
                 SELECT
                    COALESCE(
                        TRY_CAST(snapshot_date AS DATE),
                        TRY_STRPTIME(snapshot_date, '%d/%m/%Y')::DATE
                    ) AS snapshot_date,
                    location_id,
                    sku,
                    on_hand_qty
                 FROM base;
    """)

    # Close the connection
    conn.close()

if __name__ == "__main__":
    main()
    print("✅ created silver__inventory_snapshots__lite.py executed successfully.")