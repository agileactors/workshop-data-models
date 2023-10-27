from unittest.mock import Mock

from app.services.base import BaseDataManager


def test_add_one():
    """
    Test add_one method.
    """

    # Create a mock for the session
    session = Mock()
    data_manager = BaseDataManager(session=session)

    # Create a mock model instance
    model = Mock()

    # Call the add_one method
    data_manager.add_one(model)

    # Assert that the add method of the session was called with the model
    session.add.assert_called_once_with(model)


def test_add_all():
    """
    Test add_all method.
    """

    # Create a mock for the session
    session = Mock()
    data_manager = BaseDataManager(session=session)

    # Create mock model instances
    model1 = Mock()
    model2 = Mock()

    # Call the add_all method with a list of mock models
    data_manager.add_all([model1, model2])

    # Assert that the add_all method of the session was called with the list of models
    session.add_all.assert_called_once_with([model1, model2])


def test_get_one():
    """
    Test get_one method.
    """

    # Create a mock for the session
    session = Mock()
    data_manager = BaseDataManager(session=session)

    # Create a mock model instance
    model = Mock()

    # Call the add_one method
    data_manager.get_one(model)

    # Assert that the add method of the session was called with the model
    session.scalar.assert_called_once_with(model)


def test_get_all():
    """
    Test get_all method.
    """

    # Create a mock for the session
    session = Mock()
    data_manager = BaseDataManager(session=session)

    # Create a mock select statement
    select_stmt = Mock()

    # Create a mock result set
    result_set = Mock()

    # Mock the `all` method of the result set to return a list of items
    expected_data = [Mock(), Mock(), Mock()]
    result_set.all.return_value = expected_data

    # Mock the `scalars` method of the session to return the result set
    session.scalars.return_value = result_set

    # Call the get_all method
    result = data_manager.get_all(select_stmt)

    # Assert that the session's `scalars` method was called with the select statement
    session.scalars.assert_called_once_with(select_stmt)
    assert result == expected_data
