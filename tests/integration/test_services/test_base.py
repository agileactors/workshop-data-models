from app.models.table_name import TableNameModel
from app.services.base import BaseDataManager


def test_add_one_get_one_integration(session_fixture):
    """
    Test add_one method.
    """

    data_manager = BaseDataManager(session=session_fixture)

    # Create a mock model instance
    model = TableNameModel(column_name_1=1, column_name_2="test", column_name_3=1.0)

    # Call the add_one method
    data_manager.add_one(model)
    session_fixture.commit()
    actual = data_manager.get_one(select_stmt=session_fixture.query(TableNameModel).filter(TableNameModel.column_name_2 == "test"))

    assert actual.column_name_1 == 1
    assert actual.column_name_2 == "test"
    assert actual.column_name_3 == 1.0


def test_add_all_get_all_integration(session_fixture):
    """
    Test add_one method.
    """

    data_manager = BaseDataManager(session=session_fixture)

    # Create a mock model instance
    model1 = TableNameModel(column_name_1=1, column_name_2="integration_test1", column_name_3=1.0)
    model2 = TableNameModel(column_name_1=2, column_name_2="integration_test2", column_name_3=2.0)

    # Call the add_one method
    data_manager.add_all([model1, model2])
    session_fixture.commit()
    actual = data_manager.get_all(
        select_stmt=session_fixture.query(TableNameModel).filter(TableNameModel.column_name_2.like("integration_test%"))
    )

    assert actual[0].column_name_1 == 1
    assert actual[0].column_name_2 == "integration_test1"
    assert actual[0].column_name_3 == 1.0
    assert actual[1].column_name_1 == 2
    assert actual[1].column_name_2 == "integration_test2"
    assert actual[1].column_name_3 == 2.0
