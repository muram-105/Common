# -*- coding: utf-8 -*-
{
    'name': "Custom PoS Report",
    'summary': "Add Arabic to the PoS reprot",
    'description': """ """,
    'category': 'Point of Sale',
    'version': '1.1',
    'license': 'LGPL-3',
    'depends': ['point_of_sale'],
    'data': [
    ],
    'assets': {
        'point_of_sale.assets': [
            'custom_pos_report/static/src/js/models.js',
            'custom_pos_report/static/src/xml/OrderReceipt.xml'],
        }
}
