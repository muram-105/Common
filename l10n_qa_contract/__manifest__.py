# -*- coding: utf-8 -*-
{
    'name': "Qatar Contract",

    'summary': """
    This module customizes In-Place the Contracts App by adding new fields (Allowances) to meet the Qatari market needs.
    """,
    'description': """
    This module changes the label of the (contract start date) to (joining date) since the joining date is the base of all calculations. It also adds two new fields (contract signing date) and (contract authenticating date)
    """,
     'author': "Seventy Eight Systems",
    'website': "https://www.78systems.com",
    'version': '16.0.0.1',
    'category': 'HR',
    'depends': ['base', 'hr_contract'],
    'data': [
        "data/data.xml",
        "views/contract.xml",
    ],
    'license': 'LGPL-3',
}
