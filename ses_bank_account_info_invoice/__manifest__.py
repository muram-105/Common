# -*- coding: utf-8 -*-
{
    'name': "78s - Bank Account Info Invoice",
    'summary': """
        This module adds the bank account details to the invoice.""",
    'description': """
        This module adds a new field at the bank page 'SWIFT Code'
         and adds the bank details to the invoice by selecting the bank on the invoice.""",
    'author': "Seventy Eight Systems",
    'website': "https://www.78systems.com",
    'category': 'Accounting',
    'version': '16.0.1.0.0',
    'depends': ['base', 'account'],
    'data': [
        'views/bank_view.xml',
        'template/account_invoice_template.xml'
    ],
    'license': "Other proprietary",
}
