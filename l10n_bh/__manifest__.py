# -*- coding: utf-8 -*-
{
    'name': 'Bahrain - Accounting',
    'version': '1.0',
    'category': 'Accounting/Localizations/Account Charts',
    'description': """This is the base module to manage the accounting chart for Bahrain in Odoo.""",
    'website': 'https://www.smartway.co',
    'author': 'Smart Way Business Solutions',
    'depends': ['account', 'l10n_multilang', "l10n_me"],
    'data': [
        'data/account_chart_template.xml',
        "data/account_account_tag_data.xml",
        "data/account_tax_group_data.xml",
        "data/account_tax_template.xml",
        "data/account_tax_report_data.xml",
        "data/account_fiscal_position_template.xml",
        'data/account_chart_template_data.xml',
        'data/decimal_precision.xml',
    ],
    'post_init_hook': 'load_translations',
    'license': "Other proprietary",
}
