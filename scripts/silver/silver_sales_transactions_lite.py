from pathlib import Path
import duckdb

def main():
    # Define the path to the DuckDB database file
    script_dir = Path(__file__).resolve().parent
    db_path = r"C:\Users\araro\OneDrive\Desktop\Supply Chain Analytics\supply_chain_analytics.duckdb"

    # Connect to the DuckDB database
    conn = duckdb.connect(database=db_path)

    # Execute the query to create the silver__sales_transactions__lite table
    conn.execute("""
            CREATE OR REPLACE TABLE silver__sales_transactions__lite AS
            SELECT 
                    UPPER(TRIM(transaction_id)) AS transaction_id,
                 
                 COALESCE(
                    TRY_CAST(transaction_ts AS TIMESTAMP),
                    TRY_STRPTIME(transaction_ts, '%d-%m-%y %H:%M')::TIMESTAMP
                 ) AS transaction_ts,

                 CAST(
                    COALESCE(
                        TRY_CAST(transaction_ts AS TIMESTAMP),
                        TRY_STRPTIME(transaction_ts, '%d-%m-%y %H:%M')::TIMESTAMP
                    ) AS DATE
                    ) AS transaction_date,
                 
                channel,
                UPPER(TRIM(location_id)) AS location_id,
                UPPER(TRIM(sku)) AS sku,
                CAST(qty AS INTEGER) AS qty,
                CAST(unit_price AS DOUBLE) AS unit_price
            FROM bronze__sales_transactions__lite;
    """)

    # Close the connection
    conn.close()
    
if __name__ == "__main__":
    main()
    print("✅ created silver__sales_transactions__lite.py executed successfully.")