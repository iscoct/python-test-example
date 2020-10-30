from src.logic import main
from unittest.mock import patch, Mock
import pytest

@patch('src.logic.Company')
@patch('src.logic.CompanyRegister')
def test_if_company_register_was_called(mock_company_register, mock_company):
    main()

    mock_company_register.assert_called()

@patch('src.logic.Company')
def test_if_main_creates_first_company(mock_company):
    main()

    mock_company.assert_any_call('First', 'Granada')

@patch('src.logic.Company')
def test_if_main_creates_second_company(mock_company):
    main()

    mock_company.assert_any_call('Second', 'Sevilla')

@patch('src.logic.CompanyRegister')
@patch('src.logic.Company')
def test_if_main_add_first_company_to_company_register(mock_company, mock_company_register):
    first_company, second_company = 'First company', 'Second company'
    company_register_mock_instance = Mock()
    mock_company_register.return_value = company_register_mock_instance
    mock_company.side_effect = [first_company, second_company]

    main()

    company_register_mock_instance.add_company.assert_any_call(first_company)
    company_register_mock_instance.add_company.assert_any_call(second_company)
