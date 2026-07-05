from pathlib import Path
import duckdb

def main():
    # Define the path to the DuckDB database file
    script_dir = Path(__file__).resolve().parent
    db_path = r"C:\Users\araro\OneDrive\Desktop\Supply Chain Analytics\supply_chain_analytics.duckdb"

    # Connect to the DuckDB database
    conn = duckdb.connect(database=db_path)

    # Execute the query to create the gold_fact_inventory_movements table
    conn.execute("""
                CREATE OR REPLACE TABLE gold_fact_inventory_movements AS
                SELECT 
                    movement_id      AS InventoryMovementID,
                    movement_date    AS MovementDate,
                    movement_type    AS MovementType,
                    sku AS ProductSKU,
                    from_location_id AS FromLocationID,
                    to_location_id   AS ToLocationID,
                    qty              AS Quantity
                FROM silver__inventory_movements__lite;
    """)

    # Close the connection
    conn.close()

if __name__ == "__main__":
    main()
    print("✅ created gold_fact_inventory_movement.py executed successfully.")