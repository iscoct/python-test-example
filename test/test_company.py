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