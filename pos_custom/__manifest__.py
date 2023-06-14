# -*- coding: utf-8 -*-
{
    'name': "POS Custom",

    'summary': """
        This moduel add custom feature to pos
        """,

    'description': """
        This moduel add custom feature to pos
    """,

    'author': "Seventy Eight Systems",
    'website': "https://www.78systems.com",
    'category': 'POS',
    'version': '16.0.0.1',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['point_of_sale'],

    # always loaded
    'data': [
        'views/pos_views.xml',
    ],
    
}
