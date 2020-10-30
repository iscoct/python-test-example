from src.company import Company, CompanyRegister
from unittest.mock import patch
import pytest

def test_if_company_can_be_created_correctly():
    name, address = 'Dummy Name', 'Dummy Address'
    company = Company(name, address)

    assert name == company.name and address == company.address

def test_if_company_register_adds_a_company_correctly():
    name, address = 'Dummy Name', 'Dummy Address'
    company = Company(name, address)
    company_register = CompanyRegister()

    company_register.add_company(company)

    assert len(company_register.companies) == 1
    assert company_register.companies[0]['company'] == company

def test_if_a_company_can_be_get_by_its_id():
    name, address = 'Dummy Name', 'Dummy Address'
    company = Company(name, address)
    company_register = CompanyRegister()

    company_record = company_register.add_company(company)

    assert company_register.get_company(company_record['id']) == company

def test_if_a_company_can_be_remove_by_its_id():
    name, address = 'Dummy Name', 'Dummy Address'
    company = Company(name, address)
    company_register = CompanyRegister()

    company_record = company_register.add_company(company)
    company_register.remove_company(company_record['id'])

    assert len(company_register.companies) == 0

@patch('src.company.uuid')
def test_if_create_company_id_via_unique_id(mock_uuid):
    name, address = 'Dummy Name', 'Dummy Address'
    company = Company(name, address)
    company_register = CompanyRegister()

    company_register.add_company(company)

    mock_uuid.uuid4.assert_called_once()

def test_if_create_company_id_via_unique_id_with_mocker(mocker):
    mock_uuid = mocker.patch('src.company.uuid')
    name, address = 'Dummy Name', 'Dummy Address'
    company = Company(name, address)
    company_register = CompanyRegister()

    company_register.add_company(company)

    mock_uuid.uuid4.assert_called_once()

@patch('src.company.Company')
def test_ïf_add_and_create_company_from_its_properties_create_a_company(mock_company):
    name, address = 'name', 'address'
    company_register = CompanyRegister()

    company_register.add_and_create_company_from_its_properties(name, address)

    mock_company.assert_called_with(name, address)

@patch('src.company.Company')
def test_if_calls_add_company_with_the_new_company(mock_company):
    mock_company.return_value = 'Dummy Company'
    company_register = CompanyRegister()

    with patch.object(company_register, 'add_company') as add_company_mock:
        add_company_mock.return_value = 'Dummy Add Company'

        company = company_register.add_and_create_company_from_its_properties('name', 'address')

        add_company_mock.assert_called_with(mock_company.return_value)
        assert company == add_company_mock.return_value

@patch('src.company.Company')
@patch('src.company.CompanyRegister.add_company')
def test_if_we_can_mock_a_company_and_a_method_in_the_same_file(add_company_mock, mock_company):
    mock_company.return_value = 'Dummy Company'
    company_register = CompanyRegister()
    add_company_mock.return_value = 'Dummy Add Company'

    company = company_register.add_and_create_company_from_its_properties('name', 'address')

    add_company_mock.assert_called_with(mock_company.return_value)
    assert company == add_company_mock.return_value