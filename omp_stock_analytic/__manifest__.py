# -*- coding: utf-8 -*-
{
    'name': "Stock Analytic",

    'summary': """
        Add analytic account to stock operation type """,

    'description': """
         Add analytic account to stock operation type
    """,

    'author': "Seventy Eight Systems",
    'website': "https://www.78systems.com",
    'category': 'Stock',
    'version': '16.0.0.1',
    'license': 'LGPL-3',
    "depends": ["stock_account", "analytic"],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/stock_picking_views.xml',
    ],
    
}
