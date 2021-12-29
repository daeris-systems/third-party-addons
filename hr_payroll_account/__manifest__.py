#-*- coding:utf-8 -*-
{
    'name': 'Payroll Accounting',
    'category': 'Human Resources',
    'author': "Daeris + Odoo Community12",
    'license': 'AGPL-3',
    'version': "1.0",
    'summary': 'Manage your employee payroll records',
    'description': "Generic Payroll system Integrated with Accounting - Expense Encoding - Payment Encoding - Company Contribution Management",
    'support': "https://www.daeris.com",
    'website': 'https://www.daeris.com',
    'maintainer': 'daeris.iberia@gmail.com',
    'depends': ['hr_payroll', 'account'],
    'data': ['views/hr_payroll_account_views.xml'],
    #'demo': ['data/hr_payroll_account_demo.xml'],
    #'test': ['../account/test/account_minimal_test.xml'],
    'installable': True,
    'auto_install': False,
}
