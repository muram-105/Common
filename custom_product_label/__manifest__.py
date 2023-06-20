# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Product Label Arabic',
    'version' : '16.0',
    'summary': 'Product Arabic Labels',
    'sequence': 10,
    'description': """Product Arabic Labels
    """,
    'category': 'Product',
    'depends': ['product'],
    'data': [

        'views/product_label_layout_view.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
