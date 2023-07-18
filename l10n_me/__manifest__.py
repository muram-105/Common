# -*- coding: utf-8 -*-
{
    'name': 'Middle East - Accounting',
    'version': '1.0',
    'category': 'Localization',
    'description': """
This is the base module to manage the accounting chart for the Middle East in Odoo.
=====================================================================================
    """,
    'license': "Other proprietary",
    'website': 'https://www.smartway.co',
    'author': 'Smart Way Business Solutions',
    'depends': ['account','l10n_multilang',],
    'data': [
        "views/journal_view.xml",
        "data/account_chart_template.xml",
        'data/account.account.template.csv',
        "data/account_chart_template_post_data.xml",
        'data/account.group.template.csv',
        "data/account_reconcile_model_template.xml",
        "views/account_move_view.xml",
        "data/res.lang.csv"
    ],
    'installable': True

    
}
