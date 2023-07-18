# -*- coding: utf-8 -*-
{
    'name': "Qatar Employee",
    
    'summary': "This module customizes In-Place the Employees App by adding new fields and functionality to meet the Qatari market needs.",
    'category': 'Human Resources',
    'author': "Seventy Eight Systems",
    'website': "https://www.78systems.com",
    'version': '16.0.0.1',
    'depends': ['base', 'hr'],
    'data': [
        "security/ir.model.access.csv",
        "data/access_rights.xml",
        "data/insurance_sate.xml",
        "data/schedule.xml",
        "views/hr_employee_views.xml",
        "views/res_config.xml",
        "views/hr_dependants_views.xml",
        "views/hr_insurance_views.xml",
        'views/res_company.xml'
    ],
    'license': 'LGPL-3',
}
