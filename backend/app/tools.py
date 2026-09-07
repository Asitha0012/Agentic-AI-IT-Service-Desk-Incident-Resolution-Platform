import psycopg
from psycopg.rows import dict_row

DB_URL = "postgresql://aura:aura@localhost:5432/aura"

def get_asset_info(asset_tag: str) -> dict:
    """Lookup an IT asset's details and health score from the database."""
    try:
        # Connect to Postgres and fetch the row as a dictionary
        with psycopg.connect(DB_URL, row_factory=dict_row) as conn:
            with conn.cursor() as cur:
                cur.execute(
                    "SELECT asset_tag, owner_username, asset_type, health_score, status FROM assets WHERE asset_tag = %s", 
                    (asset_tag,)
                )
                result = cur.fetchone()
                
                if result:
                    # Convert the decimal health_score to a float so it can be parsed to JSON later
                    result['health_score'] = float(result['health_score'])
                    return result
                
                return {"error": f"Asset {asset_tag} not found in the database."}
    except Exception as e:
        return {"error": str(e)}