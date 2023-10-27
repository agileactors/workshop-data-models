from dotenv import dotenv_values
from pydantic import BaseModel
from pydantic_settings import BaseSettings

# Get the value of an environment variable
config = dotenv_values(".env.variables")
pg_user = config["POSTGRES_USER"]
pg_password = config["POSTGRES_PASSWORD"]
pg_db = config["POSTGRES_DB"]
pg_port = 5432
pg_host = "localhost"


class DatabaseConfig(BaseModel):
    """Backend database configuration parameters.

    Attributes:
        dsn:
            DSN for target database.
    """

    dsn: str = f"postgresql://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_db}"


class Config(BaseSettings):
    """API configuration parameters.

    Automatically read modifications to the configuration parameters
    from environment variables and ``.env`` file.

    Attributes:
        database:
            Database configuration settings.
            Instance of :class:`app.backend.config.DatabaseConfig`.
    """

    database: DatabaseConfig = DatabaseConfig()

    class Config:
        """Pydantic configuration."""

        env_file = ".env"
        env_file_encoding = "utf-8"
        env_nested_delimiter = "__"
        case_sensitive = False


config = Config()
