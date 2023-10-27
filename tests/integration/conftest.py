import pytest
import sqlalchemy
from sqlalchemy import orm

from app.models.table_name import TableNameModel


@pytest.fixture(scope="module")
def session_fixture():
    """Create a session fixture for the operational events database"""

    engine = sqlalchemy.create_engine(url="postgresql://myuser:mypassword@localhost:5433/mydatabase")
    session_maker = orm.sessionmaker(bind=engine)
    session = session_maker()

    yield session

    # Cleanup all the data from the operational events database
    session.query(TableNameModel).delete()
    session.commit()
