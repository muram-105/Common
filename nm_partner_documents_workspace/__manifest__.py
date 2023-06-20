# -*- coding: utf-8 -*-
{
    'name': "NM - Partner Documents Workspace ",
    'summary': """
    Centralize the documents attached to the partner workspace
    """,
    'author': "NextMove Business Solutions",
    'website': "https://www.nextmovebs.com",
    'category': 'Documents',
    'version': '1.0',
    'license': 'LGPL-3',
    'depends': ['base', 'documents','nm_reception_treatment_unit'],
    'data': [
        'views/res_partner_views.xml',
        'views/res_config_settings_views.xml',
        'views/documents_documnet.xml',
    ],
    'images':  ["static/description/image.png"],
    'installable': True,
    'auto_install': False,
    'application': False,
    'license': "Other proprietary",
}
