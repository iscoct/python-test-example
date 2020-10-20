from src.company import Company, CompanyRegister

def main():
    first_company = Company('First', 'Granada')
    second_company = Company('Second', 'Sevilla')

    company_register = CompanyRegister()
    company_register.add_company(first_company)
    company_register.add_company(second_company)

    return company_register