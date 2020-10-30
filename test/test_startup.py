from src.startup import StartUp, Company
from unittest.mock import patch, Mock
import pytest

class TestStartUp:

    def test_if_num_employees_exists_and_not_name(self, mocker):
        patcher = patch.object(StartUp, '__bases__', (mocker.Mock,))

        with patcher:
            patcher.is_local = True

            name, address, num_employees = 'Name', 'Address', 7
            start_up = StartUp(name, address, num_employees)

            assert hasattr(start_up, 'num_employees')
            assert not hasattr(start_up, 'name')

    def test_if_num_employees_exists_and_not_address(self, mocker):
        StartUp.__bases__ = (mocker.Mock,)

        dummy = StartUp('dummy', 'dummy', 3)

        assert hasattr(dummy, 'num_employees')
        assert not hasattr(dummy, 'address')

    @patch('src.startup.StartUp.get_name', return_value='some name')
    @patch('src.startup.StartUp.get_address', return_value='some address')
    def test_if_we_can_mock_several_methods(self, get_address_mock, get_name_mock):
        start_up = StartUp('dummy', 'dummy', 2)

        assert 'some name' in str(start_up) and 'some address' in str(start_up)
        get_address_mock.assert_called()
        get_name_mock.assert_called()

    @patch('src.startup.StartUp.get_name', return_value='some name')
    @patch('src.startup.StartUp.get_address', return_value='some address')
    def test_if_we_can_mock_several_methods_and_base_class(self, get_address_mock, get_name_mock):
        patcher = patch.object(StartUp, '__bases__', (Mock,))

        with patcher:
            patcher.is_local = True

            start_up = StartUp('dummy', 'dummy', 7)

            assert 'some name' in str(start_up) and 'some address' in str(start_up)

    def test_if_we_can_mock_several_methods_in_a_diff_way(self):
        name, address = 'some name', 'some address'

        with patch('src.startup.StartUp.get_name', return_value=name):
            with patch('src.startup.StartUp.get_address', return_value=address):
                start_up = StartUp('dummy', 'dummy', 7)

                assert name in str(start_up) and address in str(start_up)

    def test_if_we_can_mock_several_methods_in_a_different_way_and_base_class(self):
        name, address = 'some name', 'some address'
        patcher = patch.object(StartUp, '__bases__', (Mock,))
        
        with patch('src.startup.StartUp.get_name', return_value=name), \
            patch('src.startup.StartUp.get_address', return_value=address), \
            patcher:
            patcher.is_local = True
            start_up = StartUp('dummy', 'dummy', 7)

            assert name in str(start_up) and address in str(start_up)
            assert not hasattr(start_up, 'address')
