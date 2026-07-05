from pathlib import Path
import duckdb

def main():
    # Define the path to the DuckDB database file
    script_dir = Path(__file__).resolve().parent
    db_path = r"C:\Users\araro\OneDrive\Desktop\Supply Chain Analytics\supply_chain_analytics.duckdb"

    # Connect to the DuckDB database
    conn = duckdb.connect(database=db_path)

    # Execute the query to create the silver__inventory_movements__lite table
    conn.execute("""
                CREATE OR REPLACE TABLE silver__inventory_movements__lite AS
                WITH base AS (
                SELECT 
                    UPPER(TRIM(movement_id)) AS movement_id,
                    movement_date,
                    UPPER(TRIM(movement_type)) AS movement_type,
                    UPPER(TRIM(sku)) AS sku,
                    UPPER(TRIM(from_location_id)) AS from_location_id,
                    UPPER(TRIM(to_location_id)) AS to_location_id,
                    qty
                FROM bronze__inventory_movements__lite
        )
                 SELECT
                    movement_id,
                    COALESCE(
                        TRY_CAST(movement_date AS DATE),
                        TRY_STRPTIME(movement_date, '%d/%m/%Y')::DATE
                    ) AS movement_date,
                    movement_type,
                    sku,
                    from_location_id,
                    to_location_id,
                    qty
                 FROM base;
    """)

    # Close the connection
    conn.close()

if __name__ == "__main__":
    main()
    print("✅ created silver__inventory_movements__lite.py executed successfully.")