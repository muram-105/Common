# -*- coding: utf-8 -*-
{
    'name': "Products Custom",

    'summary': """
        Products customization""",

    'description': """Add field to product""",
    'category': 'Products',
    'version': '0.1',
    'depends': ['stock','product','sale'],
    'data': [
        'views/product_views.xml',
    ],
     'license': 'LGPL-3',
}
