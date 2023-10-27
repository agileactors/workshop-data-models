import logging

from config import config
from sqlalchemy import create_engine

logging.basicConfig(level=logging.INFO)
engine = create_engine(url=config.database.dsn)


def execute_sql_script(sql_script_path: str):
    """Execute SQL script."""

    try:
        with open(sql_script_path) as f:
            query = "".join(f.readlines())
            engine.execute(query)
        logging.info(f"Executed script {sql_script_path} successfully")
    except Exception as e:
        logging.error(f"Error executing script {sql_script_path}: {str(e)}")


# Execute the first script for test_schema
sql_script_path1 = "app/backend/sql_scripts/setup_pg_db.sql"
execute_sql_script(sql_script_path1)

# Execute the second script for ecommerce_schema
sql_script_path2 = "app/backend/sql_scripts/init_ecommerce_tables.sql"
execute_sql_script(sql_script_path2)

print("--------------------")
logging.info("All scripts executed successfully")
print("--------------------")
