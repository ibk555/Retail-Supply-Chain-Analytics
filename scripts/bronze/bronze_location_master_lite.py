from pathlib import Path
import pandas as pd
import duckdb

def main():
    # Define the path to the DuckDB database file
    script_dir = Path(__file__).resolve().parent
    db_path = r"C:\Users\araro\OneDrive\Desktop\Supply Chain Analytics\supply_chain_analytics.duckdb"

    # Correct relative path 
    xlsx_path = r"C:\Users\araro\OneDrive\Desktop\Supply Chain Analytics\raw__location_master__lite.xlsx" 

    df = pd.read_excel(xlsx_path)

    # Connect to the DuckDB database
    conn = duckdb.connect(database=db_path)
    conn.register("tmp_location_master__lite", df)


    # Execute the query to create the bronze__location_master__lite table
    conn.execute("""
                CREATE OR REPLACE TABLE bronze__location_master__lite
                 AS
                SELECT 
                    location_id,
                    location_name,
                    location_type,
                    region,
                FROM tmp_location_master__lite;
    """)

    # Close the connection
    conn.close()

if __name__ == "__main__":
    main()
    print("✅ created bronze__location_master__lite.py executed successfully.")