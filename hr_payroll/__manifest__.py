#-*- coding:utf-8 -*-
{
    'name': 'Payroll',
    'category': 'Human Resources',
    'author': "Daeris + Odoo Community12",
    'license': 'AGPL-3',
    'version': "1.0",
    'summary': 'Manage your employee payroll records',
    'description': "Manage your employee payroll records",
    'support': "https://www.daeris.com",
    'website': 'https://www.daeris.com',
    'maintainer': 'daeris.iberia@gmail.com',
    'depends': ['hr_contract','hr_holidays',],
    'data': [
        'security/hr_payroll_security.xml',
        'security/ir.model.access.csv',
        'wizard/hr_payroll_payslips_by_employees_views.xml',
        'views/hr_contract_views.xml',
        'views/hr_salary_rule_views.xml',
        'views/hr_payslip_views.xml',
        'views/hr_employee_views.xml',
        'data/hr_payroll_sequence.xml',
        'views/hr_payroll_report.xml',
        'data/hr_payroll_data.xml',
        'data/mail_template.xml',
        'data/hr_contract_type_data.xml',
        'wizard/hr_payroll_contribution_register_report_views.xml',
        'views/res_config_settings_views.xml',
        'views/report_contributionregister_templates.xml',
        'views/report_payslip_templates.xml',
        'views/report_payslipdetails_templates.xml',
        'views/schedule_cron.xml',
        'views/hr_payroll.xml',
        'views/hr_payslip_wizard_view.xml',
        'views/hr_mass_payroll_wizard.xml',
        'views/menu_payslip_report.xml',
        'views/hr_multi_payslip_confirm_views.xml',
        'views/company_views.xml',
    ],
    #'demo': ['data/hr_payroll_demo.xml'],
    'installable': True,
    'auto_install': False,
}
