import uuid

class Company:
    def __init__(self, name, address):
        self.name = name
        self.address = address

class CompanyRegister:
    def __init__(self):
        self.companies = []

    def add_company(self, company):
        record = {
            'company': company,
            'id': uuid.uuid4()
        }
        
        self.companies.append(record)

        return record

    def add_and_create_company_from_its_properties(self, name, address):
        return self.add_company(
            Company(name, address)
        )

    def get_company(self, company_id):
        result = None

        for company in self.companies:
            if company['id'] == company_id: result = company

        return result['company']

    def remove_company(self, company_id):
        self.companies = list(filter(lambda company: company['id'] != company_id, self.companies))
