# -*- coding: utf-8 -*-
{
    	'price': "15",
	'currency': "USD",
	'name': "POS Session Summary",

    'summary': """
       This Odoo addon provides a new report for the pos.session which enables users to print the POS Session Summary, including basic session information and payments summary. This addon is a simple yet powerful tool for Odoo users who want to better manage their POS sessions.""",

    'description': """
        This Odoo addon adds a new report to the pos.session which allows the user to print the POS Session Summary. The report includes the session basic information and the payments summary. This simple module enhances the functionality of Odoo's point of sale (POS) system, allowing users to easily generate a summary report of their POS sessions.
    """,
    'images': ['images/main_screenshot.png'],
    'author': "Seventy Eight Systems",
    'website': "https://www.78systems.com",
    'category': 'POS',
    'version': '16.0.0.1',
    'license': 'LGPL-3',
    'depends': ['point_of_sale'],

    # always loaded
    'data': [
        'report/pos_session_report.xml',
    ],
   
}
